import os
import re

german_html = """<section id="booking" style="background: var(--bg-alt); padding: 5rem 5%;">
            <div class="container text-center">
                <h2 class="section-title">Termin buchen</h2>
                
                <!-- Main Action Card -->
                <div class="calendly-external-wrapper" style="max-width: 650px; margin: 0 auto 2rem; background: white; border-radius: 12px; padding: 2.5rem 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); text-align: center;">
                    <p style="font-size: 1.1rem; color: #444; margin-bottom: 2rem; line-height: 1.6;">Sie werden zu unserem sicheren Buchungssystem (Calendly) weitergeleitet. Dort können Sie ganz einfach Ihr gewünschtes Datum und die Uhrzeit auswählen.</p>
                    
                    <div style="background-color: #fff9e6; border: 1px dashed #ffca28; padding: 1.5rem; border-radius: 8px; margin-bottom: 2.5rem; text-align: left;">
                        <p style="margin-top: 0; margin-bottom: 0.8rem; font-weight: 600; color: #d89b00; font-size: 1.05rem;">【 Bevor Sie zur Buchungsseite gehen 】</p>
                        <p style="color: #666; font-size: 0.95rem; margin-bottom: 1.2rem;">Fügen Sie diese Seite Ihrem Startbildschirm hinzu, um beim nächsten Mal mit nur einem Tippen zurückzukehren!</p>
                        <div style="text-align: center;">
                            <a href="#" class="inline-fav-btn" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; background-color: white; color: #d89b00; border: 2px solid #ffca28; padding: 0.8rem 1.5rem; font-size: 1rem; font-weight: 600; border-radius: 50px; text-decoration: none; transition: all 0.2s; box-shadow: 0 4px 10px rgba(0,0,0,0.05);" onmouseover="this.style.backgroundColor='#fff9e6'" onmouseout="this.style.backgroundColor='white'">
                                <span style="font-size: 1.2rem;">⭐</span> Diese Seite speichern
                            </a>
                        </div>
                    </div>
                    
                    <a href="https://calendly.com/shiatsu-massage-iyashi" target="_blank" rel="noopener noreferrer" style="display: inline-block; background-color: #2a2a2a; color: white; padding: 1.2rem 2.5rem; font-size: 1.15rem; font-weight: 600; border-radius: 50px; text-decoration: none; box-shadow: 0 4px 15px rgba(0,0,0, 0.2); transition: all 0.3s ease; width: 100%; max-width: 400px;" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 8px 25px rgba(0,0,0, 0.3)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(0,0,0, 0.2)';">
                        📅 Zur Buchungsseite
                    </a>
                </div>

                <!-- Important Alerts -->
                <div style="max-width: 650px; margin: 0 auto 2rem; background-color: #fcfcfc; border-left: 4px solid #ffca28; padding: 1.5rem; text-align: left; border-radius: 0 8px 8px 0; font-size: 0.95rem; box-shadow: 0 2px 10px rgba(0,0,0,0.03);">
                    <h4 style="color: #d89b00; margin-top: 0; margin-bottom: 1rem; font-size: 1.1rem;">Wichtige Informationen zu Ihrer Buchung</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; color: #555; line-height: 1.6;">
                        <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 10px;"><span style="font-size: 1.1rem; flex-shrink: 0;">💳</span> <span><strong>Die Zahlung erfolgt nach der Behandlung in der Praxis.</strong></span></li>
                        <li style="margin-bottom: 1.5rem; display: flex; align-items: flex-start; gap: 10px;"><span style="font-size: 1.1rem; flex-shrink: 0;">🕒</span> <span>Buchungen sind bis zu 2 Stunden vor dem Termin möglich.</span></li>
                        
                        <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 10px;"><span style="font-size: 1.1rem; flex-shrink: 0;">✉️</span> <span><strong>Bestätigungs-E-Mail:</strong> Nach der Buchung erhalten Sie eine E-Mail von Calendly. <strong>Bitte prüfen Sie auch Ihren Spam-Ordner.</strong> (Manchmal denken Kunden fälschlicherweise, die Buchung sei fehlgeschlagen, weil die E-Mail im Spam-Ordner gelandet ist).</span></li>
                        <li style="margin-bottom: 1rem; display: flex; align-items: flex-start; gap: 10px;"><span style="font-size: 1.1rem; flex-shrink: 0;">🔄</span> <span><strong>Ändern oder Stornieren:</strong> Nutzen Sie dafür immer den Link in der Bestätigungs-E-Mail (nicht auf die E-Mail antworten). Wichtig: Das Löschen des Termins aus Ihrem <strong>eigenen</strong> (Google-)Kalender storniert die Buchung <em>nicht</em> in unserem System.</span></li>
                        <li style="display: flex; align-items: flex-start; gap: 10px;"><span style="font-size: 1.1rem; flex-shrink: 0;">⚠️</span> <span><strong>Stornierungsbedingungen:</strong> Bis zu 2 Tage vor dem Termin ist die Stornierung kostenlos. Bei Stornierungen am Vortag oder am Tag der Behandlung gelten unsere Stornierungsbedingungen am Ende dieser Seite.</span></li>
                    </ul>
                </div>

                <!-- Support -->
                <div style="max-width: 650px; margin: 0 auto;">
                    <div style="background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid rgba(0,0,0,0.08); margin-bottom: 1rem; text-align: left; display: flex; align-items: center; gap: 1rem; box-shadow: 0 2px 10px rgba(0,0,0,0.02);">
                        <span style="font-size: 2rem;">💬</span>
                        <p style="margin: 0; color: var(--text-dark); font-size: 0.95rem; line-height: 1.5;">Probleme bei der Buchung? Senden Sie uns eine Nachricht über <a href="https://wa.me/31684332141" target="_blank" style="font-weight: 600; text-decoration: underline; color: #1EAE53;">WhatsApp</a>.<br><span style="color: #888; font-size: 0.85rem;">(Wir nehmen keine telefonischen Buchungen entgegen).</span></p>
                    </div>
                </div>
            </div>
        </section>"""

pattern = r"<section id=\"booking\".*?</section>"

german_files = ["de/index.html"] + [f"de/massage-{c}.html" for c in ["gronau", "ahaus", "ochtrup", "bad-bentheim", "vreden", "muenster"]]

for filepath in german_files:
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()
        
        content = re.sub(pattern, german_html, content, flags=re.DOTALL)
        
        # Also fix footer links ONLY in de/index.html
        if filepath == "de/index.html":
            dutch_cities = ["hengelo", "almelo", "oldenzaal", "haaksbergen", "borne", "losser"]
            for c in dutch_cities:
                content = content.replace(f'href="massage-{c}.html"', f'href="../massage-{c}.html"')
        
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated {filepath}")
