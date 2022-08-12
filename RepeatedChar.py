

# Method that return count of the
# given character in the string
def count(string, character):

    # Count variable
    res = 0

    for i in range(len(string)):

        # Checking character in string
        if (string[i] == character):
            res = res + 1
    return res


# Driver code
str = "beekeeper."
c = 'e'
print(count(str, c))
