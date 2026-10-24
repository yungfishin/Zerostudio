const verifyHandler = require('../netlify/functions/verify-device').handler;
const unbindHandler = require('../netlify/functions/unbind-device').handler;

async function runTests() {
    console.log("=== TESTING CLOUD CENTRAL DEVICE VERIFICATION ENGINE ===");

    // Test 1: Bind Device A on Pro Key
    const res1 = await verifyHandler({
        httpMethod: 'POST',
        headers: { 'client-ip': '1.1.1.1' },
        body: JSON.stringify({ license_key: 'ZERO-PRO-TEST-1001', device_id: 'DEV-MACHINE-A' })
    }, {});
    const d1 = JSON.parse(res1.body);
    console.log("1. Bind Device A:", res1.statusCode, d1.message, "| Cert:", !!d1.certificate);
    if (res1.statusCode !== 200 || !d1.success) throw new Error("Test 1 Failed");

    // Test 2: Try bind Device B on same Pro Key (Should be rejected: Strike 1)
    const res2 = await verifyHandler({
        httpMethod: 'POST',
        headers: { 'client-ip': '2.2.2.2' },
        body: JSON.stringify({ license_key: 'ZERO-PRO-TEST-1001', device_id: 'DEV-MACHINE-B' })
    }, {});
    const d2 = JSON.parse(res2.body);
    console.log("2. Device B Strike 1:", res2.statusCode, d2.message);
    if (res2.statusCode !== 400 || d2.strikes !== 1) throw new Error("Test 2 Failed");

    // Test 3: Device B tries again (Strike 2)
    const res3 = await verifyHandler({
        httpMethod: 'POST',
        headers: { 'client-ip': '2.2.2.2' },
        body: JSON.stringify({ license_key: 'ZERO-PRO-TEST-1001', device_id: 'DEV-MACHINE-B' })
    }, {});
    const d3 = JSON.parse(res3.body);
    console.log("3. Device B Strike 2:", res3.statusCode, d3.strikes);
    if (d3.strikes !== 2) throw new Error("Test 3 Failed");

    // Test 4: Device B tries 3rd time (Strike 3 -> Permanent BAN)
    const res4 = await verifyHandler({
        httpMethod: 'POST',
        headers: { 'client-ip': '2.2.2.2' },
        body: JSON.stringify({ license_key: 'ZERO-PRO-TEST-1001', device_id: 'DEV-MACHINE-B' })
    }, {});
    const d4 = JSON.parse(res4.body);
    console.log("4. Device B Strike 3:", res4.statusCode, d4.error, d4.banned);
    if (res4.statusCode !== 403 || !d4.banned) throw new Error("Test 4 Failed");

    // Test 5: Unbind Device A
    const res5 = await unbindHandler({
        httpMethod: 'POST',
        body: JSON.stringify({ license_key: 'ZERO-PRO-TEST-1001', device_id: 'DEV-MACHINE-A' })
    }, {});
    const d5 = JSON.parse(res5.body);
    console.log("5. Unbind Device A:", res5.statusCode, d5.message);
    if (res5.statusCode !== 200 || !d5.success) throw new Error("Test 5 Failed");

    // Test 6: Try to unbind AGAIN immediately (Should trigger 30-Day Cooldown!)
    const res6 = await unbindHandler({
        httpMethod: 'POST',
        body: JSON.stringify({ license_key: 'ZERO-PRO-TEST-1001', device_id: 'DEV-MACHINE-C' })
    }, {});
    const d6 = JSON.parse(res6.body);
    console.log("6. 30-Day Cooldown Enforcement:", res6.statusCode, d6.error, "| Remaining days:", d6.remaining_days);
    if (res6.statusCode !== 400 || d6.error !== 'COOLDOWN_ACTIVE') throw new Error("Test 6 Failed");

    console.log("\n>>> ALL CLOUD SECURITY & ANTI-TAMPER TESTS PASSED 100%! <<<");
}

runTests().catch(err => {
    console.error("TEST FAILED:", err);
    process.exit(1);
});
