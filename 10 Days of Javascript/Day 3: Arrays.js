/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    let sorted = nums.sort(compare);
    function compare(first, second) {return first - second;}
      let removeDuplicate = [sorted[0]];  
      let ans = [];  

      for(let i=1; i < sorted.length; i++) {  
        if(sorted[i-1] !== sorted[i]) {
          removeDuplicate.push(sorted[i]);  
        }  
      }

      return removeDuplicate[removeDuplicate.length-2];
}