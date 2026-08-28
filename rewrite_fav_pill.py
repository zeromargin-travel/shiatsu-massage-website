import os

# 1. Update CSS
css_path = "css/style.css"
if os.path.exists(css_path):
    with open(css_path, "r") as f:
        content = f.read()
    
    # Remove old .fav-btn
    import re
    content = re.sub(r'/\* Floating Favorite Button \*/.*?(?=\Z|/\*)', '', content, flags=re.DOTALL)
    
    # Add new .floating-fav-btn
    new_css = """
/* Floating Favorite Pill Button */
.floating-fav-btn {
    background-color: #fff;
    color: #d89b00;
    border: 1px solid #ffca28;
}
.floating-fav-btn.active {
    background-color: #ffca28;
    color: #fff;
    border: 1px solid #ffca28;
}
.floating-fav-btn:hover {
    background-color: #fff9e6;
    color: #d89b00;
}
"""
    content += new_css
    
    with open(css_path, "w") as f:
        f.write(content)

# 2. Update JS
js_path = "js/script.js"
if os.path.exists(js_path):
    with open(js_path, "r") as f:
        content = f.read()
    
    # Replace id="floating-fav-btn" with class="floating-fav-btn"
    content = content.replace('document.getElementById("floating-fav-btn")', 'document.querySelector(".floating-fav-btn")')
    
    with open(js_path, "w") as f:
        f.write(content)

# 3. Update HTML files
dutch_files = ["index.html"] + [f"massage-{c}.html" for c in ["hengelo", "almelo", "oldenzaal", "haaksbergen", "borne", "losser"]]
german_files = ["de/index.html"] + [f"de/massage-{c}.html" for c in ["gronau", "ahaus", "ochtrup", "bad-bentheim", "vreden", "muenster"]]

old_fav_btn = '<a href="#" id="floating-fav-btn" class="fav-btn" title="Save this page">★</a>'

dutch_fav_pill = '        <a href="#" class="floating-btn floating-fav-btn" title="Save this page">★ <span>Bewaar</span></a>\n'
german_fav_pill = '        <a href="#" class="floating-btn floating-fav-btn" title="Save this page">★ <span>Speichern</span></a>\n'

def process_html(filepath, pill_injection):
    if not os.path.exists(filepath): return
    with open(filepath, "r") as f:
        content = f.read()
    
    # Remove old button if exists (ignoring leading/trailing spaces for exact match, so using strip and replace or regex)
    # Actually I used `    <a href="#" id="floating-fav-btn" class="fav-btn" title="Save this page">★</a>` earlier.
    content = re.sub(r'\s*<a href="#" id="floating-fav-btn" class="fav-btn" title="Save this page">★</a>', '', content)
    
    # Inject new pill button at the top of the floating-cta-container
    if "floating-fav-btn" not in content:
        content = content.replace('<div class="floating-cta-container">', '<div class="floating-cta-container">\n' + pill_injection)
        
    with open(filepath, "w") as f:
        f.write(content)

for f in dutch_files:
    process_html(f, dutch_fav_pill)

for f in german_files:
    process_html(f, german_fav_pill)

