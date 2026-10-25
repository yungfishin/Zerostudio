INDEX_PATH = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    c = f.read()

target = '<script src="./libs/tesseract.min.js"></script>'
replace = """<script src="./libs/tesseract.min.js"></script>
    <!-- Cryptographic Verification Core (RSA-2048 Hybrid Authentication & Anti-Debug) -->
    <script src="./assets/keys/drm_public_key.js"></script>
    <script src="./assets/keys/drm_verifier.js"></script>"""

assert target in c, "target not found"
c = c.replace(target, replace, 1)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(c)

print("SUCCESS: Added drm_verifier.js and drm_public_key.js to index.html!")
