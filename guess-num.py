import random

r = random.randint(1, 100)
count = 0
while True:
	num = input('請猜數字：')
	num = int(num)
	count += 1
	if num == r:
		print('猜對了！')
		print('你總共猜了', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')