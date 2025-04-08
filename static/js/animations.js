// Navbar Scroll Effect
document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('.navbar');
    const backToTop = document.querySelector('.back-to-top');

    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
            backToTop?.classList.add('visible');
        } else {
            navbar.classList.remove('scrolled');
            backToTop?.classList.remove('visible');
        }
    });

    // Back to top functionality
    backToTop?.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Fade in elements on scroll
    const fadeElements = document.querySelectorAll('.fade-in');
    const observerOptions = {
        root: null,
        threshold: 0.1,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    fadeElements.forEach(element => observer.observe(element));

    // Page transition
    document.body.classList.add('page-enter');
    requestAnimationFrame(() => {
        document.body.classList.add('page-enter-active');
    });

    // Add loading spinner to images
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        const wrapper = document.createElement('div');
        wrapper.className = 'position-relative';
        const spinner = document.createElement('div');
        spinner.className = 'loading-spinner position-absolute top-50 start-50 translate-middle';
        
        img.parentNode.insertBefore(wrapper, img);
        wrapper.appendChild(spinner);
        wrapper.appendChild(img);

        img.addEventListener('load', () => {
            spinner.remove();
        });
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Button click effect
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const circle = document.createElement('div');
            circle.style.left = x + 'px';
            circle.style.top = y + 'px';
            circle.className = 'ripple';
            
            this.appendChild(circle);
            setTimeout(() => circle.remove(), 1000);
        });
    });
});
