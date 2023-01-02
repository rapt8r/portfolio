// let test = anime({
//     targets: hero_picture,
//     translateY: function() {
//       return anime.random(10, 20);
//     },
//     duration: function() {
//       return anime.random(1000, 2000);
//     },
//     rotate: function() {
//       return anime.random(-20, 20);
//     },
//     direction: 'alternate',
//     loop: true,
//     easing: 'easeInOutSine',
// })

function randomNameShake() {
    anime({
        targets: document.getElementById('hero-name'),
        translateX: function () {
            return anime.random(-1, 1);
        },
        translateY: function () {
            return anime.random(-1, 1);
        },
        rotate: function () {
            return anime.random(-0.5, 0.5);
        },
        easing: 'easeInOutBack',
        duration: function () {
            return anime.random(200, 1250);
        },
        delay: function () {
            return anime.random(0, 50);
        },
        complete: randomNameShake
    });
}
function randomIconsShake() {
    anime({
        targets: document.getElementsByClassName('tech-icon'),
        translateX: function () {
            return anime.random(-25, 50);
        },
        translateY: function () {
            return anime.random(-25, 50);
        },
        rotate: function () {
            return anime.random(-25, 25);
        },
        easing: 'easeInOutBack',
        duration: function () {
            return anime.random(1000, 1250);
        },
        delay: function () {
            return anime.random(0, 1500);
        },
        complete: randomIconsShake
    });
}
randomNameShake();
randomIconsShake();
