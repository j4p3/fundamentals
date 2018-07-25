class Node {
  constructor(key, value) {
    this.key = key || null;
    this.value = value || null;
    this.next = undefined;
    this.prev = undefined;
  }
}

class HashTable {
  constructor() {
    this.slots = [];
    this.maxSize = 100;
  }

  hashCode(val) {
    var i;
    var hashCode = 0;
    var character;
    // If value to be hashed is already an integer, return it.
    if (val.length === 0 || val.length === undefined) {
      return val;
    }
    for (i = 0; i < val.length; i += 1) {
      character = val.charCodeAt(i);
      /*jshint -W016 */
      hashCode = ((hashCode << 5) - hashCode) + character;
      hashCode = hashCode & hashCode;
      /*jshint -W016 */
    }
    return hashCode;
  };

  insert(key, value, hashCode) {
    const node = new Node(key, value);

    // allow manual hashcode set for testing
    if (hashCode) {
      hashCode = this.hashCode(hashCode);
    } else {
      hashCode = this.hashCode(key);
    }
    hashCode = hashCode % this.maxSize;

    if (this.slots[hashCode] === undefined) {
      this.slots[hashCode] = node;
      return node;
    }

    if (this.slots[hashCode].key === key) {
      this.slots[hashCode].value = value;
      return node;
    }

    let p = this.slots[hashCode];
    while (p.next !== undefined) {
      p = p.next;
    }
    p.next = node;
    node.prev = p;
    return node;
  }

  get(key) {
    const hashCode = this.hashCode(key) % this.maxSize;
    if (this.slots[hashCode] === undefined) {
      return undefined;
    }
    if (
      this.slots[hashCode].next === undefined &&
      this.slots[hashCode].key === key) {
      return this.slots[hashCode].value;
    }

    let p = this.slots[hashCode];

    while (
      p !== undefined &&
      p.next !== undefined &&
      p.key !== key
    ) {
      p = p.next;
    }

    if (p.key === key) {
      return p;
    }

    return undefined;
  }
}

export { HashTable };
