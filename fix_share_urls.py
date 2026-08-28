import os
import re
from urllib.parse import quote

dutch_files = ["index.html"] + [f"massage-{c}.html" for c in ["hengelo", "almelo", "oldenzaal", "haaksbergen", "borne", "losser"]]
german_files = ["de/index.html"] + [f"de/massage-{c}.html" for c in ["gronau", "ahaus", "ochtrup", "bad-bentheim", "vreden", "muenster"]]

def fix_file(filepath, is_german):
    if not os.path.exists(filepath): return
    
    with open(filepath, "r") as f:
        content = f.read()

    # Determine exact URL
    if filepath == "index.html":
        exact_url = "https://shiatsumassage-iyashi.com/"
    elif filepath == "de/index.html":
        exact_url = "https://shiatsumassage-iyashi.com/de/"
    else:
        # e.g., massage-hengelo.html -> https://shiatsumassage-iyashi.com/massage-hengelo.html
        # e.g., de/massage-gronau.html -> https://shiatsumassage-iyashi.com/de/massage-gronau.html
        exact_url = f"https://shiatsumassage-iyashi.com/{filepath}"
    
    # 1. Fix Schema.org JSON-LD
    content = content.replace("https://storied-malabi-d51188.netlify.app/images/logo.png", "https://shiatsumassage-iyashi.com/images/logo.png")
    # Carefully replace the generic @id and url in Schema (might be hardcoded)
    content = re.sub(r'"@id":\s*"https://storied-malabi-d51188.netlify.app/.*?"', f'"@id": "{exact_url}"', content)
    content = re.sub(r'"url":\s*"https://storied-malabi-d51188.netlify.app/.*?"', f'"url": "{exact_url}"', content)

    # Prepare localized texts
    wa_text = "Schauen Sie sich diese Website von Shiatsu Massage Iyashi an!" if is_german else "Bekijk deze website van Shiatsu Massage Iyashi!"
    wa_promo = "Schauen Sie sich diese Freundschaftsaktion bei Shiatsu Massage Iyashi an! Aktionscode: Friend26Aki" if is_german else "Bekijk deze Vriendenpromotie bij Shiatsu Massage Iyashi! Actiecode: Friend26Aki"
    x_text = "Shiatsu Massage Iyashi in Enschede" # Same for both
    x_promo = "Freundschaftsaktion bei Shiatsu Massage Iyashi" if is_german else "Vriendenpromotie bij Shiatsu Massage Iyashi"
    
    # 2. Fix Social Buttons (regex replacement)
    # WhatsApp standard
    wa_std_pattern = r'href="https://api\.whatsapp\.com/send\?text=[^"]*?- [^"]*?"'
    content = re.sub(wa_std_pattern, f'href="https://api.whatsapp.com/send?text={quote(wa_text)} - {exact_url}"', content)
    
    # WhatsApp promo
    wa_promo_pattern = r'href="https://api\.whatsapp\.com/send\?text=[^"]*?Friend26Aki - [^"]*?"'
    content = re.sub(wa_promo_pattern, f'href="https://api.whatsapp.com/send?text={quote(wa_promo)} - {exact_url}"', content)
    
    # Facebook
    fb_pattern = r'href="https://www\.facebook\.com/sharer/sharer\.php\?u=[^"]*?"'
    content = re.sub(fb_pattern, f'href="https://www.facebook.com/sharer/sharer.php?u={exact_url}"', content)
    
    # X/Twitter standard
    x_std_pattern = r'href="https://twitter\.com/intent/tweet\?url=[^"&]*?&text=[^"]*?"'
    content = re.sub(x_std_pattern, f'href="https://twitter.com/intent/tweet?url={exact_url}&text={quote(x_text)}"', content)
    
    # X/Twitter promo (if any)
    x_promo_pattern = r'href="https://twitter\.com/intent/tweet\?url=[^"&]*?&text=.*?promotie.*?"'
    content = re.sub(x_promo_pattern, f'href="https://twitter.com/intent/tweet?url={exact_url}&text={quote(x_promo)}"', content, flags=re.IGNORECASE)
    
    # LinkedIn
    in_pattern = r'href="https://www\.linkedin\.com/sharing/share-offsite/\?url=[^"]*?"'
    content = re.sub(in_pattern, f'href="https://www.linkedin.com/sharing/share-offsite/?url={exact_url}"', content)

    with open(filepath, "w") as f:
        f.write(content)

for f in dutch_files:
    fix_file(f, False)
for f in german_files:
    fix_file(f, True)

