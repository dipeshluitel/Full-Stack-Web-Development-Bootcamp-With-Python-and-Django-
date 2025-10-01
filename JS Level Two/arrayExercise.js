var student = ["Ram", "Shyam", "Sita"];
go = true;
while (go == true) {
  var choice = prompt(
    "What do you want to do: add,remove,display,quit"
  ).toLowerCase();
  if (choice == "add") {
    student.push(prompt("Enter the student full name"));
  } else if (choice == "remove") {
    var reName = prompt("Enter the student full name");
    var index = student.indexOf(reName);
    student.splice(index, 1);
  } else if (choice == "display") {
    for (nam of student) {
      console.log(nam);
    }
  } else {
    go = false;
  }
}
