#!/usr/bin/node
exports.converter = function (base) {
  console.log(`base: ${base}`);
  return (num) => num.toString(base);
};
