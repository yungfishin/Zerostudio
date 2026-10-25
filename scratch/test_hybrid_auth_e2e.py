import json, time, secrets, base64, subprocess
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

KEY_DIR = Path(r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\assets\keys")
priv_pem = (KEY_DIR / "drm_private_key.pem").read_bytes()
private_key = serialization.load_pem_private_key(priv_pem, password=None)

claims = {
    "v": 1,
    "hwid": "DEV-SEC-2F353F87",
    "tier": "ultra",
    "key": "ZERO-ULTRA-TEST",
    "iat": int(time.time()),
    "exp": int(time.time()) + 315360000,
    "nonce": secrets.token_hex(8)
}

claims_bytes = json.dumps(claims, separators=(',', ':')).encode('utf-8')
b64_claims = base64.urlsafe_b64encode(claims_bytes).decode('utf-8').rstrip('=')

sig = private_key.sign(claims_bytes, padding.PKCS1v15(), hashes.SHA256())
b64_sig = base64.urlsafe_b64encode(sig).decode('utf-8').rstrip('=')
token = f"ZS-LIC.{b64_claims}.{b64_sig}"

# Test with Node
key_posix = (KEY_DIR / "drm_public_key.pem").as_posix()
node_script = f"""
const fs = require('fs');
const crypto = require('crypto');

const pubPem = fs.readFileSync('{key_posix}', 'utf8');
const lines = pubPem.split('\\n').filter(l => !l.startsWith('---')).map(l => l.trim()).join('');
const binary = Buffer.from(lines, 'base64');

async function verify(token) {{
    const key = await crypto.subtle.importKey(
        'spki',
        binary,
        {{ name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }},
        false,
        ['verify']
    );
    const [_, b64Claims, b64Sig] = token.split('.');
    const padClaims = b64Claims + '='.repeat((4 - b64Claims.length % 4) % 4);
    const padSig = b64Sig + '='.repeat((4 - b64Sig.length % 4) % 4);

    const dataBytes = Buffer.from(padClaims, 'base64');
    const sigBytes = Buffer.from(padSig, 'base64');

    const valid = await crypto.subtle.verify(
        'RSASSA-PKCS1-v1_5',
        key,
        sigBytes,
        dataBytes
    );
    console.log('Node WebCrypto Verify Result:', valid);
    if (!valid) process.exit(1);
}}
verify('{token}');
"""

p = subprocess.run(["node", "-e", node_script], capture_output=True, text=True)
print("Node Output:", p.stdout)
if p.stderr:
    print("Node Error:", p.stderr)
assert "Result: true" in p.stdout
print("[OK] Python Mint -> Node WebCrypto Verify PASSED 100%!")
