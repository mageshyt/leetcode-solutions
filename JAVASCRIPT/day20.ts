const isObject = (x: null) => x !== null && typeof x === "object";


const objDiff = (obj1: any, obj2: any): any => {
  // logic
  // if both primitive and diff ,then diff
  // if on is object and other is'nt, then diff
  // if both are objects or arrays, then recurse
  // if one is array nd in obj , then diff

  if (!isObject(obj1) && !isObject(obj2)) {
    // both are primitive
    return obj1 === obj2 ? {} : [obj1, obj2];
  }

  if (!isObject(obj1) || !isObject(obj2)) {
    // one is primitive
    return [obj1, obj2];
  }

  // one is object and other is array
  if (Array.isArray(obj1) !== Array.isArray(obj2)) {
    return [obj1, obj2];
  }

  const diff = {};

  for (const key in obj1) {
    if (key in obj2) {
      const difference = objDiff(obj1[key], obj2[key]);
      if (Object.keys(difference).length > 0) {
        diff[key] = difference;
      }
    }
  }

  return diff;
};
