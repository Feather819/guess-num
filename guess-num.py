import random

start = input('請決定數字範圍的開始值：')
start = int(start)
end = input('請決定數字範圍的結束值：')
end = int(end)
r = random.randint(start, end)
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