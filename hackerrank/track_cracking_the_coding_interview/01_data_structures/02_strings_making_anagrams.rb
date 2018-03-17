#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

# O(n)
def string_to_dict(s)
  h = Hash.new(0)
  (0...s.length).each {|i| h[s[i]] += 1}
  return h
end

# O(n)
def how_many(a, b)
  dict_a = string_to_dict(a)
  dict_b = string_to_dict(b)
  count = 0
  dict_a.each do |k, v|
    count += (v - dict_b[k]).abs
    dict_b.delete(k)
  end
  dict_b.each {|k, v| count += v}
  return count
end


a = gets.strip.downcase
b = gets.strip.downcase
puts how_many(a, b)
