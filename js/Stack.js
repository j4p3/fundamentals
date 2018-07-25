
class Stack {
  constructor(props) {
    this.els = [];
  }

  push(el) {
    return this.els.push(el);
  }

  pop() {
    return this.els.pop();
  }

  search(key) {
    for (var i in this.els) {
      if (this.els[i] === key) return i
    }
    return -1;
  }
}

class Queue {
  constructor(props) {
    this.els = [];
  }

  enqueue(el) {
    return this.els.push(el);
  }

  dequeue() {
    return this.els.shift();
  }

  search(key) {
    for (var i in this.els) {
      if (this.els[i] === key) return i
    }
    return -1;
  }
}

export { Stack, Queue };