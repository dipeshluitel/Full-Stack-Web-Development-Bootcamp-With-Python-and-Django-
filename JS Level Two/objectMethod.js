var studentInfo = {
  name: "Dipesh",
  year: "2078",
  symbolno: "29777/078",
  speciality: ["pyhton", "Django"],
  Database: { openSource: ["MSSQL", "SQLite", "MySql"] },
  listData: function () {
    alert("Welcome " + this.name + " your Symbol number is " + this.symbolno);
  },
};

// In order to call method from object
//  object_name.function_name();
