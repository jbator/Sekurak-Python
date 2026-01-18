# not sure if this correct answer for the ex 10
# just print base standard terminal colors codes 
# in its color on the terminal
# and bold version of it

for i in range(0,8):
	for j in range(0,2):
		code = 30 + i
		print(f'\x1b[{j};{code}mColor {i}')

# reset terminal color back to defaults
print(f'\x1b[0mdone')
