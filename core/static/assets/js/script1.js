// Fullscreen
(function () {
  var fullscreenButton = document.getElementById("maximize-screen");
  if (fullscreenButton) {
    var svgIcon = fullscreenButton.querySelector("svg use"); // Assuming the SVG use element is a child of fullscreenButton
    fullscreenButton.addEventListener("click", toggleFullScreen, false);
  }

  function toggleFullScreen() {
    if (!document.fullscreenElement && !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement) {
      // Entering fullscreen
      svgIcon.setAttribute("href", "../assets/svg/icon-sprite.svg#full-screen");
    } else {
      // Exiting fullscreen
      svgIcon.setAttribute("href", "../assets/svg/icon-sprite.svg#full-screen");
    }

    if (!document.fullscreenElement && !document.mozFullScreenElement && !document.webkitFullscreenElement && !document.msFullscreenElement) {
      var requestMethod = document.documentElement.requestFullscreen || document.documentElement.msRequestFullscreen || document.documentElement.mozRequestFullScreen || document.documentElement.webkitRequestFullscreen;
      if (requestMethod) {
        requestMethod.call(document.documentElement, Element.ALLOW_KEYBOARD_INPUT);
      }
    } else {
      var exitMethod = document.exitFullscreen || document.msExitFullscreen || document.mozCancelFullScreen || document.webkitExitFullscreen;
      if (exitMethod) {
        exitMethod.call(document);
      }
    }
  }
  // Footer year update
  var yearUpdate = document.querySelector(".year-update");
  if (yearUpdate) {
    yearUpdate.textContent = new Date().getFullYear();
  }
})();
