#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

# O(n)
def string_lst_to_dict(l)
  h = Hash.new(0)
  (0...l.length).each {|i| h[l[i]] += 1}
  return h
end

# O(n)
def possible_ransom?(magazine, note)
  magazine_dict = string_lst_to_dict(magazine)
  note_dict = string_lst_to_dict(note)
  note_dict.each {|word, count| return "No" if magazine_dict[word] < count}
  return "Yes"
end


_ = gets
magazine = gets.strip.split(' ')
note = gets.strip.split(' ')
puts possible_ransom?(magazine, note)
