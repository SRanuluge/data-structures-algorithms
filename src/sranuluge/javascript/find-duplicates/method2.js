import { array1, array2 } from "./data";

let map = {};
function isContainDuplicate() {
  for (const [i, v] of array1.entries()) {
    if (!map[v]) {
      map[v] = true;
    }
  }

  for (const [j, q] of array2.entries()) {
    if (map[q]) {
      return map[q];
    }
  }
  return false;  
}

//o(a + b) when comes to the time complexity good
//o(a) Space complexity bad => creating a objet
console.log(isContainDuplicate(array1, array2));
