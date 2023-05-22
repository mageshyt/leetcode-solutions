`2633. Convert Object to JSON String

Given an object, return a valid JSON string of that object. You may assume the object only inludes strings, 
integers, arrays, objects, booleans, and null. The returned string should not include extra spaces.
 The order of keys should be the same as the order returned by Object.keys().

Please solve it without using the built-in JSON.stringify method.


`;

const jsonStringify = (obj: any): string => {
  const type = typeof obj;

  console.log(type, obj);
  if (type === "string") {
    return `"${obj}"`;
  }

  if (type === "number" || type === "boolean" || obj === null) {
    return String(obj);
  }

  if (Array.isArray(obj)) {
    const res = obj.map((item) => jsonStringify(item));
    return `[${res.join(",")}]`;
  }

  if (type === "object") {
    const res = Object.keys(obj).map((key) => {
      return `"${key}":${jsonStringify(obj[key])}`;
    });
    return `{${res.join(",")}}`;
  }

  return "";
};

console.log(jsonStringify({ key: { a: 1, b: [{}, null, "Hello"] } }));
