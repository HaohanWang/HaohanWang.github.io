// Minimal replacement for the template's jQuery plugins: mobile nav + header shadow.
(function () {
  var nav = document.getElementById('nav-menu-container');
  if (nav) {
    var mobileNav = nav.cloneNode(true);
    mobileNav.id = 'mobile-nav';
    mobileNav.querySelector('ul').className = '';
    document.body.appendChild(mobileNav);

    var toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.id = 'mobile-nav-toggle';
    toggle.setAttribute('aria-label', 'Toggle navigation');
    toggle.innerHTML = '<i class="lnr lnr-menu"></i>';
    document.body.insertBefore(toggle, document.body.firstChild);

    var overlay = document.createElement('div');
    overlay.id = 'mobile-body-overly';
    document.body.appendChild(overlay);

    var setOpen = function (open) {
      document.body.classList.toggle('mobile-nav-active', open);
      toggle.querySelector('i').className = 'lnr ' + (open ? 'lnr-cross' : 'lnr-menu');
      overlay.style.display = open ? 'block' : 'none';
    };
    toggle.addEventListener('click', function () {
      setOpen(!document.body.classList.contains('mobile-nav-active'));
    });
    overlay.addEventListener('click', function () { setOpen(false); });
    mobileNav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setOpen(false);
    });
  }

  var header = document.getElementById('header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('header-scrolled', window.scrollY > 100);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
})();
