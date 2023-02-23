let mybutton = document.getElementById("myBtn");
let mybNavbar = document.getElementById("myNavbar");

window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.documentElement.scrollTop > 58) {
    mybutton.style.display = "block";
    if(window.innerWidth > 992){
      mybNavbar.classList.add("stickyNavbar");
    }
  } else {
    mybutton.style.display = "none";
    mybNavbar.classList.remove("stickyNavbar");
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
