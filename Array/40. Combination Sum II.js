`Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]`;

const combinationSum2 = (candidates, target) => {
  const result = [];
  candidates.sort((a, b) => a - b);
  const helper = (candidates, target, temp, index) => {
    if (target === 0) {
      result.push([...temp]);
      return;
    }
    if (target <= 0) return;
    let prev = Number.MAX_SAFE_INTEGER;
    for (let i = index; i < candidates.length; i++) {
      if (candidates[i] === prev) continue;
      prev = candidates[i];
      temp.push(candidates[i]);
      helper(candidates, target - candidates[i], temp, i + 1);
      temp.pop();
    }
  };
  helper(candidates, target, [], 0);
  return result;
};
console.log(combinationSum2([2, 5, 2, 1, 2], 5));
