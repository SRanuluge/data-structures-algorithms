import { array1, array2 } from "./data";

function isContainDuplicate() {
  for (const [i, v] of array1.entries()) {
    if (v) {
      for (const [j, q] of array2.entries()) {
        if (v === q) {
          return true; 
        }
      }
    }
  }
  return false;
}
console.log(isContainDuplicate(array1, array2));
// // O(a * b)   Time complexity 
// // O(1)       Space complexity this don't create new variables
