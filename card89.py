number = input("Please enter a card number: ")
card_number = list(number.strip())
cvv=int(input("Please enter a cvv:"))
string = input("Enter your name: ")
count1=len(number)

        

# Remove the last digit from the card number
check_digit = card_number.pop()

# Reverse the order of the remaining numbers
card_number.reverse()

processed_digits = []

for index, digit in enumerate(card_number):
	if index % 2 == 0:
		doubled_digit = int(digit) * 2

		# Subtract 9 from any results that are greater than 9		
		if doubled_digit > 9:
			doubled_digit = doubled_digit - 9

		processed_digits.append(doubled_digit)
	else:
		processed_digits.append(int(digit))

total = int(check_digit) + sum(processed_digits)

# Verify that the sum of the digits is divisible by 10
if(count1<13):
        print("Invalid Card Number")
elif (total % 10 == 0):
	print("Valid card number")
else:
	print("Invalid card number")

count=0
while(cvv>0):
    count=count+1
    cvv=cvv//10
if (count==3 or count==4):
        print("Valid CVV")
else:
        print("Invalid CVV")


if all(x.isalpha() or x.isspace() for x in string):
    print("Valid name")
else:
    print("Invalid name")

	
