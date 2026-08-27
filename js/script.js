document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80, // Adjust for fixed header
                    behavior: 'smooth'
                });
            }
        });
    });

    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navMenu = document.getElementById('navMenu');
    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });

        // Close mobile menu when link is clicked
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });
    }
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.05)';
        }
    });

    // Calendly Widget Initialization fallback check
    function initCalendly() {
        const embedContainer = document.getElementById('calendly-embed');
        if (embedContainer && window.Calendly) {
            window.Calendly.initInlineWidget({
                url: 'https://calendly.com/shiatsu-massage-iyashi',
                parentElement: embedContainer
            });
        }
    }
    
    // Check if Calendly is already loaded or wait for it
    if (window.Calendly) {
        initCalendly();
    } else {
        window.addEventListener('load', initCalendly);
    }
});

// URL Copy function
function copyShareUrl() {
    const url = window.location.href;
    navigator.clipboard.writeText(url).then(() => {
        alert("Link gekopieerd naar klembord! (URLをコピーしました)");
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

// Web Share API function
function nativeShare() {
    if (navigator.share) {
        navigator.share({
            title: 'Shiatsu Massage Iyashi in Enschede',
            text: 'Traditionele Japanse Shiatsu-massage in Enschede.',
            url: window.location.href,
        }).catch(console.error);
    } else {
        copyShareUrl();
    }
}
