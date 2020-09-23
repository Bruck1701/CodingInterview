
def fizzBuzz(n):
    # Write your code here
	for i in range(1,n+1):
		if i%3==0 and i%5==0:
			print("FizzBuzz")
		elif i%3==0 and i%5!=0:
			print("Fizz")
		elif i%3!=0 and i%5==0:
			print("Buzz")
		else:
			print(i)



if __name__ == '__main__':
	fizzBuzz(15)