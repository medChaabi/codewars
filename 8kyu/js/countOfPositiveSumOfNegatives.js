function countPositivesSumNegatives(input) {
  let countP = 0;
  let sumN = 0;
  input.map((num) => {
    if (num > 0) {
      countP += 1;
    } else {
      sumN += num;
    }
  });
  return [countP, sumN];
}

const res = countPositivesSumNegatives([1, 2, 3, -10, -11, -1]);
console.log(res);
