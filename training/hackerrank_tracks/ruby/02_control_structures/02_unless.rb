#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-tutorial-unless/problem

def scoring(array)
  array.each do |user|
    unless user.is_admin?
      user.update_score
    end
  end
end
