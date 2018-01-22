let button = document.createElement("button");
button.id = "btn";
button.innerHTML = 0;
document.body.appendChild(button);
button.onclick = function() {
    button.innerHTML = 1 + button.innerHTML++;
}

//Don't forget to connect HTML and CSS sheets