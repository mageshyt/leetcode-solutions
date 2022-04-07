// `In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

// If the town judge exists, then:

// The town judge trusts nobody.
// Everybody (except for the town judge) trusts the town judge.
// There is exactly one person that satisfies properties 1 and 2.
// You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

// Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

// Example 1:

// Input: n = 2, trust = [[1,2]]
// Output: 2
// Example 2:

// Input: n = 3, trust = [[1,3],[2,3]]
// Output: 3
// Input: n = 3, trust = [[1,3],[2,3],[3,1]]
// Output: -1
// `;
// //! Solution1:
// const findJudge = (N, trust) => {
//   const truster = Array(N).fill(0); // keep track of count of people this person trusts
//   const trustee = Array(N).fill(0); // keep track of count of people that trust this person
//   console.log({ trustee, truster });
//   for (let i = 0; i < trust.length; i++) {
//     let [a, b] = trust[i];
//     a--; //get indexes correct
//     b--;

//     truster[a]++;
//     // console.log(truster);
//     trustee[b]++;
//     // console.log(trustee);
//   }
//   console.log({ trustee, truster });
//   for (let i = 0; i < N; i++) {
//     if (truster[i] == 0 && trustee[i] == N - 1) {
//       return i + 1;
//     }
//   }

//   return -1;
// };
// (n = 3),
//   (trust = [
//     [1, 2],
//     [2, 3],
//   ]);
// // console.log(findJudge(n, trust));

// const findJudge2 = (n, trust) => {
//   if (!trust.length && n === 1) return n; // if there is no trust and only 1 person, then that person is the judge
//   let max_trust = -Infinity;
//   let trust_freq = new Map();
//   for (let i = 0; i < trust.length; i++) {
//     const [truster, trustee] = trust[i];
//     if (!trust_freq.has(trustee)) {
//       trust_freq.set(trustee, 1);
//     } else {
//       trust_freq.set(trustee, trust_freq.get(trustee) + 1);
//     }
//     // for finding max_trust
//     if (trust_freq.get(trustee) > max_trust) {
//       max_trust = trust_freq.get(trustee);
//     }
//   }
//   const trust_hash = new Map(trust);
//   for (let i = 1; i <= n; i++) {
//     if (!trust_hash.has(i) && max_trust === n - 1) {
//       return i;
//     }
//   }
//   return -1;
// };
// (n = 3),
//   (trust = [
//     [1, 3],
//     [2, 3],
//   ]);
// console.log(findJudge2(n, trust));
// console.log()
const guess_Name = (names, name) => {
  let result = [];
  for (let i = 0; i < names.length; i++) {
    if (names[i].includes(name)) {
      result.push(names[i]);
    }
  }
  return result;
};
const result = guess_Name(["John", "Jon", "Chris", "Chris", "Chris"], "Chris");
console.log(result);
