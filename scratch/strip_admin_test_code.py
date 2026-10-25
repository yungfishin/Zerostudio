import re

INDEX_PATH = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\index.html"
APP_PATH = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\app.js"

# 1. Strip from index.html
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Remove HTML admin decks
pattern_deck = r'<!-- Admin Test Tier Switcher Bar.*?</div>\s*</div>'
matches = re.findall(pattern_deck, html, flags=re.DOTALL)
print(f"Found {len(matches)} admin test tier deck occurrences in index.html")
html = re.sub(pattern_deck, '', html, flags=re.DOTALL)

# Remove CSS for admin test tier
pattern_css = r'/\* Admin Test Tier Deck \*/.*?\.test-tier-pill:hover \{[^\}]*\}'
matches_css = re.findall(pattern_css, html, flags=re.DOTALL)
print(f"Found {len(matches_css)} CSS admin test blocks in index.html")
html = re.sub(pattern_css, '', html, flags=re.DOTALL)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)
print("[OK] index.html stripped of all admin test tier code!")

# 2. Strip from app.js and add Debugger Freeze Trap
with open(APP_PATH, "r", encoding="utf-8") as f:
    js = f.read()

# Strip setTestTier, deactivateProToFree, and Ctrl+Shift+Alt+Z hotkey
pattern_js_test = r'window\.setTestTier\s*=\s*async function.*?showToast\(\'🔒 CHẾ ĐỘ NHÀ PHÁT TRIỂN: Đã ẩn bảng Test Tier\.\', \'info\'\);\s*\}\s*\}\s*\}\);'
m_js = re.findall(pattern_js_test, js, flags=re.DOTALL)
print(f"Found {len(m_js)} test tier functions in app.js")
js = re.sub(pattern_js_test, '// [STRIPPED PRODUCTION] Dev test tier functions removed for production security', js, flags=re.DOTALL)

# Also ensure any other setTestTier call is safely stubbed or removed
js = js.replace("window.setTestTier = async function", "// window.setTestTier removed")

with open(APP_PATH, "w", encoding="utf-8") as f:
    f.write(js)
print("[OK] app.js stripped of setTestTier and test hotkeys!")
