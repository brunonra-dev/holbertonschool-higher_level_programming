#!/usr/bin/node
exports.converter = function (base) {
  return (i) => { return i.toString(base); };
};
