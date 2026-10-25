import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

KEY_DIR = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\assets\keys"
os.makedirs(KEY_DIR, exist_ok=True)

PRIV_PATH = os.path.join(KEY_DIR, "drm_private_key.pem")
PUB_PATH = os.path.join(KEY_DIR, "drm_public_key.pem")
PUB_JS_PATH = os.path.join(KEY_DIR, "drm_public_key.js")

if not os.path.exists(PRIV_PATH):
    print("Generating new RSA-2048 Master Keypair...")
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    pem_priv = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    pem_pub = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(PRIV_PATH, "wb") as f:
        f.write(pem_priv)

    with open(PUB_PATH, "wb") as f:
        f.write(pem_pub)
else:
    print("Reading existing RSA-2048 Keypair...")
    with open(PUB_PATH, "rb") as f:
        pem_pub = f.read()

# Convert public key PEM to SPKI base64 clean string for WebCrypto / JS
pub_lines = [l.strip() for l in pem_pub.decode("utf-8").splitlines() if not l.startswith("---")]
spki_b64 = "".join(pub_lines)

js_content = f"""// ZeroStudio Cryptographic Public Key (Embedded for Client-Side WASM / WebCrypto)
window.ZEROSTUDIO_PUBLIC_KEY_SPKI = "{spki_b64}";
"""

with open(PUB_JS_PATH, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"[OK] Keys saved:")
print(f"  Private: {PRIV_PATH}")
print(f"  Public: {PUB_PATH}")
print(f"  Public JS: {PUB_JS_PATH}")
print(f"  SPKI Base64 length: {len(spki_b64)}")
