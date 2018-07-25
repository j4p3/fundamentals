function longestChain(chain) {

  const _isLeaf = (blockIndex) => !chain.includes(blockIndex);

  const _walkChain = (index, stack) => {
    stack.push(index);
    if (chain[index] === -1) {
      return stack;
    }
    return _walkChain(chain[index], stack);
  }

  const chains = chain
    .map((block, i) => _isLeaf(i) ? i : null)
    .filter(blockIndex => blockIndex)
    .map(blockIndex => {
      if (_isLeaf(blockIndex)) {
        return _walkChain(blockIndex, [])
      }
  });

  const longest = chains.reduce((acc, cv) => cv.length > acc.length ? cv : acc)
  console.log(longest);
  return longest;
}

export { longestChain };
