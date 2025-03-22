def romanToInt(s):
  roman_int = {'I': 1, 'V': 5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
  total = 0
  i = 0
  while i < len(s):
    #kiểm tra trường hợp các số đặc biệt như 4,9,59,...
    if i < len(s) - 1 and roman_int[s[i+1]] > roman_int[s[i]]: 
      total += roman_int[s[i+1]] - roman_int[s[i]]
      i += 2 #bỏ qua kí tự tiếp theo vì đã xử lí cặp (vd 4 --> IV, nhảy qua kí tự V vì đã xử lí cặp với I)
    #xét các số ở trường hợp bình thường như 1,5,10...
    else:
      total += roman_int[s[i]]
      i += 1 #duyệt kí tự tiếp theo
  return total
#tránh dùng while, dùng for