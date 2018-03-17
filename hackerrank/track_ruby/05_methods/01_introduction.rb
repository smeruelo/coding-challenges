#!/usr/bin/ruby
# https://www.hackerrank.com/domains/ruby/ruby-methods

def prime?(n)
  if n <= 2
    return n % 2 == 0
  else
    i = 2
    while i <= (Math.sqrt(n)).ceil
      if n % i == 0
        return false
      else
        i += 1
      end
    end
    return true
  end
end
