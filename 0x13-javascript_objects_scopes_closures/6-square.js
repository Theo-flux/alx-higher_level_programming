#!/usr/bin/node
const Squrae5 = require('./5-square');

class Square extends Squrae5 {
  constructor(size) {
    super(size);
    this.size = size;
  }

  charPrint(c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    }

    for (let i = 0; i < this.size; i++) {
      console.log('X'.repeat(this.size));
    }
  }
}

module.exports = Square;
