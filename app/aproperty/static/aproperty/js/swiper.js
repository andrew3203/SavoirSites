var swiper = new Swiper(".mySwiper", {
    slidesPerView: "auto",
    centeredSlides: true,
    spaceBetween: 15,
    loop: true,
    freeMode: false,
    speed: 6000,
    freeModeMomentum: false,
    autoplay: {
        delay: 10,
        disableOnInteraction: true,
    },
});