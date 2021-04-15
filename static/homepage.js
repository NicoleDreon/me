"use strict";
function showName(evt) {
  evt.preventDefault();
}

$("#login-form").on("click", showName);
