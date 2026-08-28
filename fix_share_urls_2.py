import os
import re

html_files = ["index.html"] + [f"massage-{c}.html" for c in ["hengelo", "almelo", "oldenzaal", "haaksbergen", "borne", "losser"]] + ["de/index.html"] + [f"de/massage-{c}.html" for c in ["gronau", "ahaus", "ochtrup", "bad-bentheim", "vreden", "muenster"]]

for filepath in html_files:
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()

        # Determine exact URL
        if filepath == "index.html":
            exact_url = "https://shiatsumassage-iyashi.com/"
        elif filepath == "de/index.html":
            exact_url = "https://shiatsumassage-iyashi.com/de/"
        else:
            exact_url = f"https://shiatsumassage-iyashi.com/{filepath}"
            
        # We can just do a brute force string replacement of the Netlify URL to the exact_url
        content = content.replace("https://storied-malabi-d51188.netlify.app/", exact_url)
        content = content.replace("https://storied-malabi-d51188.netlify.app", exact_url)

        with open(filepath, "w") as f:
            f.write(content)

# Fix sitemap.xml
if os.path.exists("sitemap.xml"):
    with open("sitemap.xml", "r") as f:
        sitemap = f.read()
    sitemap = sitemap.replace("https://storied-malabi-d51188.netlify.app/", "https://shiatsumassage-iyashi.com/")
    sitemap = sitemap.replace("https://storied-malabi-d51188.netlify.app", "https://shiatsumassage-iyashi.com")
    with open("sitemap.xml", "w") as f:
        f.write(sitemap)
        
