(function () {
    var wrapper = document.getElementById('wrapper');
    var toggle = document.querySelector('.menu-toggle');

    if (!wrapper || !toggle) return;

    toggle.addEventListener('click', function () {
        wrapper.classList.toggle('sidebar-active');
    });

    wrapper.addEventListener('click', function (e) {
        if (wrapper.classList.contains('sidebar-active') && e.target === wrapper) {
            wrapper.classList.remove('sidebar-active');
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') wrapper.classList.remove('sidebar-active');
    });

    document.querySelectorAll('.submenu-toggle').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            btn.closest('li').classList.toggle('expanded');
        });
    });
})();
