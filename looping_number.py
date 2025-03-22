def sum_of_squares(n):
	#trả về tổng bình phương của số trước đó (vd: 4^2 = 16 , số tiếp theo sẽ là 1^2 + 6^2 = 37)
  return sum(int(digit) ** 2 for digit in str(n))
#phần kiểm tra xem nó có là số lặp không
def is_looping_num(n):
  seen = set() #tập hợp để lưu value đã xuất hiện
  while n!=1:
    if n in seen:
      return True
    seen.add(n) #lưu số hiện tại để kiểm tra cho lần sau
    n = sum_of_squares(n) #tính tổng bình phương của số hiện tại
  return False