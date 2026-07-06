//2. Variables and Data Types (10 Questions)

//Q11. Declare a variable using let and log its value.
let a = 20;
console.log(a);

//Q12. Create a constant to store value of PI and log it. 
const pi = Math.PI;
console.log(pi);

//Q13. Reassign a value to a variable declared with let and log the result.
let x = 10;
x = 20;
console.log(x);

//Q14. Check the type of null and log it.
console.log(typeof(null));

//Q15. Create a variable with a number as a string (eg., "25") and log its type. 
var age = "25";
console.log(typeof(age));

//Q16.Use typeof to check the type of a boolean variable.
let name = true;
console.log(typeof(true));

//Q17. Create three variables of types string, number, blooean, and log their values.
let aa = "Hi", bb = 13, cc = true;
console.log(aa, bb, cc);

//Q18. Declare a variable without assinging a value. log its type.
let score;
console.log(typeof(score));

//Q19. Create a variable with undefined and log its type.
let d = undefined;
console.log(typeof(d));

//Q20. Use const to create an arra. Try reassinging the array and observe the error. 
const e = [1,2,3,4];
e.pop();
e.push(9);
console.log(e);