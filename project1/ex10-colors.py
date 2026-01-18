color = 'a'
for i in range(0,8):
	for j in range(0,2):
		code = 30 + i
		print(f'\x1b[{j};{code}mColor {i}')

print(f'\x1b[0mdone')
