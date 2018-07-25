// 
// Heap class
//  methods for building heap, inserting, removing, sorting
//  building heap is O(n)
//  sorting heap is O(log(n))
// comparitor: Fn(int, int) => Bool
// 
class Heap {
  // max heap
  constructor(comparitor) {
    const defaultComparitor = (a, b) =>  a - b > 0;
    this._heap = [];
    this._heapsize = this._heap.length;
    this._cmp = comparitor || defaultComparitor;
  }

  insert(v) {
    let i = this._heap.push(v) - 1;
    let p = Math.floor(i / 2);
    while (p >= 0 && this._cmp(this._heap[i], this._heap[p])) {
      // walk up tree and swap new value upward until it fits
      [this._heap[i], this._heap[p]] = [this._heap[p], this._heap[i]];
      i = p;
      p = Math.floor(p / 2);
    }
    // clean up by heapifying location of last swap
    this._heapify(i);
    this._resizeHeap();
  }
  
  extract() {
    if (!this._heap.length) {
      return undefined;
    }
    const i = this.heap.shift();
    this._heapify(0);
    this._resizeHeap();

    return i;
  }

  buildHeap(arr) {
    this._heap = arr;
    for (let i=Math.floor(arr.length/2); i>=0; i--) {
      this._heapify(i);
    }
    this._resizeHeap();
  }

  heapsort() {
    for (var i = this._heapsize - 1; i >= 1; i--) {
      // swap largest to end
      [this._heap[0], this._heap[i]] = [this._heap[i], this._heap[0]];

      // decrement heap size and reorder
      this._heapsize -= 1;
      this._heapify(0);
    }
    return this._heap;
  }

  _resizeHeap() {
    this._heapsize = this._heap.length;
  }

  _heapify(i) {
    const left = 2*i+1;
    const right = 2*i+2;
    let m = i;

    if (left < this._heapsize &&
        this._cmp(this._heap[left], this._heap[i])) {
      m = left;
    }
    if (right < this._heapsize &&
        this._cmp(this._heap[right], this._heap[m])) {
      m = right;
    }
    if (m !== i) {
      [this._heap[i], this._heap[m]] = [this._heap[m], this._heap[i]];
      this._heapify(m);
    }
  }

}

// 
// Heapsort as a function on an unsorted array
//  builds heap, sorts it, returns
//  building heap is O(n)
//  sorting heap is O(log(n))
// arr: Array<int>
// 
function Heapsort(arr) {
  let heapsize = arr.length - 1;

  // heapify subtree
  function _heapify(j) {
    const left = 2*j+1;
    const right = 2*j+2;
    let max = j;

    if (left < heapsize &&
        arr[left] > arr[max]) {
      max = left;
    }
    if (right < heapsize &&
        arr[right] > arr[max]) {
      max = right;
    }
    if (max !== j) {
      [arr[j], arr[max]] = [arr[max], arr[j]]; 
      _heapify(max);
    }
  }

  // build full heap
  for (var k=Math.floor(arr.length/2); k>=0; k--) {
    _heapify(k);
  }

  // sort heap
  for (var i=heapsize; i>=1; i--) {
    [arr[0], arr[i]] = [arr[i], arr[0]];

    heapsize -= 1;
    _heapify(0);
  }
  return arr;
}

export { Heap, Heapsort };
