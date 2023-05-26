const chunk = (arr: any[], size: number) => {
  const res: any = [];
  for (let i = 0; i < arr.length; i += size) {
    res.push(arr.slice(i, i + size));
  }
  return res;
};

const compact = (arr: any[]) => arr.filter(Boolean);
