def triangular_sum(nums):
  while len(nums) > 1: #xét cho vòng lặp chạy tới khi chỉ còn 1 phần tử
    newNums = []
    for i in range(len(nums) -1):
      newNums.append((nums[i] + nums[i+1])%10) #tính tổng rồi lấy phần dư 10
    nums = newNums #gán số mới vào để tiếp tục vòng lặp while cho đến khi thỏa điều kiện của vòng lặp while
  return nums[0] #trả về phần tử duy nhất còn lại