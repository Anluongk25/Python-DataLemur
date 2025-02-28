def compound_interest(principal, rate, contribution, years):
  total = principal
  for year in range(years):
    print(f"Year {year + 1}: Current total is {total}")
    total += total * (rate/100) + contribution 
    round_total = round(total,2)
    
  return round_total