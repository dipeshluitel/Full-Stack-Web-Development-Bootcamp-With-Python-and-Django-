var fname = prompt("Enter your First Name: ");
var lname = prompt("Enter your Last Name: ");
var age = Number(prompt("Enter your age: "));
var height = Number(prompt("Enter your height in CM: "));
var pname = prompt("Enter your pet name: ");

if (fname[0] == lname[0]) {
  if (20 < age < 30) {
    if (height >= 170) {
      if (pname[pname.length - 1]) {
        console.log("The Passkey is 'SECRET@)@%2025'");
      }
    }
  }
}
