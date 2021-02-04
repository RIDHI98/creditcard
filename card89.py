


def check_name(name):

    for character in name:

        if not (character.isalpha() or character == ' '):

            print("Name can only contain alphabets and spaces!")

            return False

    return True


def check_card(card_number):
    luhn_sum = 0
    even_dig = False

    for i in reversed(range(len(card_number))):
        d = int(card_number[i])
        if even_dig:
            d *= 2
        luhn_sum += (d // 10 + d % 10)

        even_dig = not even_dig
    if luhn_sum % 10 == 0:
        return True
    print("Invalid Card Number!")
    return False


def check_cvv(cvv):
    if 100 < cvv < 10000:
        return True
    print("Invalid CVV!")
    return False

def valid(user_info):
    return "Successfully validated card details" if check_name(user_info['user_name']) and check_card(
        user_info['card_number']) and check_cvv(int(user_info['cvv']))  else "Try Again!"


if __name__ == "__main__":
    user_info = {'user_name': input("Enter name: "),
                 'card_number': input("Card number: "),
                 'cvv': input("CVV: ")}
    print(valid(user_info))


	
