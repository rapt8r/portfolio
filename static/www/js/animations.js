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
    rotate: 15,
    autoplay: false,
    direction: 'alternate',
    loop: true,
    easing: 'easeInOutSine',
});

let wavingHandInAnimation = anime({
    targets: '#waving-hand-icon',
    keyframes: [
        {translateY: [-50, 0], opacity: [0, 1], duration: 1500},
    ],
    complete: function () {
        wavingHandShakeAnimation.play();
    },
});
wavingHandInAnimation.play();
let confetti = new Confetti('btn-download-cv');

// Edit given parameters
confetti.setCount(75);
confetti.setSize(1);
confetti.setPower(10);
confetti.setFade(true);
confetti.destroyTarget(false);

Cookies.set('visited', true)