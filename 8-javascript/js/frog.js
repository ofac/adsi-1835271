
var btnPlay    = document.getElementById('btn-play');
var btnCredits = document.getElementById('btn-credits');
var btnBack    = document.getElementById('btn-back');
var screens    = document.getElementsByClassName('screen');
var frog       = document.getElementById('frog');
var cars       = document.getElementsByClassName('car');

btnPlay.onmouseover = function() {
	this.classList.add('animated', 'heartBeat', 'infinite');
}
btnPlay.onmouseout = function() {
	this.classList.remove('animated', 'heartBeat', 'infinite');
}
btnPlay.onclick = function() {
	game.screenTo(0, 1);
	game.start();
}
btnCredits.onmouseover = function() {
	this.classList.add('animated', 'heartBeat', 'infinite');
}
btnCredits.onmouseout = function() {
	this.classList.remove('animated', 'heartBeat', 'infinite');
}
btnCredits.onclick = function() {
	game.screenTo(0, 2);
}
btnBack.onmouseover = function() {
	this.classList.add('animated', 'heartBeat', 'infinite');
}
btnBack.onmouseout = function() {
	this.classList.remove('animated', 'heartBeat', 'infinite');
}
btnBack.onclick = function() {
	game.screenTo(2, 0);
}

var game = {
	postLeft: 368,
	postTop: 480,
	start: function() {
		this.moveFrog();
		this.randomCars();
	},
	moveFrog: function() {
		document.onkeyup = function(event) {
			//console.log(event.keyCode);
			// Left - - - - - - - - - - - - - - - 
			if(event.keyCode == 37) {
				if(game.postLeft > 8) {
					game.postLeft -= 60; 
					frog.style.left = game.postLeft+'px';
				}
				game.jumpFrog();
			}
			// Right - - - - - - - - - - - - - - - 
			if(event.keyCode == 39) {
				if(game.postLeft < 728) {
					game.postLeft += 60; 
					frog.style.left = game.postLeft+'px';
				}
				game.jumpFrog();
			}
			// Up - - - - - - - - - - - - - - - 
			if(event.keyCode == 38) {
				if(game.postTop > 0) {
					game.postTop -= 60; 
					frog.style.top = game.postTop+'px';
				}
				game.jumpFrog();
			}
			// Down - - - - - - - - - - - - - - - 
			if(event.keyCode == 40) {
				if(game.postTop < 480) {
					game.postTop += 60; 
					frog.style.top = game.postTop+'px';
				}
				game.jumpFrog();
			}
		}
	},
	randomCars: function() {
		var lt  = -100; // left
		var tp  = 480;  // top 
		var rt  = 0;    // rotate
		var tm  = 60;    // time
		var dr  = 'r';  // direction
		for (var i=0; i < cars.length; i++) {
			let rndcar = Math.round(Math.random() * 5);
			if(i == 3) {
				lt = 810;
				tp -= 60;
				rt = 180
				dr = 'l';
			}
			tp -= 60;
			tm -= 10;
			cars[i].style.top       = tp+'px';
			cars[i].style.left      = lt+'px';
			cars[i].style.transform = 'rotate('+rt+'deg)';
			cars[i].classList.add('car'+rndcar);
			this.moveCars(cars[i], tm, dr);
		}
	},
	moveCars: function(car, tme, dir) {
		let posl = -100;
		let posr = 810;
		setInterval(function() {
			if(dir == 'r') {
				if(posl < 810) {
					posl += 10;
					car.style.left = posl+'px';
				} else {
					posl = -100;
				}	
			} else {
				if(posr > -100) {
					posr -= 10;
					car.style.left = posr+'px';
				} else {
					posr = 810;
				}
			}
		}, tme);
	},
	jumpFrog: function() {
		frog.classList.add('animated', 'heartBeat');
		setTimeout(function() {
			frog.classList.remove('animated', 'heartBeat');
		}, 360);
	},
	screenTo: function(start, final) {
		screens[start].classList.remove('bounceInUp');
		screens[start].classList.add('bounceOutDown');
		setTimeout(function() {
			screens[start].classList.remove('bounceOutDown');
			screens[start].classList.add('hide');
			screens[final].classList.remove('hide');
			screens[final].classList.add('animated', 'bounceInUp');
		}, 800);
	}
};
