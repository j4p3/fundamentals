

class Node {
  constructor(key) {
    this.key = key || null;
    this.p = null;
    this.rSibling = null;
    this.lChild = null;
  }
}

class BinaryNode {
  constructor(key) {
    this.key = key;
    this.p = null;
    this.left = null;
    this.right = null;
  }

  height() {
    return Math.max(
      this.left ? this.left.height() + 1 : 0,
      this.right? this.right.height() + 1 : 0
    );
  }

  size() {
    return (
      1 +
      (this.left ? this.left.size() : 0) +
      (this.right ? this.right.size() : 0)
    );
  }

  leaf() {
    return !(this.left || this.right);
  }
}

class Tree {
  constructor(root) {
    this.root = new Node();
  }
}


class BinaryTree {
  constructor(root) {
    this.root = new BinaryNode(root);
  }

  size() {
    return this.root.size();
  }

  traverseInOrder() {
    const a = [];
    function _inOrder(node) {
      if (!node) return;
      _inOrder(node.left);
      a.push(node.key);
      _inOrder(node.right);
    }
    _inOrder(this.root);
    return a;
  }

  traversePreOrder() {
    const a = [];
    function _preOrder(node) {
      if (!node) return;
      a.push(node.key);
      _preOrder(node.left);
      _preOrder(node.right);
    }
    _preOrder(this.root);
    return a;
  }

  traversePostOrder() {
    const a = [];
    function _postOrder(node) {
      if (!node) return;
      _postOrder(node.left);
      _postOrder(node.right);
      a.push(node.key);
    }
    _postOrder(this.root);
    return a;
  }
}

class BinarySearchTree extends BinaryTree {
  insert(key, node) {
    if (!this.root) {
      this.root = new BinaryNode(key);
    }

    node = node || this.root;

    if (key < node.key) {
      if (!node.left) {
        const newNode = new BinaryNode(key);
        newNode.p = node;
        node.left = newNode;
        return;
      }
      this.insert(key, node.left);
      return; // break to avoid executing below
    }

    // use above break instead of conditional to avoid another check in loop
    if (!node.right) {
      const newNode = new BinaryNode(key);
      newNode.p = node;
      node.right = newNode;
      return;
    }
    this.insert(key, node.right);
  }

  search(key, node) {
    node = node || this.root;
    if (key === node.key) {
      return node;
    } else if (key < node.key) {
      return this.search(key, node.left);
    } else {
      return this.search(key, node.right);
    }
  }

  searchIterative(key, node = this.root) {
    while (node && key !== node.key) {
      if (key < node.key) {
        node = node.left;
      } else {
        node = node.right;
      }
    }
    return node;
  }

  delete(key, node = this.root) {
    // @todo node deletion that preserves child nodes
    // need successor method
    // splice out node, find successor, etc
    // v. easy to find successor - just take minimum of right child
    // or, if no right child, walk up tree until node is no longer in right subtree
    node = this.search(key, node);

    if (!node) {
      return null;
    }

    if (!node.p) {
      this.root = null;
      return node;
    }
    
    if (key === node.p.left.key) {
      node.p.left = null;
      return node;
    }

    node.p.right = null;
    return node;
  }

  minimum(node = this.root) {
    if (!node) return null;
    if (!node.left) return node.key;
    return this.minimum(node.left);
  }

  minimumIterative(node = this.root) {
    while (node.left) {
      node = node.left;
    }
    return node.key;
  }

  maximum(node = this.root) {
    if (!node) return null;
    if (!node.right) return node.key;
    return this.maximum(node.right);
  }

  maximumIterative(node = this.root) {
    while (node.right) {
      node = node.right;
    }
    return node.key;
  }
}

class RedBlackNode extends BinaryNode {
  constructor(key) {
    super(key);
    this.color = null;
  }
}

class RedBlackTree extends BinarySearchTree {
  // @todo: when to know how to rotate?
  // @todo: when to assign color? is it purely theoretical?
  constructor(root) {
    super(root);
    this.root = new RedBlackNode(root);
    this.root.color = 'black';
  }

  lRotate(node) {
    const swap = node.right;

    // reassign subtree
    node.right = swap.left;
    if (swap.left) {
      swap.left.p = node;
    }

    // reassign parent pointers
    swap.p = node.p;
    if (!node.p) {
      this.root = swap;
    } else {
      if (Object.is(node.p.left, node)) {
        node.p.left = swap;
      } else {
        node.p.right = swap
      }
    }

    // reassign nodes' pointers
    swap.left = node;
    node.p = swap;
  }

  rRotate(node) {
    const swap = node.left;

    // reassign subtree
    node.left = swap.right;
    if (swap.right) {
      swap.right.p = node;
    }

    // reassign parent pointers
    swap.p = node.p;
    if (!node.p) {
      this.root = swap;
    } else {
      if (Object.is(node.p.left, node)) {
        node.p.left = swap;
      } else {
        node.p.right = swap
      }
    }

    // reassign nodes' pointers
    swap.right = node;
    node.p = swap;
  }

  insertFixup(node) {
    // @todo - comprehend three cases of insert-fixup
    // how have we violated red-black properties?
    // did we make the make the root red? only if inserting root.
    // did we insert a red node on a red child? probably.
    // loop over our chain of red nodes, flipping their parents black, rotating left or right as necessary while they've still got red parents.
    let parent;
    let grandparent;
    let uncle;
    console.log(`fixing up node ${node.key}`)

    while (node.p && node.p.color == 'red') {
      console.log(`while:`)
      console.log(node);
      parent = node.p;
      if (parent && !Object.is(parent, this.root)) {
        grandparent = parent.p;
        uncle = Object.is(parent, grandparent.left) ?
          grandparent.right :
          grandparent.left;
        if (uncle && uncle.color == 'red') {
          // case 1
          parent.color = 'black';
          uncle.color = 'black';
          grandparent.color = 'red';
          node = grandparent;
        } else if (parent && uncle) {
          if (Object.is(node, parent.right)) {
            node = parent;
            this.lRotate(node);
          }
          parent.color = 'black';
          grandparent.color = 'red';
          this.rRotate(grandparent)
        }
      }
    }

    // while loop with pointers not particularly well suited to JS.
    // possible to do this with a few conditions.
  }

  insert(key, node = this.root) {
    console.log(`inserting key ${key}`)
    if (!node.key) {
      node.key = key;
      return node;
    }

    if (key > node.key) {
      if (!node.right) {
        const newNode = new RedBlackNode(key);
        newNode.color = 'red';
        newNode.p = node;
        node.right = newNode;

        this.insertFixup(newNode);
        return newNode;
      }
      return this.insert(key, node.right);
    }

    if (!node.left) {
      const newNode = new RedBlackNode(key);
      newNode.color = 'red';
      newNode.p = node;
      node.left = newNode;

      this.insertFixup(newNode);
      return newNode;
    }
    return this.insert(key, node.left);
  }

  insertIterative(key) {
    const newNode = new RedBlackNode(key);
    newNode.color = 'red';

    let node = this.root;
    let prev = node;

    while (node) {
      prev = node;
      if (key > node.key) {
        node = node.right;
      } else {
        node = node.left;
      }
    }
    if (key > prev.key) {
      prev.right = newNode;
    } else {
      prev.left = newNode;
    }
    newNode.p = prev;

    this.insertFixup(newNode);
    return newNode;
  }
}

export { Node, BinaryNode, Tree, BinaryTree, BinarySearchTree, RedBlackTree };