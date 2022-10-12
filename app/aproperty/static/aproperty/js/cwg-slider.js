const slidesContainer = document.getElementById("slides-container");
const slide = document.querySelector(".cwg-slide");
const prevButton = document.getElementById("slide-arrow-prev");
const nextButton = document.getElementById("slide-arrow-next");

function moveRight () {
  const slideWidth = slide.clientWidth;
  
  if (slideWidth > 650) {
    slidesContainer.scrollLeft += slideWidth / 3
    if (slidesContainer.scrollLeft + 1 >= slide.clientWidth*2) {
      slidesContainer.scrollLeft -= (slide.clientWidth*2 - 1)
    }
  } else {
    slidesContainer.scrollLeft += slideWidth
    if (slidesContainer.scrollLeft + 1 >= slide.clientWidth*8) {
      slidesContainer.scrollLeft -= (slide.clientWidth*8 - 1)
    }
  }
}

function moveLeft () {
  const slideWidth = slide.clientWidth;
  
  if (slideWidth > 650) {
    slidesContainer.scrollLeft -= slideWidth / 3
    if (slidesContainer.scrollLeft - 1 <= 0) {
      slidesContainer.scrollLeft += (slide.clientWidth*2 + 1)
    }
  } else {
    slidesContainer.scrollLeft -= slideWidth
    if (slidesContainer.scrollLeft - 1 <= 0) {
      slidesContainer.scrollLeft += (slide.clientWidth*8 + 1)
    }
  }
}

let moving = setInterval(moveRight, 3000);

slidesContainer.addEventListener("scroll", () => {})

nextButton.addEventListener("click", () => {
  moveRight()
  clearInterval(moving);
});

prevButton.addEventListener("click", () => {
  moveLeft()
  clearInterval(moving);
});


function iteration() {
  const date = new Date()
  clock(date, "moscow", 0, 0);
  clock(date, "london", -3, 0);
  clock(date, "dubai", 1, 0);
  clock(date, "delhi", 2, 30);
  clock(date, "ankara", 0, 0);
  clock(date, "teheran", 1, 30);
  clock(date, "baku", 1, 0);
  clock(date, "bejing", 5, 0);
  clock(date, "er-riad", 0, 0);
}

function clock(date, id, hour_offset, minute_offset) {

  const minutes = date.getMinutes() + minute_offset;
  const hours = ((date.getHours() + 11 + hour_offset + ((minutes > 60) ? 1 : 0)) % 12 + 1);
  const seconds = date.getSeconds();

  const hour = hours * 30;
  const minute = (minutes % 60) * 6;
  const second = seconds * 6;

  if (document.querySelector(`#${id}-hour-sm`)) {
    document.querySelector(`#${id}-hour-sm`).style.transform = `rotate(${hour}deg)`
    document.querySelector(`#${id}-minute-sm`).style.transform = `rotate(${minute}deg)`
    document.querySelector(`#${id}-second-sm`).style.transform = `rotate(${second}deg)`
  }
  
  document.querySelector(`#${id}-hour`).style.transform = `rotate(${hour}deg)`
  document.querySelector(`#${id}-minute`).style.transform = `rotate(${minute}deg)`
  document.querySelector(`#${id}-second`).style.transform = `rotate(${second}deg)`
}

iteration();
setInterval(iteration, 1000);
