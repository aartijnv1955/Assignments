##n=int(input())
def isPalindrome(s):
    return s==s[::-1]
s=input()
if isPalindrome(s):
    print("YES")
else:
    print("NO")