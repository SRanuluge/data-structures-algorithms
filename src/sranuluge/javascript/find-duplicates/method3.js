import { array1, array2 } from "./data";

// Readability is good
const isContainDuplicate = (arr1, arr2) =>
  arr1.some((item) => arr2.includes(item)); 

console.log(isContainDuplicate(array1, array2));
