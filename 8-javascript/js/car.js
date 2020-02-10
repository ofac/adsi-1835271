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
		//console.log(this.brand);
	},
	on: function() {
		console.log('on');
	},
	off: function() {
		console.log('off');
	},
	stop: function() {
		console.log('stop');
	},
	forward: function() {
		console.log('forward');
	},
	backward: function() {
		console.log('backward');
	}
};

car.info();