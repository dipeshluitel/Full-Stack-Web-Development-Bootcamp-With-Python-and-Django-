var employee = {
  name: "Dipesh Luitel",
  job: "Developer",
  age: 21,

  //To print the total length of name
  nameLength: function () {
    console.log("The Length of the employee name is: " + this.name.length);
  },

  //TO display Information using this. functionality
  getInfo: function () {
    alert(
      "The name is " +
        this.name +
        " Job is " +
        this.job +
        " and age is " +
        this.age
    );
  },

  //To obtain the Last Name only
  getLastName: function () {
    var lastName = employee.name.split(" ");
    console.log(lastName[1]);
  },
};
