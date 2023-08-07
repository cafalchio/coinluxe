// Navbar buttom
const btn = document.querySelector(".mobile-menu-button");
const menu = document.querySelector(".mobile-menu");

btn.addEventListener("click", () => {
  menu.classList.toggle("hidden");
});

document.addEventListener("click", (event) => {
    const target = event.target;
    const isOutsideMenu = !menu.contains(target) && !btn.contains(target);
    if (isOutsideMenu) {
      menu.classList.add("hidden");
    }
});

