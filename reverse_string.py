# short recursive Python function that takes a character string s and outputs its reverse. For example, the reverse of pots&pans would be snap&stop .
def reverse_string(data):
    if len(data) ==2:
        return data[1] + data[0]
    elif len(data) ==1:
        return data[0]
    else:
        return data[len(data)-1] + reverse_string(data[1:len(data)-1])+data[0]
print reverse_string(' pots&pans')
