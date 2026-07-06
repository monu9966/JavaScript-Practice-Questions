//1. Print Numbers from 1 to 10
let a = 1;
while (a <= 10) {
    console.log(a);
    a++;
}

//2. Print Numbers from 10 to 1
let b = 10;
while (b >= 1) {
    console.log(b);
    b--;
}

//3. Print Even Numbers from 1 to 20
let m = 1;
while (m <= 20) {
    if (m % 2 === 0) {
        console.log(m);
    }
    m++;
}

//4. Print Odd Numbers from 1 to 20
let p = 1;
while (p <= 20) {
    if (p % 2 !== 0) {
        console.log(p);
    }
    p++;
}

//5. Print the Multiplication Table of 7
let c = 17;
let d = 1;
while (d <= 10 ) {
    console.log(`${c} x ${d} = ${c * d}`);
    d++;
}

//6. Find the Sum of Numbers from 1 to 10
let e = 1;
let sum = 0;
while (e <= 10) {
    sum = sum + e;
    e++;
}
console.log(sum)

//7. Count from 1 to N
let f = 1;
let n = 8;
while (f <= n) {
    console.log(f);
    f++;
} 

//8. Print Squares of Numbers from 1 to 10
let g = 1;
while (g <= 10) {
    console.log(g ** 2);
    g++;
}

//9. Print All Numbers Divisible by 5 from 1 to 50
let h = 1;
while (h <= 50) {
    if (h % 5 === 0) {
        console.log(h);
    }
    h++;
}

//10. Count Down from N to 1
let j = 5;
while (j >= 1) {
    console.log(j);
    j--;
}