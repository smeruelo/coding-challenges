#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-methods-variable-arguments/problem

def full_name(first, *rest)
  first + ' ' + rest.join(' ')
end
