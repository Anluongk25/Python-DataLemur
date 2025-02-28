def another_one(digits):
  for i in range(len(digits)-1,-1,-1):
    if digits[i] <9:
      digits[i] += 1
      return digits
    else:
      digits[i] = 0
      
  return [1] + digits #không được ghi digits + [1] vì như vậy sẽ bị làm tròn ngược (vd: [9,9] --> [0,0,1] trong khi đúng là [1,0,0])
	
	    