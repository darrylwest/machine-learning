#!/usr/bin/env node

// dpw@seattle.local
// 2016.10.03
'use strict';

const trainingSetA = {
    xvector: [ 3, 2, 4, 0 ],
    yvector: [ 4, 1, 3, 1 ]
};

/*
const trainingSetB = {
    xvector: [ 1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 8, 10 ], 
    yvector: [
};
*/

// calculate the cost for theta 0,1 against the training set...
const calcCost = function(theta0, theta1, ts) {

    if (!ts) {
        ts = trainingSetA;
    }

    const m = ts.xvector.length;
    const dr = (2 * m);

    let sum = 0;
    let idx = 0;

    while (idx < m) {
        let x = ts.xvector[ idx ];
        let y = ts.yvector[ idx ];

        let result = theta1 * x + theta0;
        let cost = Math.pow(( result - y ), 2);

        // sum up the cost squared
        sum = sum + cost;

        console.log(`idx: ${idx}, result: ${result}, cost: ${cost}, sum: ${sum}`); 

        idx++;
    }

    const totalCost = sum / dr;

    return totalCost;
};

const q1 = function() {
    const q = `
        Consider the problem of predicting how well a student does in her second year of college/university, given how well they did in their first year.

        Specifically, let x be equal to the number of "A" grades (including A-. A and A+ grades) that a student receives in their first year of college 
        (freshmen year). We would like to predict the value of y, which we define as the number of "A" grades they get in their second year (sophomore year).

        Refer to the following training set of a small sample of different students' performances (note that this training set may also be referenced in 
        other questions in this quiz). Here each row is one training example. Recall that in linear regression, our hypothesis is hθ(x)=θ0+θ1x, and we 
        use m to denote the number of training examples.
    `;

    const m = trainingSetA.xvector.length;
    console.log( `q1) m = ${m}`);

};

const q2 = function() {
    const q = `
        With the training set, recall that out definition of the cost function was J(θ0,θ1) = 1/2m m∑i=1 (hθ(x(i))−y(i))^2.
        What is J(0,1)? in the box below, please enter the answer (Simplify fractions to decimals when entering anser, and '.' as the delimiter, e.g. 1.5).
    `;

    console.log(`q2) ${q}`);
    console.log(`cost = ${calcCost( 0, 1 )}`);

};

const q3 = function() {

    const theta0 = -2;
    const theta1 = 0.5;
    const x = 6; // trainingSet.xvector[3];
    const y = theta0 + theta1 * x;

    console.log(`q3) h(${x}) = ${theta0} + ${theta1} * ${x} = ${y}`);
};


q1();
q2();
q3();

console.log( 'q4) check #3' );
console.log( 'q5) check #2' );
