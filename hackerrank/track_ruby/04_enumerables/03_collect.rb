#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-enumerable-collect/problem

def rot13(secret_messages)
  def rot13_char(char)
    if char.ord.between?(65, 90)
      (65 + (char.ord + 13 - 65) % 26).chr
    elsif char.ord.between?(97, 122)
      (97 + (char.ord + 13 - 97) % 26).chr
    else
      char
    end
  end

  secret_messages.map do |word|
    encoded = ""
    (0...word.length).each do |i|
      encoded += rot13_char(word[i])
    end
    encoded
  end
end
