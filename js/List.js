
class Node {
  constructor(key) {
    this.key = key;
    this.next = null;
    this.prev = null;
  }
}


class DoublyLinkedList {
  constructor(props) {
    props = props || {};
    this.sentinel = new Node(null);
    this.sentinel.next = this.sentinel;
    this.sentinel.prev = this.sentinel;
  }

  insert(key) {
    console.log(`inserting key ${key}`);
    const prevFirstNode = this.sentinel.next;
    const newFirstNode = new Node(key);
    console.log(newFirstNode);
    newFirstNode.prev = this.sentinel;
    newFirstNode.next = prevFirstNode;
    this.sentinel.next = newFirstNode;
    return newFirstNode;
  }

  append(key) {
    console.log(`appending key ${key}`);
    const prevLastNode = this.sentinel.prev;
    const newLastNode = new Node(key);
    newLastNode.next = this.sentinel;
    newLastNode.prev = prevLastNode;
    this.sentinel.prev = newLastNode;
    return newLastNode;
  }

  search(key) {
    let node = this.sentinel.next;
    while (node.key !== null && node.key !== key) {
      node = node.next;
    }
    return node;
  }
}


export { Node, DoublyLinkedList };
