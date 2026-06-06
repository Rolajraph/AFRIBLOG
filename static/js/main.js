document.addEventListener('DOMContentLoaded', () => {
    // 1. Reading Progress Bar Logic
    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        const progressBar = document.getElementById("progress-bar");
        if (progressBar) progressBar.style.width = scrolled + "%";
    });

    // 2. Dark Mode Toggle Logic
    const themeToggleBtn = document.getElementById('theme-toggle');
    const body = document.body;

    if (themeToggleBtn) {
        // Check saved preference
        if (localStorage.getItem('theme') === 'dark') {
            body.classList.add('dark-mode');
            themeToggleBtn.innerHTML = '<span class="icon">☀️</span> Light Mode';
        }

        themeToggleBtn.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
                themeToggleBtn.innerHTML = '<span class="icon">☀️</span> Light Mode';
            } else {
                localStorage.setItem('theme', 'light');
                themeToggleBtn.innerHTML = '<span class="icon">🌙</span> Dark Mode';
            }
        });
    }

    // 3. Hamburger Menu Logic
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }
});

window.onscroll = function() {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    
    const progressBar = document.getElementById("progress-bar");
    if (progressBar) {
        progressBar.style.width = scrolled + "%";
    }
};