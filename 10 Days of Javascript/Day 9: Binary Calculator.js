document.getElementById("btn0").innerHTML = 0;
document.getElementById("btn1").innerHTML = 1;
document.getElementById("btnClr").innerHTML = "C";
document.getElementById("btnEql").innerHTML = "=";
document.getElementById("btnSum").innerHTML = "+";
document.getElementById("btnSub").innerHTML = "-";
document.getElementById("btnMul").innerHTML = "*";
document.getElementById("btnDiv").innerHTML = "/";


let operand1 = 0;
let operator = "";

function calcZero() {
    document.getElementById("res").innerHTML += "0";
}

function calcOne() {
    document.getElementById("res").innerHTML += "1";
}

function calcClr() {
    document.getElementById("res").innerHTML = "";
}

function calcSum() {
    operator = "+";
    operand1 = parseInt(document.getElementById("res").innerHTML, 2); //string to num base 2
    document.getElementById("res").innerHTML += "+"
}

function calcSub() {
    operator = "-";
    document.getElementById("res").innerHTML += "-"
}

function calcMul() {
    operator = "*";
    operand1 = parseInt(document.getElementById("res").innerHTML, 2); //string to num base 2
    document.getElementById("res").innerHTML += "*"
}

function calcDiv() {
    operator = "/";
    document.getElementById("res").innerHTML += "/"
}

function calcEql() {
    let total = 0;
    if (operator == "+") {
        let i= (document.getElementById("res").innerHTML).indexOf("+");
        let operand2 = parseInt((document.getElementById("res").innerHTML).substr(i+1), 2);
        total = operand1 +  operand2;
    }
    
    if (operator == "-") {
        let i= (document.getElementById("res").innerHTML).indexOf("-");
        let operand2 = parseInt((document.getElementById("res").innerHTML).substr(i+1), 2);
        total = operand1 -  operand2;
    }
    
    if (operator == "*") {
        let i= (document.getElementById("res").innerHTML).indexOf("*");
        let operand2 = parseInt((document.getElementById("res").innerHTML).substr(i+1), 2);
        total = operand1 * operand2
    }
    
    if (operator == "/") {
        let i= (document.getElementById("res").innerHTML).indexOf("/");
        let operand2 = parseInt((document.getElementById("res").innerHTML).substr(i+1), 2);
        total = operand1 /  operand2
    }
    
    document.getElementById("res").innerHTML = total.toString(2);
}