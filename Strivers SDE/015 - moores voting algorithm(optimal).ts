/* 
Moore's Voting Algorithm(Optimal Solution)
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times.
Space Complexity: O(1)
Time Complexity: O(n)
*/

function majorityElement(nums: number[]): number {
    let count = 0;
    let candidate = 0;
    for (let num of nums) {
        if (count === 0) {
            candidate = num;
        }
        count += (num === candidate) ? 1 : -1;
    }
    return candidate;
};

console.log(majorityElement([3, 2, 3])); // 3
console.log(majorityElement([2, 2, 1, 1, 1, 2, 2])); // 2
console.log(majorityElement([1])); // 1
console.log(majorityElement([1, 2])); // 1
