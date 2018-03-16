#!/usr/bin/ruby
#https://www.hackerrank.com/contests/womens-codesprint-5/challenges/recycled-number

def rotate(n)
  aux = n.to_s
  size = aux.length - 1
  minimum = aux
  size.times do
    aux = aux[-1] + aux[0...size]
    minimum = aux if aux.to_i < minimum.to_i
  end
  return minimum
end

def dict_count(arr)
  dict = Hash.new(0)
  arr.each {|i| dict[i] += 1}
  return dict
end

def uniqueRecycledPairs(arr)
  arr.uniq!
  rotated = arr.map {|a| rotate(a)}
  repetitions = dict_count(rotated)
  pairs = 0
  repetitions.each {|k, v| pairs += v * (v - 1) / 2 if v > 1}
  return pairs
end

# Some test cases
# puts uniqueRecycledPairs ["10", "1", "13", "31", "23", "32"].map(&:to_i)
# puts uniqueRecycledPairs [10, 10]
# puts uniqueRecycledPairs [10]
# puts ''
