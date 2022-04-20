//////////////////
// EDABIT
/////////////////
// 1. HOW EDABIT WORKS
const hello = () => {
  return "hello edabit.com";
};

console.log(hello());

// 2. Two Makes Ten
const makesTen = (a, b) => {
  return a === b;
};

console.log(makesTen());

// 3. Concatenate First and Last Name into One String
const concatName = (firstName, lastName) => {
  return `${lastName}, ${firstName}`;
};

console.log(concatName("Joe(first name)", "Mama(last name)"));
