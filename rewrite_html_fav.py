import os

# 1. Update CSS
css_path = "css/style.css"
if os.path.exists(css_path):
    with open(css_path, "a") as f:
        f.write("""

/* Floating Favorite Button */
.fav-btn {
    position: fixed;
    bottom: 100px;
    right: 30px;
    background-color: #fff;
    color: #ccc;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 28px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    z-index: 1000;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 2px solid #f0f0f0;
    text-decoration: none;
}
.fav-btn:hover {
    transform: scale(1.05);
}
.fav-btn.active {
    color: #ffca28;
    border-color: #ffca28;
}

/* Toast Notification */
.toast-notification {
    position: fixed;
    bottom: -100px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0,0,0,0.85);
    color: white;
    padding: 12px 24px;
    border-radius: 30px;
    font-size: 14px;
    z-index: 1001;
    transition: bottom 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    pointer-events: none;
    text-align: center;
    width: 90%;
    max-width: 400px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    line-height: 1.5;
}
.toast-notification.show {
    bottom: 40px;
}
""")

# 2. Update JS
js_path = "js/script.js"
if os.path.exists(js_path):
    with open(js_path, "a") as f:
        f.write("""

// Favorite / Add to Homescreen Logic
document.addEventListener("DOMContentLoaded", () => {
    const favBtn = document.getElementById("floating-fav-btn");
    if (!favBtn) return;
    
    const isSaved = localStorage.getItem("iyashi_favorite");
    if (isSaved) {
        favBtn.classList.add("active");
    }
    
    favBtn.addEventListener("click", (e) => {
        e.preventDefault();
        const wasActive = favBtn.classList.contains("active");
        if (!wasActive) {
            favBtn.classList.add("active");
            localStorage.setItem("iyashi_favorite", "true");
        }
        showToast();
    });
});

function showToast() {
    let toast = document.getElementById("fav-toast");
    if (!toast) {
        toast = document.createElement("div");
        toast.id = "fav-toast";
        toast.className = "toast-notification";
        document.body.appendChild(toast);
    }
    
    const userAgent = navigator.userAgent || navigator.vendor || window.opera;
    const isGerman = window.location.pathname.includes("/de/");
    let message = "";
    let title = isGerman ? "Gespeichert!" : "Bewaard!";
    
    if (/android/i.test(userAgent)) {
        message = isGerman ? 
            "Tippen Sie auf das Menü [⋮] und dann auf<br><b>Zum Startbildschirm hinzufügen</b>!" : 
            "Tik op het menu [⋮] en kies<br><b>Toevoegen aan startscherm</b>!";
    } else if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
        message = isGerman ? 
            "Tippen Sie unten auf Teilen [↑] und dann auf<br><b>Zum Startbildschirm hinzufügen</b>!" : 
            "Tik op delen [↑] en kies<br><b>Zet op beginscherm</b>!";
    } else {
        message = isGerman ? 
            "Drücken Sie <b>Ctrl+D</b> (Mac: Cmd+D),<br>um diese Seite zu speichern!" :
            "Toets <b>Ctrl+D</b> (Mac: Cmd+D) in<br>om deze pagina te bewaren!";
    }
    
    toast.innerHTML = `⭐ <b>${title}</b><br>${message}`;
    toast.classList.add("show");
    
    setTimeout(() => {
        toast.classList.remove("show");
    }, 4500);
}
""")

# 3. Update HTML files
dutch_files = ["index.html"] + [f"massage-{c}.html" for c in ["hengelo", "almelo", "oldenzaal", "haaksbergen", "borne", "losser"]]
german_files = ["de/index.html"] + [f"de/massage-{c}.html" for c in ["gronau", "ahaus", "ochtrup", "bad-bentheim", "vreden", "muenster"]]

dutch_booking_target = "Kies hieronder de gewenste datum en tijd voor uw behandeling. Vul vervolgens uw naam, e-mailadres en telefoonnummer in om de reservering eenvoudig te voltooien.</p>"
dutch_booking_injection = """
                <div style="background-color: #fff9e6; border-left: 4px solid #ffca28; padding: 1rem; margin: 1.5rem 0; text-align: left; border-radius: 0 8px 8px 0; font-size: 0.95rem;">
                    <p style="margin-bottom: 0.5rem; color: #555; line-height: 1.5;"><span style="font-size: 1.2rem; margin-right: 5px;">✉️</span> Na het boeken ontvangt u een bevestigingsmail van Calendly (controleer ook uw spamfolder). Wijzigen of annuleren kan eenvoudig via de link in deze e-mail. (Niet beantwoorden)</p>
                    <p style="margin-bottom: 0; color: #d89b00; font-weight: 500;"><strong>[⭐ Bewaar deze pagina]</strong> Voeg deze pagina toe aan uw startscherm, zodat u de volgende keer met 1-tap kunt openen!</p>
                </div>"""

german_booking_target = "Wählen Sie unten Ihr gewünschtes Datum und Ihre bevorzugte Zeit für die Behandlung aus. Tragen Sie dann Ihren Namen, Ihre E-Mail-Adresse und Telefonnummer ein, um die Reservierung einfach abzuschließen.</p>"
german_booking_injection = """
                <div style="background-color: #fff9e6; border-left: 4px solid #ffca28; padding: 1rem; margin: 1.5rem 0; text-align: left; border-radius: 0 8px 8px 0; font-size: 0.95rem;">
                    <p style="margin-bottom: 0.5rem; color: #555; line-height: 1.5;"><span style="font-size: 1.2rem; margin-right: 5px;">✉️</span> Nach der Buchung erhalten Sie eine Bestätigungs-E-Mail von Calendly (bitte überprüfen Sie auch Ihren Spam-Ordner). Änderungen oder Stornierungen können Sie ganz einfach über den Link in dieser E-Mail vornehmen. (Bitte nicht antworten.)</p>
                    <p style="margin-bottom: 0; color: #d89b00; font-weight: 500;"><strong>[⭐ Seite speichern]</strong> Fügen Sie diese Seite zu Ihrem Startbildschirm hinzu, damit Sie sie beim nächsten Mal mit nur 1-Tap öffnen können!</p>
                </div>"""

floating_btn = '\n    <a href="#" id="floating-fav-btn" class="fav-btn" title="Save this page">★</a>\n'

def process_file(filepath, target, injection):
    if not os.path.exists(filepath): return
    with open(filepath, "r") as f:
        content = f.read()
    
    if "fav-btn" not in content:
        # Inject booking notice
        content = content.replace(target, target + injection)
        
        # Inject floating button before WhatsApp button or before closing body
        if "wa-float" in content:
            content = content.replace("<a href=\"https://wa.me", floating_btn + "    <a href=\"https://wa.me")
        else:
            content = content.replace("</body>", floating_btn + "</body>")
            
        with open(filepath, "w") as f:
            f.write(content)

for f in dutch_files:
    process_file(f, dutch_booking_target, dutch_booking_injection)

for f in german_files:
    process_file(f, german_booking_target, german_booking_injection)

