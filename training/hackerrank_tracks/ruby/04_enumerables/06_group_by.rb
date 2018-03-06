#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-enumerable-group-by/problem

def group_by_marks(marks, pass_marks)
  marks.group_by {|k, v| if v < pass_marks then "Failed" else "Passed" end}
end
