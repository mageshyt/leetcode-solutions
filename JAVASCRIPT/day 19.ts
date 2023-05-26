`2675. Array of Objects to Matrix

Input: 
arr = [
  {"b": 1, "a": 2},
  {"b": 3, "a": 4}
]
Output: 
[
  ["a", "b"],
  [2, 1],
  [4, 3]
]

Explanation:
There are two unique column names in the two objects: "a" and "b".
"a" corresponds with [2, 4].
"b" coresponds with [1, 3].

`;
// Helper function to check if a value is an object
const isObject = (x: null) => x !== null && typeof x === "object";
function jsonToMatrix(arr: any[]): (string | number | boolean | null)[][] {
  // Recursive function to get keys

  const getKeys = (obj: any): string[] => {
    if (!isObject(obj)) return [""];

    let keys: string[] = [];
    const objKeys = Object.keys(obj);

    objKeys.forEach((key) => {
      if (isObject(obj[key])) {
        keys = keys.concat(getKeys(obj[key]).map((k) => `${key}.${k}`));
      } else {
        keys.push(key);
      }
    });

    return keys;
  };

  // Get all keys
  const keys = Array.from(
    new Set(arr.map((obj) => getKeys(obj)).flat())
  ).sort();

  //   get the value for the given key

  const getValue = (
    obj: any,
    path: string
  ): string | number | boolean | null => {
    const paths = path.split(".");

    let value = obj;

    let i = 0;

    while (i < paths.length && isObject(value)) {
      value = value[paths[i]];
      i++;
    }
    // If the value is not found or is an object, return an empty string

    return i < paths.length || isObject(value) || value === undefined
      ? ""
      : value;
  };

  // build the matrix

  const matrix: any = [keys];

  arr.forEach((obj: any) => {
    return matrix.push(keys.map((key: string) => getValue(obj, key)));
  });

  return matrix;
}

console.log(
  jsonToMatrix([
    { b: 1, a: 2 },
    { b: 3, a: 4 },
  ])
);
