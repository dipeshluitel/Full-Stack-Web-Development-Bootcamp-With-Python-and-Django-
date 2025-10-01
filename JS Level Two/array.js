var countrires = [
  "Nepal",
  "India",
  "China",
  "Maldives",
  "Sirlankha",
  "Bhutan",
  "Pakistan",
];
var nepalstates = [
  ["Jhapa", " Illam", "Biratnagar"],
  ["Kathmandu", "Chitwan"],
  ["Pokhara", "Kaski", "Lumbini", "Rolpa"],
];

function saarc(name) {
  console.log(name + " is a SAARC country");
}
for (country of countrires) {
  console.log(country);
}
countrires.forEach(saarc);
