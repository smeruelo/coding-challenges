#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

def counterpart(c)
  case c
  when '('; ')'
  when '{'; '}'
  when '['; ']'
  end
end

# O(n)
def balanced?(s)
  opened = []
  i = 0
  while i < s.length
    case s[i]
    when '(', '{', '['
      opened.push(s[i])
    when ')', '}', ']'
      return false if counterpart(opened.pop) != s[i]
    end
    i += 1
  end
  return opened == []
end


gets.to_i.times {if balanced?(gets) then puts 'YES' else puts 'NO' end}
