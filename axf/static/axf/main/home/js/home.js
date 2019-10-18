$(function () {
    initWheel();
    initMustBuy();
})
function  initWheel() {
    var mySwiper = new Swiper('#topSwiper',
        {
            loop:true,
            direction:'horizontal',
            speed:500,
            autoplay:3000,
            autoplayDisableOnInteraction: false,
            pagination: '.swiper-pagination',
            nextButton: '.swiper-button-next',
            prevButton: '.swiper-button-prev',
            control:true,

        })
}

function  initMustBuy() {
    var mySwiper1 = new Swiper('#swiperMenu',{
        slidesPerView:3,
        paginationClickable:true,
        spaceBetween:2,
        loop:false,
    })
}