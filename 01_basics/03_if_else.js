// Question 1: Positive, Negative, or Zero
// Write a program to check whether a number is:
// Positive
// Negative
// Zero
let n = 10;
if (n > 0) {
    console.log(n, "Number is Positive");
} else if (n < 0) {
    console.log(n, "Number is Negative");
    
} else {
    console.log(n, "Number is Zero");
}

//Question 2: Even or Odd
//Write a program to check whether a number is even or odd.

let number = 111;
if (number % 2 === 0) {
    console.log(number, "is Even");
} else {
    console.log(number, "is Odd");
}

//Question 3: Eligible to Vote
//If a person's age is 18 or above, print: Eligible to vote Otherwise print: Not eligible to vote

// let age = 8;
// if (age >= 18) {
//     console.log("You are Eligible to vote");
// } else {
//     console.log("You are Not Eligible to vote");
// }

//Question 4: Pass or Fail
//If marks are 35 or above, print:Pass Otherwise print: Fail

let marks = 300;
if (marks >= 35) {
    console.log("Pass");
} else {
    console.log("Fail");
}

//Question 5: Greater Number
//Given two numbers, print the greater number.

let x = 10;
let y = 10;
if (x >= y) {
    console.log(x, "is Greater number");
} else {
    console.log(y, "is greater number");
}

//Question 6: Divisible by 5
//Check whether a number is divisible by 5.

let num = 13;
if (num % 5 === 0) {
    console.log(num, "is divisible by 5");
} else {
    console.log(num, "is not divisible by 5");
}

//Question 7: Driving License Eligibility
//If age is 18 or above, print: Can apply for driving license Otherwise print: Cannot apply

let age = 20;
if (age >= 18) {
    console.log("You can apply for driving license");
} else {
    console.log("You cannot apply");
}

//Question 8: Largest of Three Numbers
//Given three numbers, print the largest number.

let a = 10;
let b = 50;
let c = 30;

if (a >= b && a >= c) {
    console.log(a, "is largest number.");
} else if (b >= a && b >= c) {
    console.log(b, "is largest number.");
} else {
    console.log(c, "is largest number.")
}

//Question 9: Leap Year (Easy Version)
//Check if a year is divisible by 4.
//If yes: Leap Year Otherwise: Not a Leap Year

let year = 2024;
if (year % 4 === 0) {
    console.log(year, "is Leap Year");
} else {
    console.log(year, "not a Leap Year");
}

//Question 10: Temperature Check
// If temperature is greater than 30, print: Hot Otherwise print: Cool

let temp = 40;
if (temp > 30) {
    console.log("Hot");
} else {
    console.log("Cool");
}