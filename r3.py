#讀取檔案并將內容存進空清單
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

#將清單內容以空格切割，并印出
for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	message = s[1:]
	print(time, name, message)


