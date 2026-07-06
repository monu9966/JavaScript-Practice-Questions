
//1. Basic Console Usage (10 Questions)
//Q1. Log your name  and favorite hobby to the console.
console.log("Monu", ",", "Listening Music")

//Q2. Perform and log the result of 45 * 2 - 10.
console.log(45 * 2 - 10);

//Q3. Use console.log() display the current year. 
const newdate = new Date();
console.log(newdate.getFullYear());

//Q4. create twi variables for first and last name then Concatenate and log them.
var first = "Monu";
var last = "Thakur";

console.log(first + " " + last);

//Q5. Track the value of a variable by logging it before and after updating.
var a = 12;
console.log(a);
a = 20;
console.log(a);

//Q6. Use console.error() to simulate an error message.
console.error("Something went wrong");

//Q7. Log the square of the number 12 to the console.
console.log(12 * 12);

//Q8. Print the type of a variable holding the value true.
var a = "M";
console.log(typeof a);

//Q9. Create a variable holding your age and log whether it's grather than 18.
let age = 20;

if (age > 18) console.log(true);
else console.log(false);

//Q10. Log the result of 100 / 0 and observe output.
console.log(100/0);