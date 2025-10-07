var player1 = prompt("Enter your Name, You're Blue ");
var player1Color = "rgb(0,0,225)";
var player2 = prompt("Enter your Name, You're Red ");
var player2Color = "rgb(225,0,0)";

var game_on = true;
var table = $("table tr");

function reportWin(rowNum, colNum) {
  console.log("You won starting at this row,col");
  console.log(rowNum);
  console.log(colNum);
}

function changeColor(rowIndex, colIndex, color) {
  return table
    .eq(rowIndex)
    .find("td")
    .eq(colIndex)
    .find("button")
    .css("background-color", color);
}
function returnColor(rowIndex, colIndex) {
  return table
    .eq(rowIndex)
    .find("td")
    .eq(colIndex)
    .find("button")
    .css("background-color");
}

function checkBottom(colIndex) {
  var colorReport = returnColor(5, colIndex);
  for (var row = 5; row > -1; row--) {
    colorReport = returnColor(row, colIndex);
    if (colorReport === "rgb(240, 240, 218)") {
      return row;
    }
  }
}

function colorMatchCheck(one, two, three, four) {
  return (
    one === two &&
    one === three &&
    one === four &&
    one !== "rgb(240, 240, 218)" &&
    one !== undefined
  );
}
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      if (
        colorMatchCheck(
          returnColor(row, col),
          returnColor(row, col + 1),
          returnColor(row, col + 2),
          returnColor(row, col + 3)
        )
      ) {
        console.log("Horizontal Win!");
        reportWin(row, col);
        return true;
      } else {
        continue;
      }
    }
  }
}
function verticalWin() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 4; row++) {
      if (
        colorMatchCheck(
          returnColor(row, col),
          returnColor(row + 1, col),
          returnColor(row + 2, col),
          returnColor(row + 3, col)
        )
      ) {
        console.log("Vertical Win!");
        reportWin(row, col);
        return true;
      } else {
        continue;
      }
    }
  }
}
