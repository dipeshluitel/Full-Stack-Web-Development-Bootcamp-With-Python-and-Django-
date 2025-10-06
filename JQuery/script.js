$("h1").click(function () {
  alert("There was a click");
  $(this).text("I was clicked");
});

$("p").click(function () {
  alert("There was a click on paragraph");
  $(this).text("I was clicked");
});

//also for double click - dblclick()

//KEYPRESS

$("input")
  .eq(0)
  .keypress(function () {
    $("h1").text("key is pressed inside input box");
  });

// usage of event (which)
$("input")
  .eq(0)
  .keypress(function (event) {
    if (event.which === 13) {
      $("h1").text("Enter key is pressed inside input box");
    }
  });

// on() (like addEventListener)
$("button").mouseenter(function () {
  $("h1").text("Mouse pointer has entered button field");
});
$("button").mouseout(function () {
  $("h1").text("Mouse pointer has left button field");
});

//Animation Available in JQuery
$("button").on("click", function () {
  $("body").fadeOut(3000); //slideUp
});
