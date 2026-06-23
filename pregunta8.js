console.log("What will be displayed in the console?\n");

console.log("Code:");
console.log('let x = 5;');
console.log('let y = "10";');
console.log('let result = x + y;');
console.log('console.log(result);\n');

console.log("Options:");
console.log("A) 15");
console.log('B) "510"');
console.log("C) Error");
console.log("D) NaN");

// Simulación de la respuesta correcta
let respuesta = "B";

if (respuesta.toUpperCase() === "B") {
    console.log('Correct! The answer is "510"');
} else {
    console.log('Incorrect. The correct answer is "510"');
}