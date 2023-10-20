`You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

 

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].`;

class NestedIterator {
  constructor(nestedList) {
    this.stack = flatten(nestedList);
  }
  flatten(nestedList) {
    return nestedList.flatMap((nested) =>
      nested.isInteger() ? nested.getInteger() : this.flatten(nested.getList())
    );
  }

  hasNext() {
    return this.stack.length > 0;
  }
  next() {
    return this.stack.shift();
  }
}

const test = new NestedIterator([[1, 1], 2, [1, 1]]);
console.log(test.next());
console.log(test.next());

const NestedIterator = (nestedList) => {
  stack = [];
  const flat = (list) => {
    return list.reduce((acc, curr) => {
      const isInteger = typeof curr === "number";

      return acc.concat(isInteger ? [curr] : flat(curr));
    }, []);
  };
  stack = flat(nestedList);
};

NestedIterator.prototype.hasNext = function () {
  return this.stack.length > 0;
};

NestedIterator.prototype.next = function () {
  return this.stack.shift();
};
