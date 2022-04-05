#!/usr/bin/node
exports.esrever = function (list) {
  const tmp = [];

  for (let n = list.length - 1; n >= 0; n--) {
    tmp.push(list[n]);
  }

  return tmp;
};
