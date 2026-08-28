import os
import re

german_files = ["de/index.html"] + [f"de/massage-{c}.html" for c in ["gronau", "ahaus", "ochtrup", "bad-bentheim", "vreden", "muenster"]]

for filepath in german_files:
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()

        # The Dutch links block looks like:
        # <p style="margin-top: 1rem; font-size: 0.8rem;">
        #     <a href="../massage-hengelo.html"...
        # ...
        # </p>
        
        # We can use regex to remove the paragraph that contains "Massage Hengelo"
        pattern = r'<p style="margin-top: 1rem; font-size: 0\.8rem;">\s*<a href="[^"]*?massage-hengelo\.html".*?</p>'
        
        content = re.sub(pattern, '', content, flags=re.DOTALL)

        with open(filepath, "w") as f:
            f.write(content)
