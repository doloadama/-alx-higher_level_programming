#!/usr/bin/node
class Rectangle{
    constructor(w, h) {
	if (typeof width === 'number' && typeof height === 'number' && width > 0 && height > 0) {
	    this.width = w;
	    this.height = w;
	}
    }
    print () {
	for (let i = 0; i < this.height; ++i) {
	    let j = 0;
	    for (; j < this.width; ++j) {
		process.stdout.write('X');
	    }

	    if ( j === this.width) {
		console.log('');
	    }
	}
    }
}
module.export = Rectangle;
