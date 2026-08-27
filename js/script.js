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

    // Header scroll effect
    const header = document.querySelector('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.05)';
        }
    });

    // Load pricing from Decap CMS JSON data (if running on a server that can fetch them)
    // For local dev without a server, fetch might fail due to CORS, but works in production (Netlify/Vercel)
    async function loadPricing() {
        try {
            // Note: In a static site, you'd typically have a build step (like 11ty or Hugo) 
            // that compiles these JSON files into the HTML. 
            // Alternatively, we can try to fetch them dynamically if we expose a list of files,
            // but for a pure HTML setup without a backend, we rely on the static HTML fallback 
            // written in index.html for simplicity, unless we fetch specific known files.
            
            const prices = ['30-min.json', '50-min.json']; // Ideally generated
            const grid = document.getElementById('pricing-grid');
            
            // We only do this if we want fully dynamic client-side rendering
            // For now, the fallback HTML is used.
        } catch (error) {
            console.log("Using fallback pricing data.");
        }
    }
    
    // loadPricing();
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
