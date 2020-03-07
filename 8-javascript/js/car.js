// Vars Attributes
var brand     = document.getElementById('brand');
var reference = document.getElementById('reference');
var cc        = document.getElementById('cc');
var model     = document.getElementById('model');
var color     = document.getElementById('color');
// Vars Buttons
var btn_on     = document.getElementById('btn-on');
var btn_off    = document.getElementById('btn-off');
var btn_forw   = document.getElementById('btn-forw');
var btn_back   = document.getElementById('btn-back');
var btn_stop   = document.getElementById('btn-stop');
// Vars Car
var path       = document.getElementById('path');
var vehicle    = document.getElementById('vehicle');
// Vars Logic
var engineOn   = false;
var stopeOn    = true;
// Vars Sounds
var sstart  = document.getElementById('sstart');
var sengine = document.getElementById('sengine');


var car = {
	// Atributos
	brand:     'Lamborgini',
	reference: 'Muercielago',
	cc:        6.2,
	model:     2016,
	color:     'Negro',
	image:     'imgs/lambo.png',
	// Métodos
	info: function() {
		brand.innerText     = this.brand;
		reference.innerText = this.reference;
		cc.innerText        = this.cc + " cc";
		model.innerText     = this.model;
		color.innerText     = this.color;
		vehicle.style.backgroundImage = "url("+this.image+")";
		//console.log(this.brand);
	},
	on: function() {
		if(engineOn == false) {
			sstart.play();
			vehicle.classList.add('on');
			engineOn = true;
		} else {
			alert("Not Allowed!");
		}
		//console.log('on');
	},
	off: function() {
		if(engineOn == true && stopeOn == true) {
			vehicle.classList.remove('on');
			engineOn = false;
		} else {
			alert("Not Allowed!");
		}
		
		//console.log('off');
	},
	stop: function() {
		if(engineOn == true && stopeOn == false) {
			sengine.pause();
			sengine.currentTime = 0;
			path.classList.add('stop');
			//path.classList.remove('forward');
			stopeOn = true;
		} else {
			alert("Not Allowed!");
		}
		//console.log('stop');
	},
	forward: function() {
		if (engineOn == true && stopeOn == true) {
			sengine.play();
			path.classList.remove('stop');
			path.classList.remove('backward');
			path.classList.add('forward');
			stopeOn = false;
		} else {
			alert("Not Allowed!");
		}
		//console.log('forward');
	},
	backward: function() {
		if(engineOn == true && stopeOn == true ) {
			path.classList.remove('stop');
			//path.classList.add('forward');
			path.classList.add('backward');
			stopeOn = false;
		} else {
			alert("Not Allowed!");
		}
		//console.log('backward');
	}
};

car.info();

btn_on.onclick = function() {
	car.on();
}
btn_off.onclick = function() {
	car.off();
}
btn_stop.onclick = function() {
	car.stop();
}
btn_forw.onclick = function() {
	car.forward();
}
btn_back.onclick = function() {
	car.backward();
}