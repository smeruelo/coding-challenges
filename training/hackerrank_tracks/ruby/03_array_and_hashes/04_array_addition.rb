#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-array-addition/problem

def end_arr_add(arr, element)
  arr.push(element)
  arr
end

def begin_arr_add(arr, element)
  arr.unshift(element)
  arr
end

def index_arr_add(arr, index, element)
  arr.insert(index, element)
  arr
end

def index_arr_multiple_add(arr, index)
  arr.insert(index, 3, 13)
  arr
end
