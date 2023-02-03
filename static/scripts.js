    
  var changeColorButton = document.getElementById("change-color-button");
  changeColorButton.addEventListener("click", function() {
    var rooms = document.getElementsByClassName("patient");
    for (var i = 0; i < rooms.length; i++) {
        rooms[i].style.backgroundColor = "red";
      }
    }); 