// import { DoublyLinkedList } from './List';

// const l = new DoublyLinkedList();
// l.insert(5);
// l.insert(6);
// l.append(12);
// l.insert(22);
// l.append(1);

// console.log(l); 
// let node = l.sentinel.next;
// while (node.key !== null) {
//   console.log(node.key);
//   node = node.next;
// }
// console.log(l.search(6));
// console.log(l.search(99));

// import { Stack, Queue } from './Stack';

// const q = new Queue();

// q.enqueue(1);
// q.enqueue(3);
// q.enqueue(8);
// q.enqueue(7);
// q.enqueue(2);

// console.log(q.search(23));

// import { Node, BinaryNode, Tree, BinaryTree, BinarySearchTree, RedBlackTree } from './Tree';

// const insertRandom = (node) => {
//   // @todo crazy mutability/pointer problem here
//   console.log('creating children for node ' + node.key)
//   node.left = new BinaryNode(Math.floor(Math.random()*50));
//   node.left.p = node;
//   node.right = new BinaryNode(Math.floor(Math.random()*50));
//   node.right.p = node;
// }

// const t = new BinaryTree(5);
// let pointer = t.root;
// pointer.left = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer.right = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer = pointer.left;
// pointer.left = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer.right = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer = pointer.left;
// pointer.left = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer.right = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer = pointer.p;
// pointer = pointer.right;
// pointer.left = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer.right = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer = pointer.p;
// pointer = pointer.p;
// pointer = pointer.right;
// pointer.left = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer.right = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer = pointer.left;
// pointer.left = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});
// pointer.right = new BinaryNode({p: pointer,key: Math.floor(Math.random()*50)});

// const ino = t.traverseInOrder();
// const pre = t.traversePreOrder();
// const post = t.traversePostOrder();

// console.log(ino);
// console.log(pre);
// console.log(post);

// const t = new BinarySearchTree(Math.floor(Math.random()*300));
// for (var i=0;i<200;i++) {
//   t.insert(Math.floor(Math.random()*300))
// }

// t.insert(99);

// // const ino = t.traverseInOrder();
// // const pre = t.traversePreOrder();
// // const post = t.traversePostOrder();

// // console.log(ino);
// // console.log(pre);
// // console.log(post);

// console.log(t.search(99));
// console.log(t.searchIterative(99));
// console.log(t.size());
// console.log(t.minimum());
// console.log(t.minimumIterative());
// console.log(t.maximum());
// console.log(t.maximumIterative());


// const rb = new RedBlackTree(5);

// for (var i=0;i<10;i++) {
//   let node = rb.insertIterative(Math.floor(Math.random()*30))
// }

// let ino = rb.traverseInOrder();
// console.log(ino);

// rb.insert(12);

// ino = rb.traverseInOrder();
// console.log(ino);

// import { RBTree } from './RedBlackTree';

// const rbt = new RBTree();

// rbt.insert(5, {foo: 'bar'});
// rbt.insert(10, {foo: 'baz'});
// rbt.insert(15, {foo: 'baz'});
// rbt.insert(1, {foo: 'baz'});
// rbt.insert(115, {foo: 'baz'});
// rbt.insert(25, {foo: 'baz'});
// rbt.insert(5, {foo: 'baz'});
// for (let i=0;i<50;i++) {
//   rbt.insert(Math.floor(Math.random()*100), {idx: i});
// }
// console.log(rbt.traverse());
// console.log(rbt.levelTraverse());


// import { HashTable } from './HashTable';

// const ht = new HashTable();

// // console.log(ht.hashCode(50));

// ht.insert(5, { foo: 'bar' });
// ht.insert(10, { baz: 'qux' }, 10);
// ht.insert(30, { fee: 'zil' }, 10);
// ht.insert(50, { fee: 'zil' }, 10);
// for (let i=0;i<500;i++) {
//   ht.insert(Math.floor(Math.random()*100), {idx: i});
// }

// console.log(ht.get(5));
// console.log(ht.get(10));
// console.log(ht.get(55));
// console.log(ht.get(105));

// ht.slots.forEach(slot => {
//   console.log(slot);
// });

import { Heap, Heapsort } from './Heap';

const heap = new Heap();
const arr = [];
for (let i=0;i<18;i++) {
  arr.push(Math.floor(Math.random()*50));
}
heap.buildHeap(arr);
console.log(heap._heap);

const sorted = heap.heapsort();
console.log(sorted);

const functionallySorted = Heapsort(arr);
console.log(functionallySorted);


