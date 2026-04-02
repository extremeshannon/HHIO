(function () {
  var toggle = document.getElementById("nav-toggle");
  var nav = document.getElementById("site-nav");
  var header = document.querySelector(".site-header");
  var year = document.getElementById("year");

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  if (!toggle || !nav || !header) return;

  function setOpen(open) {
    nav.classList.toggle("nav-open", open);
    header.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
  }

  toggle.addEventListener("click", function () {
    setOpen(!nav.classList.contains("nav-open"));
  });

  nav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      if (window.matchMedia("(max-width: 768px)").matches) {
        setOpen(false);
      }
    });
  });

  window.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setOpen(false);
  });
})();
