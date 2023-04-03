let var1 = 1; //global

function maFonction() {
    let var2 = 2;

    for (let var3 = 0; var3 < 3; var3++) {
       console.log(var1);
       console.log(var2);
       console.log(var3);
    }
    console.log(var3);
}


console.log(var1);
console.log(var2); //error
console.log(var3); //error