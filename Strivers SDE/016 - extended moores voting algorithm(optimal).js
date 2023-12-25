/*
Extended Moores Voting Algorithm (Optimal)
Given an array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays is
{3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8), so we need
to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2
and 3.

Time Complexity: O(nk)
Space Complexity: O(k)
*/

function extendedMooresVotingAlgorithm(arr, k) {
    let map = new Map();
    let result = [];
    let threshold = arr.length / k;
    
    for (let i = 0; i < arr.length; i++) {
        if (map.has(arr[i])) {
        map.set(arr[i], map.get(arr[i]) + 1);
        } else if (map.size < k) {
        map.set(arr[i], 1);
        } else {
        for (let [key, value] of map) {
            map.set(key, value - 1);
            if (value - 1 === 0) {
            map.delete(key);
            }
        }
        }
    }
    
    for (let [key, value] of map) {
        let count = 0;
        for (let i = 0; i < arr.length; i++) {
        if (arr[i] === key) {
            count++;
        }
        }
        if (count > threshold) {
        result.push(key);
        }
    }
    
    return result;
    }

    console.log(extendedMooresVotingAlgorithm([3, 1, 2, 2, 1, 2, 3, 3], 4)); // [2, 3]
    console.log(extendedMooresVotingAlgorithm([2, 7, 2], 2)); // [2]
    console.log(extendedMooresVotingAlgorithm([2, 3, 3, 2], 3)); // [2, 3]
    console.log(extendedMooresVotingAlgorithm([2, 3, 3, 2], 2)); // [2, 3]
    console.log(extendedMooresVotingAlgorithm([2, 3, 3, 2], 4)); // []
    console.log(extendedMooresVotingAlgorithm([2, 3, 3, 2, 1, 1, 1, 1], 4)); // [1]
    console.log(extendedMooresVotingAlgorithm([2, 3, 3, 2, 1, 1, 1, 1], 2)); // [1]
    console.log(extendedMooresVotingAlgorithm([2, 3, 3, 2, 1, 1, 1, 1], 3)); // [1]
    console.log(extendedMooresVotingAlgorithm([2, 3, 3, 2, 1, 1, 1, 1], 1)); // [1]
    