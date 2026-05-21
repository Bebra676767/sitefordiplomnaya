// Обработка форм с анимацией спиннера
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('.btn-submit');
            if (submitBtn) {
                const spinner = submitBtn.querySelector('.spinner-border');
                submitBtn.disabled = true;
                if (spinner) {
                    spinner.classList.remove('d-none');
                }
            }
        });
    });
    
    // Инициализация карусели с авто-переключением каждые 3 секунды
    const carousel = document.getElementById('mainCarousel');
    if (carousel) {
        const bsCarousel = new bootstrap.Carousel(carousel, {
            interval: 3000,
            wrap: true,
            touch: true
        });
        
        // Пауза при наведении
        carousel.addEventListener('mouseenter', function() {
            bsCarousel.pause();
        });
        
        carousel.addEventListener('mouseleave', function() {
            bsCarousel.cycle();
        });
    }
    
    // Анимация появления элементов при скролле
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.hover-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        observer.observe(card);
    });
    
    // Маска для телефона
    const phoneInput = document.querySelector('input[name="phone"]');
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = this.value.replace(/\D/g, '');
            if (value.length > 0) {
                value = '8(' + value.substring(1, 4) + ')' + value.substring(4, 7) + '-' + value.substring(7, 9) + '-' + value.substring(9, 11);
                this.value = value.substring(0, 18);
            }
        });
    }
});