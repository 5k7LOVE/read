#讀取檔案
#as(當作)
#.strip()把換行去掉，只能用字串

data = []

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
print(data[5])