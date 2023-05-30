`2618. Check if Object Instance of Class`;

function checkIfInstanceOf(obj: any, classFunction: any): boolean {
  if (typeof obj !== "object" || obj === null) return false;
  return obj instanceof classFunction;
}
