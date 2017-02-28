def isHarshad(num):
  num_string = str(num)
  num_list = list(num_string)
  num_int_list = []
  num_sum = 0
  for x in num_list:
    num_sum += int(x)
  num_result = num/num_sum
  if num_result == round(num_result): 
    return True
  else:
    return False

harshad_numbers = []  

for num in range(1, 1000):
  if isHarshad(num) == True:
    harshad_numbers.append(num)

print(harshad_numbers)