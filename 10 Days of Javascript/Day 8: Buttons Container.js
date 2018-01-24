for(let i = 1; i <= 9; i++) {  
    let button = document.createElement("button");
    button.id = "btn"+i;
    button.innerHTML = i;
    
    document.getElementById("btns").appendChild(button);
}

let btnNum = []

let change = function () {
    for(let j = 1; j <= 9; j++){
        if (j == 5) continue;
        btnNum[j] = +(document.getElementById("btn"+j).innerHTML);
    }
    
    document.getElementById("btn1").innerHTML = btnNum[4];
    document.getElementById("btn2").innerHTML = btnNum[1];
    document.getElementById("btn3").innerHTML = btnNum[2];
    document.getElementById("btn4").innerHTML = btnNum[7];
    document.getElementById("btn5").innerHTML = 5;
    document.getElementById("btn6").innerHTML = btnNum[3];
    document.getElementById("btn7").innerHTML = btnNum[8];
    document.getElementById("btn8").innerHTML = btnNum[9];
    document.getElementById("btn9").innerHTML = btnNum[6];
}

document.getElementById("btn5").addEventListener('click', change);