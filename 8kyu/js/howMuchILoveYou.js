const howMuchILoveYou = (nbPetals) => {
  const phras = [
    "I Love You",
    "a Little",
    "a lot",
    "passionately",
    "madly",
    "not at all",
  ];
  let index = nbPetals % phras.length - 1
  if (index === -1) index = phras.length - 1
  return phras[index]
};

console.log(howMuchILoveYou(4));