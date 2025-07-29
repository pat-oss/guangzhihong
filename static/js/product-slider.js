document.addEventListener('DOMContentLoaded', () => {
    const slides  = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    if (!slides.length) return;

    let cur = 0;

    function show(index) {
        slides.forEach(s => s.classList.remove('active'));
        cur = (index + slides.length) % slides.length;
        slides[cur].classList.add('active');
    }

    prevBtn.addEventListener('click', () => show(cur - 1));
    nextBtn.addEventListener('click', () => show(cur + 1));

    // 键盘 ← → 也可翻页
    document.addEventListener('keydown', e => {
        if (e.key === 'ArrowLeft')  show(cur - 1);
        if (e.key === 'ArrowRight') show(cur + 1);
    });
});