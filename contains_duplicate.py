def contains_duplicate(input):
  
  for i in range(len(input)-1):
    for j in range(i+1, len(input)):
      if(input[i] == input[j]):
        return True
  return False