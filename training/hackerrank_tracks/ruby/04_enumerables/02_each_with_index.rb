#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-enumerable-each-with-index/problem

def skip_animals(animals, skip)
  arr = Array.new
  animals.each_with_index do |item, index|
    if index >= skip
      arr.push("#{index}:#{item}")
    end
  end
  arr
end
