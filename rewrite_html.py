import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract sections using regex
def extract_section(html, section_id):
    # Matches <section id="XYZ"> ... </section>
    pattern = re.compile(rf'(<section[^>]*id="{section_id}"[^>]*>.*?</section>)', re.DOTALL)
    match = pattern.search(html)
    return match.group(1) if match else ""

# Extract everything before main
pre_main = html[:html.find('<main>')]
# Extract everything after main
post_main = html[html.find('</main>'):]

# Update Nav
nav_pattern = re.compile(r'<nav class="nav-menu".*?</nav>', re.DOTALL)
new_nav = """<nav class="nav-menu" id="navMenu">
            <ul>
                <li><a href="#booking" style="font-weight: 600; color: var(--primary-color);">Afspraak Maken</a></li>
                <li><a href="#about">Over Shiatsu</a></li>
                <li><a href="#jun">Profiel</a></li>
                <li><a href="#reviews">Recensies</a></li>
                <li><a href="#pricing">Tarieven & Acties</a></li>
                <li><a href="#info">Info & FAQ</a></li>
            </ul>
        </nav>"""
pre_main = nav_pattern.sub(new_nav, pre_main)

# Extract sections
hero = extract_section(html, "home")
about = extract_section(html, "about")
video = extract_section(html, "video")
jun = extract_section(html, "jun")
reviews = extract_section(html, "reviews")
pricing = extract_section(html, "pricing")
autumn = extract_section(html, "autumn-offer")
campaigns = extract_section(html, "campaigns")
cadeaubon = extract_section(html, "cadeaubon")
booking = extract_section(html, "booking")
info = extract_section(html, "info")
faq = extract_section(html, "faq")
workshop = extract_section(html, "workshop")
updates = extract_section(html, "updates")
map_sec = extract_section(html, "map")

# Apply text fixes
# Fix FAQ language
faq = faq.replace("<h4>1. Is your massage like Thai massage❓</h4>", "<h4>1. Lijkt jullie massage op Thaise massage❓</h4>")
# Remove 感謝券
cadeaubon = cadeaubon.replace("Cadeaubon (感謝券)", "Cadeaubon")

# Build new main content
new_main = "\n".join([
    "    <main>",
    "        <!-- 1. Hero -->",
    "        " + hero,
    "        <!-- 2. About Shiatsu -->",
    "        " + about,
    "        <!-- 3. Video -->",
    "        " + video,
    "        <!-- 4. Profile (Jun) -->",
    "        " + jun,
    "        <!-- 5. Reviews -->",
    "        " + reviews,
    "        <!-- 6. Pricing & Campaigns Group -->",
    "        <div id=\"tarieven-acties\">",
    "            " + pricing,
    "            " + autumn,
    "            " + campaigns,
    "            " + cadeaubon,
    "        </div>",
    "        <!-- 7. Booking -->",
    "        " + booking,
    "        <!-- 8. Info & FAQ -->",
    "        " + info,
    "        " + faq,
    "        <!-- 9. Workshop & Updates -->",
    "        " + workshop,
    "        " + updates,
    "        " + map_sec,
    "    "
])

# Reassemble full HTML
new_html = pre_main + new_main + post_main

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("HTML rewritten successfully.")
