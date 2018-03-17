#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-blocks/problem

def factorial(n)
  accum = 1
  while n > 1
    accum *= n
    n -= 1
  end
  yield(accum)

end

n = gets.to_i
factorial(n) do |f|
    puts f
end
