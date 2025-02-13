def factorial(n):
  if n == 0 or n == 1:
     return 1 #trường hợp đặc biệt 0!, 1! = 1
  return n * factorial(n-1) 
  
  
