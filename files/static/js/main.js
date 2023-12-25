function slider() {
    const images = document.querySelectorAll('.slider .slider_line img');
    const sliderLine = document.querySelector('.slider_line');
    let count = 0;
    let width;


    function init() {
        console.log('resize');
        width = document.querySelector('.slider').offsetWidth;
        sliderLine.style.width = width * images.length + 'px';
        images.forEach(item => {
            item.style.width = width + 'px';
            item.style.height = 'auto';
        });
        rollSlider();

    }


    window.addEventListener('resize', init);
    init();

    document.querySelector('.slider_prev').addEventListener('click', function () {
        count--;
        if (count < 0) {
            count = images.length - 1;
        }
        rollSlider();
    });

    function rollSlider() {
        sliderLine.style.transform = 'translate(-' + count * width + 'px'
    }

    document.querySelector('.slider_next').addEventListener('click', function () {
        count++;
        if (count >= images.length) {
            count = 0;
        }
        rollSlider();
    });

    function rollSlider() {
        sliderLine.style.transform = 'translate(-' + count * width + 'px'
    }

};

slider();
