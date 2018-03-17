#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

# In place and O(n^2)
def shift_in_place(a, d)
  d.times do
    aux = a[0]
    (0...a.length-1).each {|i| a[i] = a[i+1]}
    a[a.length-1] = aux
  end
end

# New array, O(n)
def shift(a, d)
  shifted = a[d..a.length]
  (0...d).each {|i| shifted.push(a[i])}
  return shifted
end

n, d = gets.strip.split(' ').map(&:to_i)
a = gets.strip.split(' ').map(&:to_i)
puts shift(a, d).join(' ')
