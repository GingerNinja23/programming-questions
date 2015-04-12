'''
Dothraki are planning an attack to usurp King Robert's throne. King Robert 
learns of this conspiracy from Raven and plans to lock the single door 
through which the enemy can enter his kingdom.

But, to lock the door he needs a key that is an anagram of a certain
palindrome string.The king has a string composed of lowercase English
letters. Help him figure out whether any anagram of the string can be
a palindrome or not.

Input Format:
A single line which contains the input string.

Constraints :
1≤ length of string ≤105 
Each character of the string is a lowercase English letter.

Output Format :
A single line which contains YES or NO in uppercase.

Sample Input : 01

aaabbbb

Sample Output : 01

YES

Explanation 
A palindrome permutation of the given string is bbaaabb. 

Sample Input : 02

cdefghmnopqrstuvw
Sample Output : 02

NO
Explanation 
You can verify that the given string has no palindrome permutation. 

Sample Input : 03

cdcdcdcdeeeef
Sample Output : 03

YES
Explanation 
A palindrome permutation of the given string is ddcceefeeccdd

'''
string = list(raw_input())
 
found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
middle_occured = False
while(len(string)>1):
    char = string.pop(0)
    val_exist = False
    try:
        string.index(char)
        val_exist = True
    except:
        val_exist = False
    if( not val_exist and middle_occured):
        found = False
        break
    elif(not val_exist and not middle_occured):
        middle_occured = True
    else:
        string.pop(string.index(char))

if not found:
    print("NO")
else:
    print("YES")