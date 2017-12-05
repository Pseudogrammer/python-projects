import math



# Problem 2. Palindromes
#
# Given a string, determine if the string is a palindrome.
#
# Examples:
#     palindrome('anna')  returns 'True'
#     palindrome('abcdef')  returns 'False'
#     palindrome('')  returns 'True'

def palindrome(word):
    n=len(word)
    if n==1:
        return True
    elif n % 2 == 0:
        return word[n-1:int(n/2-1):-1]==word[:int(n/2)]
    else:
        return word[n-1:int((n-1)/2):-1]==word[:int((n+1)/2)]

def test(got, expected):
    score = 0
    if got == expected:
        score = 3.33
        print(" OK ", end=" ")
    else:
        print(" XX ", end=" ")
    print("Got: ", got, "Expected: ", expected)
    return score



def main():
    total = 0
    print()
    print('Task C: palindromes. ' """Each OK is worth five points.""")

    #  If this is what you get, you are good to go. Each OK is worth five points.
    # OK  Got:  True Expected:  True
    # OK  Got:  False Expected:  False
    # OK  Got:  True Expected:  True

    total += test(palindrome('anna'), True)
    total += test(palindrome('bookkeeper'), False)
    total += test(palindrome('a'), True)

    print("You final score is: ", math.ceil(total))


if __name__ == '__main__':
    main()
