import { longestChain } from './Blockchain';

test('evaluates to true', () => {
  const testChain = [6,7,1,2,2,1,5,-1,0,6];
  expect(longestChain(testChain).length).toBe(6);
});
