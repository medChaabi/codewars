function countPositivesSumNegatives(input) {
  if(input === null || input.filter(n=>n!=0).length==0) return []
  let countP = 0;
  let sumN = 0;
  input.map((num) => {
    if (num > 0) countP += 1;
    if (num < 0) sumN += num;
  });
  return [countP, sumN];
}

const res = countPositivesSumNegatives([1, 2, 3, -10, -11, -1]);
// const resb = countPositivesSumNegatives([]);
const resb = countPositivesSumNegatives([]);
console.log(res);
console.log(resb);
