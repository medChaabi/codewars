function maps(x) {
  let res = [];
  for (n of x) {
    res.push(n * 2);
  }
  return res;
}

console.log(maps([1,2,3]));