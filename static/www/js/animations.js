if (Cookies.get('visited')) {
    console.log('Odwiedzono')
}
else {
    animated_div = document.getElementById('hero-text');
    classlist = animated_div.classList.add('animate__animated');
    classlist = animated_div.classList.add('animate__fadeInLeft');
}
let wavingHandShakeAnimation = anime({
    targets: '#waving-hand-icon',
    rotate: 25,
    translateY: -20,
    autoplay: false,
    direction: 'alternate',
    duration: 1000,
    loop: true,
    easing: 'easeInOutSine',
});

let wavingHandInAnimation = anime({
    targets: '#waving-hand-icon',
    keyframes: [
        {translateY: [-70, 0], opacity: [0, 1], duration: 1500},
    ],
    complete: function () {
        wavingHandShakeAnimation.play();
    },
});
wavingHandInAnimation.play();

Cookies.set('visited', true)