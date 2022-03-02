defmodule TreeNode do
  @type t :: %__MODULE__{
          val: integer,
          left: TreeNode.t() | nil,
          right: TreeNode.t() | nil
        }
  defstruct val: 0, left: nil, right: nil
end

defmodule InvertBinaryTree do
  @moduledoc """
  Given the root of a binary tree, invert the tree, and return its root.
  Input: root = [4,2,7,1,3,6,9]
  Output: [4,7,2,9,6,3,1]

  Example 2:
  Input: root = [2,1,3]
  Output: [2,3,1]

  Example 3:
  Input: root = []
  Output: []

  Constraints:
  The number of nodes in the tree is in the range [0, 100].
  -100 <= Node.val <= 100
  """

  @spec invert_tree(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def invert_tree(root) do
    traverse(root)
  end

  defp traverse(nil), do: nil
  defp traverse(%TreeNode{} = node) do
    %TreeNode{
      left: traverse(node.right),
      right: traverse(node.left),
      val: node.val
    }
  end

  @spec invert_tree([integer()] | []) :: [integer()] | []
  def invert_flat_tree(input) do
    acc = %{
      index: 1,
      stack: [],
      inverted_tree: []
    }
    result = Enum.reduce(input, acc, &assign_node/2)
    Enum.concat(result.inverted_tree, result.stack)
  end

  defp assign_node(value, %{index: index, stack: stack, inverted_tree: inverted_tree}) do
    # if we're on a new level - if index + 1 == 2^n - flush the stack
    if index == 1 || :math.ceil(:math.log2(index)) == :math.log2(index) do
      %{
        index: index + 1,
        stack: [value],
        inverted_tree: Enum.concat(inverted_tree, stack)
      }
    else
      # otherwise, build stack
      %{
        index: index + 1,
        stack: [value | stack],
        inverted_tree: inverted_tree
      }
    end
  end
end
