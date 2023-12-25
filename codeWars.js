// Write a function which calculates the average of the numbers in a given list.

// Note: Empty arrays should return 0.

function findAverage(array) {
  function calculateAverage(numbers) {
      // your code here
    if (!numbers || numbers.length === 0) {
      return 0;
    }

    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
      total += numbers[i]
    }

    const average = total / numbers.length;
    return average
  }
  return 0;
}
