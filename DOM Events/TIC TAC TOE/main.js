var square = document.querySelectorAll("td");
var btn = document.querySelector("#track");
var start = true;

function clear() {
  for (var i = 0; i < square.length; i++) {
    square[i].textContent = "";
  }
}

function changeMarker() {
  if (this.textContent === "") {
    this.textContent = "X";
  } else if (this.textContent === "X") {
    this.textContent = "O";
  } else {
    this.textContent = "";
  }
}

for (var i = 0; i < square.length; i++) {
  square[i].addEventListener("click", changeMarker);
}
btn.addEventListener("click", clear);
