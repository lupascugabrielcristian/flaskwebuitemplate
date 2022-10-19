// Code to keep the app from closing after a few seconds
// Ref: https://github.com/ClimenteA/flaskwebgui
document.addEventListener('DOMContentLoaded', function () {

  function keep_alive_server() {
    fetch("/keeponline", {
      method: 'GET',
      cache: 'no-cache'
    })
      .then(res => { })
      .catch(err => { })
  }

  try {
    setInterval(keep_alive_server, 3 * 1000)()
  } catch (error) {
    // doesn't matter handled by middleware
  }

});


function goToSomePage() {
	window.location = "/some_page?unu=Cristi&doi=Eu";
}

function goToMain() {
	window.location = "/";
}
