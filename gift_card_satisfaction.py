def max_satisfaction(expectations, cards):
  expectations.sort()
  cards.sort()
  a = 0 #pointer for expectations
  b = 0 #pointer for cards
  while a < len(expectations) and b < len(cards):
    if cards[b] >= expectations[a]:
      a += 1
    b +=1
  return a
   