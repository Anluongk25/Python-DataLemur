def fizz_buzz_sum(target):
  sum = 0 
  for i in range (target):
    if i%3 == 0 or i%5 == 0: #xét số i đó có chia hết cho 3 hoặc chia hết cho 5 không
      sum += i #nếu thỏa điều kiện cộng số đó vào tổng
  return sum 
