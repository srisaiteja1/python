str1=input("enter 1st string: ")
str2=input("enter 2nd string: ")
print(sorted(str1),sorted(str2))
if(sorted(str1)==sorted(str2)):
    print("the given strings are anagrams")
else:
    print("the given strings are not anagrams")