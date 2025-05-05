// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Initialize AOS (Animate On Scroll) if available
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true
        });
    }

    // Add animation classes to elements when they come into view
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    const animateOnScroll = function() {
        animateElements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 50) {
                const animationClass = element.dataset.animation || 'fade-in-up';
                element.classList.add(animationClass);
            }
        });
    };
    
    if (animateElements.length > 0) {
        window.addEventListener('scroll', animateOnScroll);
        // Trigger once on page load
        animateOnScroll();
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            e.preventDefault();
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Quantity input controls for cart
    const quantityInputs = document.querySelectorAll('.quantity-input');
    
    quantityInputs.forEach(input => {
        const decrementBtn = input.parentElement.querySelector('.quantity-decrement');
        const incrementBtn = input.parentElement.querySelector('.quantity-increment');
        
        if (decrementBtn) {
            decrementBtn.addEventListener('click', function() {
                let value = parseInt(input.value);
                if (value > 1) {
                    input.value = value - 1;
                    // Trigger change event for any listeners
                    input.dispatchEvent(new Event('change'));
                }
            });
        }
        
        if (incrementBtn) {
            incrementBtn.addEventListener('click', function() {
                let value = parseInt(input.value);
                input.value = value + 1;
                // Trigger change event for any listeners
                input.dispatchEvent(new Event('change'));
            });
        }
    });

    // Reservation date validation
    const reservationDateInput = document.getElementById('id_date');
    if (reservationDateInput) {
        reservationDateInput.addEventListener('change', function() {
            const selectedDate = new Date(this.value);
            const today = new Date();
            today.setHours(0, 0, 0, 0);
            
            if (selectedDate < today) {
                alert('Будь ласка, виберіть дату починаючи з сьогоднішнього дня.');
                this.value = '';
            }
        });
    }

    // Image gallery lightbox (if any)
    const galleryImages = document.querySelectorAll('.gallery-image');
    
    galleryImages.forEach(image => {
        image.addEventListener('click', function() {
            const imageUrl = this.getAttribute('data-full-img') || this.src;
            const lightbox = document.createElement('div');
            lightbox.className = 'lightbox';
            lightbox.innerHTML = `
                <div class="lightbox-content">
                    <img src="${imageUrl}" alt="Lightbox Image">
                    <span class="lightbox-close">&times;</span>
                </div>
            `;
            
            document.body.appendChild(lightbox);
            document.body.style.overflow = 'hidden';
            
            lightbox.addEventListener('click', function(e) {
                if (e.target === lightbox || e.target.className === 'lightbox-close') {
                    document.body.removeChild(lightbox);
                    document.body.style.overflow = '';
                }
            });
        });
    });

    // Add to cart animation
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Prevent default if it's a link
            if (button.tagName === 'A') {
                e.preventDefault();
            }
            
            // Create a flying element
            const cartIcon = document.querySelector('.cart-icon');
            if (cartIcon) {
                const productCard = this.closest('.dish-card') || this.closest('.product-item');
                if (productCard) {
                    const productImage = productCard.querySelector('img');
                    if (productImage) {
                        const flyingImage = document.createElement('img');
                        flyingImage.src = productImage.src;
                        flyingImage.className = 'flying-image';
                        flyingImage.style.position = 'fixed';
                        
                        // Get positions
                        const imgRect = productImage.getBoundingClientRect();
                        const cartRect = cartIcon.getBoundingClientRect();
                        
                        // Set initial position
                        flyingImage.style.left = `${imgRect.left}px`;
                        flyingImage.style.top = `${imgRect.top}px`;
                        flyingImage.style.width = `${imgRect.width}px`;
                        flyingImage.style.height = `${imgRect.height}px`;
                        flyingImage.style.opacity = '0.8';
                        flyingImage.style.zIndex = '9999';
                        flyingImage.style.borderRadius = '50%';
                        flyingImage.style.transition = 'all 1s ease';
                        
                        document.body.appendChild(flyingImage);
                        
                        // Trigger animation after a small delay
                        setTimeout(() => {
                            flyingImage.style.left = `${cartRect.left}px`;
                            flyingImage.style.top = `${cartRect.top}px`;
                            flyingImage.style.width = '20px';
                            flyingImage.style.height = '20px';
                            flyingImage.style.opacity = '0';
                        }, 10);
                        
                        // Remove the element after animation completes
                        setTimeout(() => {
                            document.body.removeChild(flyingImage);
                            
                            // Animate cart icon
                            cartIcon.classList.add('cart-pulse');
                            setTimeout(() => {
                                cartIcon.classList.remove('cart-pulse');
                            }, 500);
                            
                            // If it's a real button (not for demo), submit the form or follow the link
                            if (!button.classList.contains('demo')) {
                                if (button.tagName === 'A') {
                                    window.location.href = button.href;
                                } else if (button.type === 'submit') {
                                    button.form.submit();
                                }
                            }
                        }, 1000);
                    }
                }
            }
        });
    });

    // Testimonial carousel/slider
    const testimonialContainer = document.querySelector('.testimonial-slider');
    if (testimonialContainer) {
        const testimonials = testimonialContainer.querySelectorAll('.testimonial-card');
        let currentIndex = 0;
        
        // Create navigation dots
        const dotsContainer = document.createElement('div');
        dotsContainer.className = 'slider-dots text-center mt-4';
        
        testimonials.forEach((_, index) => {
            const dot = document.createElement('span');
            dot.className = 'slider-dot';
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToSlide(index));
            dotsContainer.appendChild(dot);
        });
        
        testimonialContainer.parentNode.appendChild(dotsContainer);
        
        // Show only the current testimonial
        const showCurrentTestimonial = () => {
            testimonials.forEach((testimonial, index) => {
                testimonial.style.display = index === currentIndex ? 'block' : 'none';
            });
            
            // Update dots
            const dots = dotsContainer.querySelectorAll('.slider-dot');
            dots.forEach((dot, index) => {
                if (index === currentIndex) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        };
        
        // Go to specific slide
        const goToSlide = (index) => {
            currentIndex = index;
            showCurrentTestimonial();
        };
        
        // Next slide
        const nextSlide = () => {
            currentIndex = (currentIndex + 1) % testimonials.length;
            showCurrentTestimonial();
        };
        
        // Previous slide
        const prevSlide = () => {
            currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
            showCurrentTestimonial();
        };
        
        // Create next/prev buttons
        const nextButton = document.createElement('button');
        nextButton.className = 'slider-next';
        nextButton.innerHTML = '<i class="fas fa-chevron-right"></i>';
        nextButton.addEventListener('click', nextSlide);
        
        const prevButton = document.createElement('button');
        prevButton.className = 'slider-prev';
        prevButton.innerHTML = '<i class="fas fa-chevron-left"></i>';
        prevButton.addEventListener('click', prevSlide);
        
        testimonialContainer.appendChild(nextButton);
        testimonialContainer.appendChild(prevButton);
        
        // Initialize
        showCurrentTestimonial();
        
        // Auto-slide every 5 seconds
        setInterval(nextSlide, 5000);
    }

    // Add CSS for the lightbox and flying image animation
    const style = document.createElement('style');
    style.textContent = `
        .lightbox {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.9);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
        }
        
        .lightbox-content {
            position: relative;
            max-width: 90%;
            max-height: 90%;
        }
        
        .lightbox-content img {
            max-width: 100%;
            max-height: 90vh;
            border: 5px solid white;
            border-radius: 5px;
        }
        
        .lightbox-close {
            position: absolute;
            top: -40px;
            right: 0;
            font-size: 30px;
            color: white;
            cursor: pointer;
        }
        
        .cart-pulse {
            animation: pulse 0.5s ease;
        }
        
        .slider-dots {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        
        .slider-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #ccc;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .slider-dot.active {
            background-color: var(--primary-color);
            transform: scale(1.2);
        }
        
        .slider-next, .slider-prev {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background-color: white;
            border: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            z-index: 2;
            transition: all 0.3s ease;
        }
        
        .slider-next:hover, .slider-prev:hover {
            background-color: var(--primary-color);
            color: white;
        }
        
        .slider-next {
            right: -20px;
        }
        
        .slider-prev {
            left: -20px;
        }
    `;
    document.head.appendChild(style);
    
    // Back to top button
    const backToTopButton = document.querySelector('.back-to-top');
    if (backToTopButton) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                backToTopButton.classList.add('active');
            } else {
                backToTopButton.classList.remove('active');
            }
        });
        
        backToTopButton.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});
