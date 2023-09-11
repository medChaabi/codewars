const doubleChar = (str) => {
  let res = "";
  // str.map(c=>console.log(c*2))
  for(c of str){
    res += c + c
  }
  return res;
};
const res = doubleChar("salam d");
console.log(res);
