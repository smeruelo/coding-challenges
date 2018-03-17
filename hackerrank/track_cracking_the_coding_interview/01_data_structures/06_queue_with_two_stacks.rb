#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

# Two stacks: one to enqueue in (e), one to dequeue from (d)
# we enqueue into stack e
# when we need to dequeue and d is empty, we fill it with the contents of e

class Fifo
  def initialize
    @e = []
    @d = []
  end

  # O(1)
  def enqueue(n)
    @e.push(n)
  end

  # Amortized O(1)
  def dequeue
    if @d.length == 0
      @e.length.times {@d.push(@e.pop)}
    end
    @d.pop
  end

  def print_top
    if @d.length == 0
      puts @e[0]
    else
      puts @d[-1]
    end
  end

  def to_s
    @e.reverse.join(' ') + ' ' + @d.join(' ')
  end
end

queue = Fifo.new
gets.to_i.times do
  query = gets.split().map(&:to_i)
  case query[0]
  when 1; queue.enqueue(query[1])
  when 2; queue.dequeue
  when 3; queue.print_top
  end
end
