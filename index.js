let firstVariable = 10;
let secondVariable = 20
let temp;
temp = firstVariable
firstVariable = secondVariable
secondVariable = temp
console.log("🚀 ~ file: After swapping", firstVariable, secondVariable)


// Swapping without using a third variable
let firstVariable = 10;
let secondVariable = 20
firstVariable = firstVariable + secondVariable
secondVariable = firstVariable-secondVariable
firstVariable =firstVariable-secondVariable
console.log("🚀 ~ file: After swapping", firstVariable, secondVariable)