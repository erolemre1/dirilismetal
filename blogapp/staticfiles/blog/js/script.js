import Swiper from "./swiper-bundle.min.js";

const initDate = () => {
  const date = new Date();
  const day = date.getDate();
  const year = date.getFullYear();
  const month = date.toLocaleString("tr-Tr", { month: "long" });
  const newDate =
    "Fiyatlar " +
    day +
    " " +
    month +
    " " +
    year +
    " tarihi itibariyle geçerlidir.";
  document.getElementById("date").innerHTML = newDate;
};

initDate();

var swiper = new Swiper(".mySwiper", {
  effect: "cube",
  grabCursor: true,
  loop: true,
  speed: 1500,
  cubeEffect: {
    shadow: true,
    slideShadows: true,
    shadowOffset: 20,
    shadowScale: 0.94,
  },
  pagination: {
    el: ".swiper-pagination",
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});


setInterval(function () {
  document.querySelector(".swiper-button-next").click();
}, 3000);
