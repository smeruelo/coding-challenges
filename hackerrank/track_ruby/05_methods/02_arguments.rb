#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-methods-arguments/problem


def take(arr, num_elements = 1)
  arr[num_elements...arr.length]
end
