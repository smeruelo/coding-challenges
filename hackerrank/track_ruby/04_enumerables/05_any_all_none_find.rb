#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-enumerable-any-all-none-find/problem

def func_any(hash)
  hash.any? {|k, v| k.is_a?(Integer)}
end

def func_all(hash)
  hash.all? {|k, v| v.is_a?(Integer) and v < 10}
end

def func_none(hash)
  hash.none? {|k, v| v == nil}
end

def func_find(hash)
  hash.find {|k, v| (k.is_a?(Integer) and v.is_a?(Integer) and v < 20) or
             (k.is_a?(String) and v.is_a?(String) and v.start_with?("a"))}
end
