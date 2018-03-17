#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-enumerable-introduction/problem

def iterate_colors(colors)
  arr = Array.new
  colors.each do |color|
    arr.push(color)
  end
  arr
end
