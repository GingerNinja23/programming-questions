'''
This follows from Game of Thrones - I.

Now that the king knows how to find out whether a given word has an anagram 
which is a palindrome or not, he encounters another challenge. He realizes that
there can be more than one palindrome anagrams for a given word. Can you help
him find out how many palindrome anagrams are possible for a given word ?

The king has many words. For each given word, he needs to find out the number 
of palindrome anagrams of the string. As the number of anagrams can be large,
the king needs the number of anagrams % (109+ 7).

Input format :
A single line which contains the input string

Output format : 
A single line which contains the number of anagram strings which are palindrome % (109 + 7).

Constraints : 
1<=length of string <= 10^5 
Each character of the string is a lowercase alphabet. 
Each test case has at least 1 anagram which is a palindrome.

Sample Input 01 :

aaabbbb
Sample Output 01 :

3 
Explanation : 
Three palindrome permutations of the given string are abbabba , bbaaabb and bababab.

Sample Input 02 :

cdcdcdcdeeeef
Sample Output 02 :

90
'''
import math
def getAnswer(word):
    string = list(word)
    found = True
    middle_occured = False
    num_pairs = 0
    lst = {}
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
            num_pairs += 1
            val = string.index(char)
            string.pop(val)
            if(lst.get(char)):
                lst[char] += 1
            else:
                
                lst[char] = 1
    if(found):
        answer = math.factorial(num_pairs)
        for key in lst:
            answer = answer/math.factorial(lst[key])
    else:
        answer = 0
                
    return answer%1000000007
 
    
def main():
  word = raw_input()
  print getAnswer(word)  

if __name__ == '__main__':
  main()