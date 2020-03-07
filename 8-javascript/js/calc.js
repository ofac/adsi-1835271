// Calculator Elements
var btnTheme = document.getElementById('theme');
var calc     = document.getElementsByClassName('calc');
var dspMath  = document.getElementById('displayMath');
var dspAns   = document.getElementById('displayAnswer');
var memAns   = null;

// Buttons (Numbers)
var bt0 = document.getElementById('bt-0');
var bt1 = document.getElementById('bt-1');
var bt2 = document.getElementById('bt-2');
var bt3 = document.getElementById('bt-3');
var bt4 = document.getElementById('bt-4');
var bt5 = document.getElementById('bt-5');
var bt6 = document.getElementById('bt-6');
var bt7 = document.getElementById('bt-7');
var bt8 = document.getElementById('bt-8');
var bt9 = document.getElementById('bt-9');
// Buttons (Actions)
var btClear = document.getElementById('bt-clear');
var btDel   = document.getElementById('bt-del');
var btPlus  = document.getElementById('bt-plus');
var btSubs  = document.getElementById('bt-subs');
var btPro   = document.getElementById('bt-pro');
var btDiv   = document.getElementById('bt-div');
var btPow   = document.getElementById('bt-pow');
var btPl    = document.getElementById('bt-pl');
var btPr    = document.getElementById('bt-pr');
var btDot   = document.getElementById('bt-dot');
var btMod   = document.getElementById('bt-mod');
var btAns   = document.getElementById('bt-ans');
var btRq    = document.getElementById('bt-rq');
var btEqual = document.getElementById('bt-equal');

// Booleans
var allowOper = false;

// Functions
function setValueInDisplay(val) {
	// 34 characters
	if(dspMath.value.length <= 34) {
		if (val.constructor.name == "Number") {
				allowOper = true;
				dspMath.value += val;
			} else {
				if(allowOper) {
					dspMath.value += val;
					allowOper = false;
				}
			}
	}
}

// Events
btnTheme.onclick = function() {
	calc[0].classList.toggle('dark');
}

bt0.onclick = function() {
	setValueInDisplay(0);
}
bt1.onclick = function() {
	setValueInDisplay(1);
}
bt2.onclick = function() {
	setValueInDisplay(2);
}
bt3.onclick = function() {
	setValueInDisplay(3);
}
bt4.onclick = function() {
	setValueInDisplay(4);
}
bt5.onclick = function() {
	setValueInDisplay(5);
}
bt6.onclick = function() {
	setValueInDisplay(6);
}
bt7.onclick = function() {
	setValueInDisplay(7);
}
bt8.onclick = function() {
	setValueInDisplay(8);
}
bt9.onclick = function() {
	setValueInDisplay(9);
}
btClear.onclick = function() {
	dspMath.value = '';
	dspAns.value  = '';
}
btDel.onclick = function() {
	dspMath.value = dspMath.value.slice(0,-1);
}
btPlus.onclick = function() {
	setValueInDisplay('+');
}
btSubs.onclick = function() {
	setValueInDisplay('-');
}
btPro.onclick = function() {
	setValueInDisplay('*');
}
btDiv.onclick = function() {
	setValueInDisplay('/');
}
btPow.onclick = function() {
	//setValueInDisplay('');
}
btRq.onclick = function() {
	//setValueInDisplay('');
}
btPl.onclick = function() {
	setValueInDisplay('(');
}
btPr.onclick = function() {
	setValueInDisplay(')');
}
btDot.onclick = function() {
	setValueInDisplay('.');
}
btMod.onclick = function() {
	setValueInDisplay('%');
}
btAns.onclick = function() {
	if(memAns != null ) {
		dspMath.value = memAns;
	} else {
		if(dspAns.value.length > 0) {
			memAns = dspAns.value; 
			dspMath.value = memAns;
			dspAns.value = '';
		}
	}
}
btEqual.onclick = function() {
	if(dspMath.value.length > 0) {
		dspAns.value = eval(dspMath.value);
		dspMath.value = '';	
	}
}

//
document.onkeyup = function(evt) {
	//console.log(evt.keyCode);
	switch(evt.keyCode) {
		case 8:
			dspMath.value = dspMath.value.slice(0,-1);
			break;
		case 13:
			if(dspMath.value.length > 0) {
				dspAns.value = eval(dspMath.value);
				dspMath.value = '';	
			}
			break;	
		case 46:
			dspMath.value = '';
			dspAns.value  = '';
			break;	
		case 48:
			setValueInDisplay(0);
			break;
		case 49:
			setValueInDisplay(1);
			break;
		case 50:
			setValueInDisplay(2);
			break;
		case 51:
			setValueInDisplay(3);
			break;
		case 52:
			setValueInDisplay(4);
			break;
		case 53:
			setValueInDisplay(5);
			break;
		case 54:
			setValueInDisplay(6);
			break;
		case 55:
			setValueInDisplay(7);
			break;
		case 56:
			setValueInDisplay(8);
			break;
		case 57:
			setValueInDisplay(9);
			break;		
		case 187:
			setValueInDisplay('+');
			break;
		case 189:
			setValueInDisplay('-');
			break;		
		case 190:
			setValueInDisplay('.');
			break;
		case 191:
			setValueInDisplay('/');
			break;	
		case 221:
			setValueInDisplay('*');
			break;									
	}
}
