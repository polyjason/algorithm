#Write a short recursive Python function that determines if a string s is a
#palindrome, that is, it is equal to its reverse. For example, racecar and
#gohangasalamiimalasagnahog are palindromes.
def is_palindrome(data):
    if len(data) == 1:
        return True
    elif len(data) ==2:
        return data[0] == data[1]
    else:
        if data[0] !=data[len(data)-1]:
            return False
        else:
            return is_palindrome(data[1:len(data)-1])
print is_palindrome('abbsdfa')
