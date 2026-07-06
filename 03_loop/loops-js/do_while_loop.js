//1. Print Numbers from 1 to 10
let a = 1;
do {
    console.log(a);
    a++;
} while (a <= 10);

//2. Print Numbers from 10 to 1
let b = 10;
do {
    console.log(b);
    b--;
} while (b >= 1);

//3. Print Even Numbers from 1 to 20
let c = 1;
do {
    if (c % 2 === 0) {
        console.log(c);
    }
    c++;
} while (c <= 20);

//4. Print Odd Numbers from 1 to 19
let d = 1;
do {
    if (d % 2 !== 0) {
        console.log(d);
    }
    d++;
} while (d <= 20);

//5. Print the Multiplication Table of 7
let e = 7;
let f = 1;
do {
    console.log(`${e} x ${f} = ${e * f}`);
    f++;
} while (f <= 10);

//6. Find the Sum of Numbers from 1 to 10
let sum = 0;
let g = 1;
do {
    sum = sum + g;
    g++;
} while (g <= 10);

console.log(sum);

//7. Count from 1 to N
let h = 1;
let num = 15;
do {
    console.log(h);
    h++;
} while (h <= num);

//8. Print Squares of Numbers from 1 to 10
let j = 1;
do {
    console.log(j ** 2);
    j++;
} while (j <= 10);

//9. Print All Numbers Divisible by 5 from 1 to 50
let k = 1;
do {
    if (k % 5 === 0) {
        console.log(k);
    }
    k++;
} while (k <= 50);

//10. Count Down from N to 1
let l = 10;
do {
    console.log(l);
    l--;
} while (l >= 1);