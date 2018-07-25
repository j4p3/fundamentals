const Colors = {
  RED: 1,
  BLACK: 2,
}


class Node {
  // interesting thing about this table: no parents
  constructor(key, data, left, right, color) {
    this._key = key || null;
    this._data = data || null;
    this._left = left || null;
    this._right = right || null;
    this._color = color || null;
  }

  get key() { return this._key; }
  set key(key) { this._key = key; }
  get data() { return this._data; }
  set data(data) { this._data = data; }
  get left() { return this._left; }
  set left(left) { this._left = left; }
  get right() { return this._right; }
  set right(right) { this._right = right; }
  get color() { return this._color; }
  set color(color) { this._color = color; }

  inspect() {
    return this.key;
  }

  isRed() {
    return this._color === Colors.RED;
  }

  toggleColor() {
   if (this._color === Colors.RED) {
    this._color = Colors.BLACK;
   } else {
    this._color = Colors.RED;
   }
  }
}

class RBTree {
  constructor() {
    this._root = null;
  }

  insert(key, data) {
    console.log(`inserting key ${key}`);
    console.log(`current root is ${this._root ? this._root.key : this._root}`);
    // isn't this root reassignment going to fuck up the tree order?
    this._root = this._insert(key, data, this._root);
    this._root.color = Colors.BLACK;
    console.log(`new root is ${this._root.key}\n`);
    return this._root;
  }

  get(key) {
    this._get(this._root, key);
  }

  traverse() {
    // in-order traversal
    const nodes = [];
    function _inOrder(node) {
      if (!node) return;
      _inOrder(node.left);
      nodes.push(`${node.key}: ${node.color}`);
      _inOrder(node.right);
    }
    _inOrder(this._root);
    return nodes;
  }

  levelTraverse() {
    // breadth-first traversal
    const queue = [];
    const nodes = [];

    if (this._root) {
      queue.push(this._root);
    } else {
      nodes.push[null];
    }

    while (queue.length !== 0) {
      let tmp = queue.shift();
      nodes.push(`${tmp.key}: ${tmp.color}`);
      if (tmp.left) {
        queue.push(tmp.left);
      }
      if (tmp.right) {
        queue.push(tmp.right);
      }
    }
    return nodes;
  }

  isRed(node) {
    if (node === null) {
      return false;
    }
    return node.isRed();
  }

  _get(node, key) {
    if (node === null) {
      return null;
    }

    if (node.key === key) {
      return node
    }

    if (node.key > key) {
      return this._get(node.left, key)
    } else {
      return this._get(node.right, key)
    }
  }

  _insert(key, data, node) {
    // recursively traverse tree until null, then insert (or update data)
    let newRoot = node;

    if (node === null) {
      return new Node(key, data, null, null, Colors.RED);
    }

    if (node.key > key) {
      node.left = this._insert(key, data, node.left);
    } else if (node.key < key) {
      node.right = this._insert(key, data, node.right)
    } else {
      node.data = data;
    }

    // Post-insertion fixup, running on the parent of the inserted node, which is interesting
    // on initial run: this runs on root. we've just inserted a red 10 to the right of a black 5.
    // left isred is null & this evaluates to false
    // lrotate on root? ok
    // how is this not a recursive process? hown can we guarantee we'll run this just once?
    // it's already a recursive function. we're running those code on every node from root to here.

    if (this.isRed(node.right) && !this.isRed(node.left)) {
      // right child red (just inserted), left child black
      newRoot = this._rotateLeft(node);
    }
    if (this.isRed(node.left) && this.isRed(node.left.left)) {
      // left child red, left grandchild red
      newRoot = this._rotateRight(node);
    }
    if (this.isRed(node.left) && this.isRed(node.right)) {
      // both children red
      this._toggleColors(node);
    }

    return newRoot;
  }

  _toggleColors(node) {
    // why not flip color of parent as well? isn't parent red?
    // because it's always set to black after this operation?
    node.left.toggleColor();
    node.right.toggleColor();
  }

  _rotateLeft(node) {
    let y = node.right;
    if (y !== null) {
      node.right = y.left;
      y.left = node;
      y.color = node.color;
      node.color = Colors.RED;
    }
    return y;
  }

  _rotateRight(node) {
    let x = node.left;
    if (x !== null) {
      node.left = x.right;
      x.right = node;
      x.color = node.color;
      node.color = Colors.RED;
    }
    return x;
  }
}

export { RBTree };
