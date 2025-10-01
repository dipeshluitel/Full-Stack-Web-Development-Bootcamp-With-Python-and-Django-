function sleepIn(weekday, vacation) {
  if (weekday == false || vacation == true) {
    return true;
  } else {
    return false;
  }
}

function monkeyTrouble(aSmile, bSmile) {
  if (aSmile == bSmile) {
    return true;
  } else {
    return false;
  }
}

function stringTimes(str, n) {
  var word = "";
  while (n != 0) {
    word += str;
    n -= 1;
  }
  return word;
}

function caughtSpeeding(speed, is_birthday) {
  var ticket = null;
  if (is_birthday == true) {
    ticket = 0;
  } else {
    if (speed < 60) {
      ticket = 0;
    } else if (60 <= speed <= 80) {
      ticket = 1;
    } else {
      ticket = 2;
    }
  }
  return ticket;
}

function makeBricks(small, big, goal) {
  return goal % 5 >= 0 && (goal % 5) - small <= 0 && small + 5 * big >= goal;
}
