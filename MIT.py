'''
x = int(input('Enter an integter: '))
ans = 0
while ans**3 < abs(x):
	ans = ans + 1
	print(ans)
if ans**3 != abs(x):
    print(x, 'is not a cube')
else:
    if x <0:
        ans =-ans
    print('cube root of', x, 'is', ans)
'''
'''
max = int(input('Enter a positive integer: '))
i = 0
while i < max:
    i += 1
print(i)
'''
'''Find the cube 
root of a perfect cube
'''
x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while ans(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
print('numGuesses =', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(ans, 'is clost to square root of', x)
