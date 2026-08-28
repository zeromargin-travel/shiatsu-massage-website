import os

# 1. Update de/index.html with SEO footer links
german_main_file = "de/index.html"
german_footer_links = """        <p style="margin-top: 1rem; font-size: 0.8rem;">
            <a href="massage-gronau.html" style="color: #999; text-decoration: none; margin: 0 5px;">Massage Gronau</a> | 
            <a href="massage-ahaus.html" style="color: #999; text-decoration: none; margin: 0 5px;">Massage Ahaus</a> | 
            <a href="massage-ochtrup.html" style="color: #999; text-decoration: none; margin: 0 5px;">Massage Ochtrup</a> | 
            <a href="massage-bad-bentheim.html" style="color: #999; text-decoration: none; margin: 0 5px;">Massage Bad Bentheim</a> | 
            <a href="massage-vreden.html" style="color: #999; text-decoration: none; margin: 0 5px;">Massage Vreden</a> | 
            <a href="massage-muenster.html" style="color: #999; text-decoration: none; margin: 0 5px;">Massage Münster</a>
        </p>"""

if os.path.exists(german_main_file):
    with open(german_main_file, "r") as f:
        content = f.read()
    
    if "Massage Gronau" not in content:
        # Insert before </footer>
        content = content.replace("    </footer>", german_footer_links + "\n    </footer>")
        with open(german_main_file, "w") as f:
            f.write(content)

# 2. Create sitemap.xml
sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://storied-malabi-d51188.netlify.app/</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/massage-hengelo.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/massage-almelo.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/massage-oldenzaal.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/massage-haaksbergen.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/massage-borne.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/massage-losser.html</loc></url>
    
    <url><loc>https://storied-malabi-d51188.netlify.app/de/</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/de/massage-gronau.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/de/massage-ahaus.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/de/massage-ochtrup.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/de/massage-bad-bentheim.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/de/massage-vreden.html</loc></url>
    <url><loc>https://storied-malabi-d51188.netlify.app/de/massage-muenster.html</loc></url>
</urlset>"""

with open("sitemap.xml", "w") as f:
    f.write(sitemap_content)

