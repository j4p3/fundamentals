import Quicksort from './Quicksort';

test('orders an array', () => {
  const testArray = [...Array(1400)].map(i => Math.floor(Math.random()*10000));
  const sortableArray = testArray;
  Quicksort(sortableArray, 0, sortableArray.length - 1);
  testArray.sort((a, b) => a - b);
  for (var i in testArray) {
    // console.log(`${testArray[i]} : ${sortableArray[i]}`);
    expect(sortableArray[i]).toBe(testArray[i]);
  }
});
