def check(str, pattern):
    if re.search(pattern, str):
        return True
    else:
        return False


def newCheck(str, pattern):
    for i in str.lower():
        if i not in pattern.lower():
            return False
            return True


# _driver code
str1 = input()
str2 = input()
# pattern = re.compile('[str2]')
if newCheck(str1, str2):
    print("Input string is valid")
else:
    print("Input string is not valid")
    print(str1)
