// 
// Quicksort
// 

export default function Quicksort(array, start=0, end=0) {
  // console.log(`Quicksort:   sorting ${start} to ${end}`);

  function _partition(p, r) {
    // r is going to serve a our fulcrum
    // p is going to serve as our first partition marker
    // autoincrementing i will serve as our second partition marker
    //  i stats one ahead of p
    //  i iterates from subset start to fulcrum - 1
    // there is an issue here with an off-by-one dealing with zero-indexed
    let x = array[r];
    let i = p - 1;
    // console.log(`_partition:  fulcrum is ${x}`);
    for (let j=p; j<=r-1; j++) {
      // console.log(`_partition:  p1(i) is ${i}`);
      // console.log(`_partition:  p2(j) is ${j}`);
      // console.log(`_partition:  checking ${array[j]} against ${x}`);
      if (array[j] <= x) {
        i++;
        // console.log(`_partition:  found ${array[j]} less than ${x}, swapping ${array[i]} with ${array[j]}`);
        [array[i], array[j]] = [array[j], array[i]];
        // console.log(array);
      }
    }
    [array[i+1], array[r]] = [array[r], array[i+1]];
    // console.log(`_partition:  partition returns fulcrum ${i+1}`);
    return i+1;
  }

  if (start < end) {
    let fulcrum = _partition(start, end);
    // console.log(`Quicksort:   fulcrum was ${fulcrum}`);
    Quicksort(array, start, fulcrum - 1);
    Quicksort(array, fulcrum + 1, end);
  }

  return array;
}

// const testArray = [...Array(8)].map(i => Math.floor(Math.random()*100));
// console.log(testArray);
// const sorted = Quicksort(testArray, 0, testArray.length - 1);
// console.log(sorted);
// console.log(testArray.sort((a, b) => a - b));
