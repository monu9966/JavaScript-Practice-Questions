//1. Print Numbers from 1 to 10
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

//2. Print Numbers from 10 to 1
for (let a = 10; a >= 1; a--) {
    console.log(a);
}

//3. Print Even Numbers from 1 to 20
for (let b = 2; b <= 20; b +=  2) {
    console.log(b);
}

//4. Print Odd Numbers from 1 to 20
for (let c = 1; c <= 20; c += 2) {
    console.log(c);
}

//5. Print the Multiplication Table of 5
let n = 5;
for (let d = 1; d <= 10; d++) {
    console.log(`${n} x ${d} = ${n * d}`);
}

//6. Find the Sum of Numbers from 1 to 10
let sum = 0;
for (let e = 1; e<= 10; e++) {
    sum = sum + e;
}

console.log(sum);

//7. Count from 1 to N
let num = 17;
for (let g = 1; g <= num; g++) {
    console.log(g);
}

//8. Print Squares of Numbers from 1 to 10
for (let h = 1; h <= 10; h++) {
    console.log(`${h ** 2}`);
}

//9. Print All Numbers Divisible by 3 from 1 to 30
let j = 3;
for (let k = 1; k <= 30; k++) {
    if (k % 3 === 0 ) {
        console.log(k);
    }
}

//10. Count Down from N to 1
let nums = 18 ;
for (let l = nums; l >= 1; l--) {
    console.log(l);
}