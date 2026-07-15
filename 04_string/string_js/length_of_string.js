//1. Find the length of a string.
let a = "Butterfly"
console.log(a.length);

//2. Check if a string is empty.
let b = ""
if (b == "") {
    console.log("String is empty")
} else {
    console.log("String does not empty")
}

//3. Check if a string has exactly 5 characters.
let c = "mohit"
if (c.length == 5) {
    console.log("The string has exactly 5 character");
} else {
    console.log("The string do not have exactly 5 character");
}

//4. Check if the string length is even or odd.
let d = "Birds";
let len = d.length;
if (len % 2 == 0) {
    console.log( "Even");
} else {
    console.log( "Odd");
}

//5. Check if the string has more than 10 characters.
let e = "Programm"
if (e.length > 10) {
    console.log("The string has more than 10 characters.");
} else {
    console.log("He string has 10 or fewer characters.")
}


//6. Print the last index of a string. 
let f = "JavaScript"
let lastIndex = f.length -1;
console.log("Last Index:", lastIndex);

//7. Print the first half of a string.
let g = "Hello"
let half = g.slice(0, g.length / 2);
console.log("First half:", half);

//8. Print the second half of a string.
let secondHalf = g.slice(g.length / 2);
console.log("Second half:", secondHalf);

//9. Print the middle character of a string.
let middleCharacter = Math.floor(g.length / 2);
console.log("Middle character:", g[middleCharacter]);

//10. Check whether two strings have the same length.
let strOne = "Dog";
let strTwo = "Cat";

if (strOne.length == strTwo.length) {
    console.log("Both string have same length")
} else {
    console.log("Both string don't have same length")
}



