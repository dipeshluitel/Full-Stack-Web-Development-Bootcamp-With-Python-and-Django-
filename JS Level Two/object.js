var studentInfo = {
  name: "Dipesh",
  year: "2078",
  symbolno: "29777/078",
  speciality: ["pyhton", "Django"],
  Database: { openSource: ["MSSQL", "SQLite", "MySql"] },
};
for (k in studentInfo) {
  console.log(k);
  console.log(studentInfo[k]);
}
