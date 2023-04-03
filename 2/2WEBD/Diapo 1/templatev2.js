function number_or_not(x) {
    if (isNaN(x)) {
      return "Pas un nombre !";
    }
    return x;
}

let chiffre = 52;
let str = "test";

//simple

console.log(number_or_not(15));
console.log(number_or_not("Michel"));
console.log(number_or_not(`dzdzd`));
console.log(number_or_not(`52`));

//Concatenate

console.log(number_or_not(`${chiffre}`));
console.log(number_or_not(`${str}`));
console.log(number_or_not(`${chiffre}${chiffre}`));
console.log(number_or_not(`${chiffre}${str}`));