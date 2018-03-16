#!/usr/bin/ruby
# https://www.hackerrank.com/contests/womens-codesprint-5/challenges/easy-change

def howMuchToAsk(c, p)
  bills = [20, 50, 100, 200, 500, 1000]
  if bills.include?(p - c)
    return 0
  else
    aux = bills.select {|bill| bill - p + c > 0 and bill - p + c < 10}
    if aux != [] then return aux.first - p + c else -1 end
  end
end

# fp = File.open(ENV['OUTPUT_PATH'], 'w')
# t = gets.to_i
# t.times do |t_itr|
#     cp = gets.rstrip.split
#     c = cp[0].to_i
#     p = cp[1].to_i
#     result = howMuchToAsk c, p
#     fp.write result
#     fp.write "\n"
# end
# fp.close()
