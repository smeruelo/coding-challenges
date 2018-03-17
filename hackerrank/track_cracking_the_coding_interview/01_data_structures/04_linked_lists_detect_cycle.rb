#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

class Node
  attr_accessor :data, :next
  def initialize(data: nil, next_node: nil)
    @data = data
    @next = next_node
  end
end

# O(n)
def has_cycle?(head)
  # Two pointers, p1 advances one node at a time, p2 two nodes
  # If there's a cycle, they'll eventually meet
  p1 = p2 = head
  while p1 and p2
    p1 = p1.next
    if p2.next
      p2 = p2.next.next
    else
      p2 = nil
    end
    return true if p1 and p1 == p2
  end
  return false
end
