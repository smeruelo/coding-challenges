#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

class Node
  attr_accessor :data, :left, :right
  def initialize(data, left: nil, right: nil)
    @data = data
    @left = left
    @right = right
  end
end

O(n)
def check_subtree(node)
  min_subtree = max_subtree = node.data
  bst_subtree = true
  if node.left != nil
    bst_left, min_left, max_left = check_subtree(node.left)
    bst_subtree = bst_left && max_left < node.data
    min_subtree = [min_left, min_subtree].min
    max_subtree = [max_left, max_subtree].max
  end
  if node.right != nil
    bst_right, min_right, max_right = check_subtree(node.right)
    bst_subtree = bst_right && bst_subtree && min_right > node.data
    min_subtree = [min_right, min_subtree].min
    max_subtree = [max_right, max_subtree].max
  end
  return [bst_subtree, min_subtree, max_subtree]
end

def checkBST?(root)
  if root == nil
    return true
  else
    return check_subtree(root)[0]
  end
end


yes = Node.new(3, left: Node.new(2, left: Node.new(1)),
                  right: Node.new(6, left: Node.new(4, right: Node.new(5)),
                                     right: Node.new(7)))
no1 = Node.new(3, left: Node.new(2, left: Node.new(1)),
                  right: Node.new(6, left: Node.new(4, right: Node.new(3)),
                                     right: Node.new(7)))
no2 = Node.new(5, left: Node.new(2, left: Node.new(1), right: Node.new(3)),
                  right: Node.new(6, left: Node.new(4), right: Node.new(7)))

puts "#{checkBST?(yes)}, true"
puts "#{checkBST?(no1)}, false"
puts "#{checkBST?(no2)}, false"
puts "#{checkBST?(nil)}, true"

