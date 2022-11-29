//-------------  SCROLL A SECCIONES - TRANSICIÓN --------------//
$(document).ready(function () {
    // Add smooth scrolling to all links
    $("a").on('click', function (event) {

        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
            // Prevent default anchor click behavior
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function () {

                // Add hash (#) to URL when done scrolling (default click behavior)
                window.location.hash = hash;
            });
        } // End if
    });
});

//-------------  IMAGEN HEADER --------------//
let parallax = document.querySelector('.parallax');
let titulo = document.querySelector('.Home-banners-item-text');

function scrollParallax() {
    let scrollTop = document.documentElement.scrollTop;
    parallax.style.transform = 'translateY(' + scrollTop * -0.3 + 'px)';
    titulo.style.transform = 'translateY(' + scrollTop * -0.3 + 'px)';
}

window.addEventListener('scroll', scrollParallax);

//-------------  MENU ESTATICO --------------//
window.onscroll = function () { myFunctionSta() };

var Header = document.getElementById("myNavbar");

var sticky = Header.offsetTop;

function myFunctionSta() {
    if (window.pageYOffset > sticky) {
        Header.classList.add("sticky");
    } else {
        Header.classList.remove("sticky");
    }
}

//-------------  FUNCIÓN/PARTE --------------//
/* Toggle between adding and removing the "responsive" class to the navbar when the user clicks on the icon */
function openNav() {
    document.getElementById("myNavbar").style.width = "100%";
}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeNav() {
    document.getElementById("myNavbar").style.width = "0%";
}
//-------------  FUNCIÓN/PARTE --------------//
let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function carouselExampleIndicators2(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("card");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}


//-------------  FUNCIÓN/PARTE --------------//


//-------------  FUNCIÓN/PARTE --------------//