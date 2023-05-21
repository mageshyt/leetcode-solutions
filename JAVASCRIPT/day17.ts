`2628. JSON Deep Equal`;

function areDeeplyEqual(o1: any, o2: any): boolean {
  if (o1 === o2) return true;

  // if there type is not obj

  if (typeof o1 !== "object" || typeof o2 !== "object") return false;

  if (Array.isArray(o1) !== Array.isArray(o2)) return false;

  //   if different length
  if (Object.keys(o1).length !== Object.keys(o2).length) return false;

  for (let key in o1) {
    if (!areDeeplyEqual(o1[key], o2[key])) return false;
  }

  return true;
}



