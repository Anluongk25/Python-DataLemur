def intersection(a, b):
  intersection = [] #list rỗng để chứa số trùng lặp
  for num in a:
    if num in b and num not in intersection:
    
      intersection.append(num)
  return intersection
