#!/usr/bin/ruby
# https://www.hackerrank.com/challenges/ruby-methods-keyword-arguments/problem

def convert_temp(temp, input_scale: 'celsius', output_scale: 'celsius')
  # convert to celsius first
  case input_scale
  when 'kelvin'
    intermediate = temp - 273.15
  when 'fahrenheit'
    intermediate = (temp - 32.0) * 5/9
  when 'celsius'
    intermediate = temp
  end

  case output_scale
  when 'kelvin'
    output = intermediate + 273.15
  when 'fahrenheit'
    output = (intermediate * 9/5) + 32.0
  when 'celsius'
    output = intermediate
  end

  return output
end

puts convert_temp(0, output_scale: 'kelvin')
puts convert_temp(0, input_scale: 'celsius', output_scale: 'fahrenheit')
