$(document).ready(function(){
  $("#mySearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".card-body").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});