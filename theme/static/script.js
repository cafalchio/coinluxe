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

function checkValue(e) {
  // Check stripe max value and message user
  const maxValue = 999999.99
  const minValue = 0.04
  let total = 0;
  const values = document.querySelectorAll(".cvalue");

  values.forEach(valueElement => {
      total += parseFloat(valueElement.textContent);
  });
  const errorMessage = document.getElementById("errorMessage");
  if (total > maxValue) {
      e.preventDefault()
      errorMessage.textContent = "Value too high to be processed here. Please contact us at webcoinluxe@gmail.com";
      return false; 
  } else if (total < minValue) {
    e.preventDefault()
    errorMessage.textContent = "Value too low to be paid, please add more cryptos to your bag.";
    return false; 
  } else {
      errorMessage.textContent = "";
      return true; 
  }
}