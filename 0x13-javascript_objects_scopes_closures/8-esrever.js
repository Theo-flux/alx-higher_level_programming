#!/usr/bin/node
exports.esrever = function (list) {
  let revList = [];
  for (let i = 0; i < list.length; i++) {
    revList[i] = list[list.length - i - 1];
  }
  return revList;
};
