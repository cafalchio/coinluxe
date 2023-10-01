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

function validateInput() {
  const inputField = document.getElementById("validationInput");
  const inputValue = inputField.value.trim(); 
  if (inputValue === "") {
      alert("Please add your address.");
      return false;
  }
}

function checkValue(e) {
  // Check stripe max value and message user
  const maxValue = 999999.99
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
  } else {
      errorMessage.textContent = "";
      return true; 
  }
}