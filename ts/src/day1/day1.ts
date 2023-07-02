import * as fs from "fs";

const input: string = fs.readFileSync("input.txt", "utf-8");

// in TS it's convention to use camelCase, snake_case is rarely used
function getFloorsWithTarget(floors: string[], target: number = -1): { floorsCount: number, targetAt: number } {
  let floorsCount = 0
  let targetAt: number | null = null;
  floors.forEach((char, index) => {
    char === '(' ? floorsCount++ : floorsCount--
    floorsCount === target ? targetAt = index : null
  })

  if (!targetAt) {
    throw new Error("target at empty")
  }

  // function expects as to return 2 arguments specified after semicolon in function definition, we don't have to return them like
  // {floorsCount: floorsCount, targetAt: targetAt} - if names are the same, TS/JS will figure that out 
  return { floorsCount, targetAt }
}

// if you're curious what it is, it is destructuring, you can read about it, but in this case function returns object with 2 properties
// and while declaring properties we declare them and assign to whatever function returns (in this case floorsCount and target)
const { floorsCount, targetAt } = getFloorsWithTarget(input.split(''))
console.log(
  `The instructions take Santa to floor ${floorsCount} and the position of the first character taking Santa to the target floor is ${targetAt}.`
);

// TS has some powerfull methods, many of which are for arrays, below is example of above code in more functional manner
// ts ignore comment below will silent warning, that we are not using this function
// @ts-ignore
function getFloorsWithTarget2(floors: string[], target: number = -1): { floorsCount: number, targetAt: number } {
  return floors.reduce(
    (accumulator, char, index) => {
      accumulator.floorsCount += char === '(' ? 1 : -1;
      if (accumulator.floorsCount === target) {
        accumulator.targetAt = index;
      }
      return accumulator;
    },
    { floorsCount: 0, targetAt: -1 }
  );
}

// you can also define functions as arrow functions, it has it's own behavior, but that's topic for future
// @ts-ignore
const myFunction = (num: number): number => {
  return num + 4
}

