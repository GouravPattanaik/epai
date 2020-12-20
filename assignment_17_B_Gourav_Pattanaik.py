#1 write a program to reverse a list 
lst = [11, 5, 17, 18, 23]
def reverse(lst): 
    new_lst = lst[::-1] 
    return new_lst
	
#2 write a program to find sum of elements in list
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements in given list: ", total)

#3 write a program to find the largest number in a list 
list1 = [10, 20, 4, 45, 99] 
list1.sort() 
print("Largest element is:", list1[-1]) 

#4 write a program to print Even Numbers in a List 
list1 = [10, 21, 4, 45, 66, 93] 
for num in list1: 
    if num % 2 == 0: 
       print(num, end = " ") 
       
#5 write a program to print negative Numbers in given range 
start, end = -4, 19
for num in range(start, end + 1): 
    if num < 0: 
        print(num, end = " ") 
        
#6 write a program to remove empty List from List using list comprehension 
test_list = [5, 6, [], 3, [], [], 9] 
print("The original list is : " + str(test_list)) 
res = [ele for ele in test_list if ele != []] 
print ("List after empty list removal : " + str(res)) 

#7 write a  program to remove empty tuples from a list of tuples 
def Remove(tuples): 
    tuples = filter(None, tuples) 
    return tuples 
  
# Driver Code 
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),  
          ('krishna', 'akbar', '45'), ('',''),()] 
print Remove(tuples)

#8 write a program to break a list into chunks of size N
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
n = 4 
x = [l[i:i + n] for i in range(0, len(l), n)]  
print(x)

#9 write a program to find the frequency of words present in a string  
  
test_str = 'times of india times new india express'
print("The original string is : " + str(test_str)) 

res = {key: test_str.count(key) for key in test_str.split()} 
print("The words frequency : " + str(res))

#10 write a program to accept a string if it contains all vowels
def check(string): 
  if len(set(string).intersection("AEIOUaeiou"))>=5: 
    return ('accepted') 
  else: 
    return ("not accepted") 
  
if __name__=="__main__": 
  string="helloworld"
  print(check(string)) 
  

#11 write a program to rotate string left and right by d length  
def rotate(input,d):  
  
    Lfirst = input[0 : d]  
    Lsecond = input[d :]  
    Rfirst = input[0 : len(input)-d]  
    Rsecond = input[len(input)-d : ]  
  
    print ("Left Rotation : ", (Lsecond + Lfirst) ) 
    print ("Right Rotation : ", (Rsecond + Rfirst))  
  
if __name__ == "__main__":  
    input = 'helloworld'
    d=2
    rotate(input,d) 
    

#12 write a program to convert key-values list to flat dictionary 

from itertools import product 
test_dict = {'month' : [1, 2, 3], 
             'name' : ['Jan', 'Feb', 'March']} 
  
print("The original dictionary is : " + str(test_dict)) 
  
res = dict(zip(test_dict['month'], test_dict['name'])) 
print("Flattened dictionary : " + str(res)) 

# write a program to remove the duplicate words 
s = "Hello world Hello"
l = s.split() 
k = [] 
for i in l: 
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i) 
print(' '.join(k)) 


#13 write a program to convert into dictionary 
def Convert(tup, di): 
    for a, b in tup: 
        di.setdefault(a, []).append(b) 
    return di 
      
tups = [("A", 10), ("B", 20), ("C", 30),  
     ("D", 40), ("E", 50), ("F", 60)] 
dictionary = {} 
print (Convert(tups, dictionary)) 


#14 write program to extract digits from Tuple list 
from itertools import chain 
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)] 
print("The original list is : " + str(test_list)) 
temp = map(lambda ele: str(ele), chain.from_iterable(test_list)) 
res = set() 
for sub in temp: 
    for ele in sub: 
        res.add(ele) 
print("The extrated digits : " + str(res))  

#15 write a program to Remove Tuples of Length K Using list comprehension 
  
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
print("The original list : " + str(test_list)) 
K = 1
res = [ele for ele in test_list if len(ele) != K] 
print("Filtered list : " + str(res)) 

#16 write a program to find Maximum and Minimum K elements in Tuple 
test_tup = (5, 20, 3, 7, 6, 8) 
print("The original tuple is : " + str(test_tup)) 
K = 2
test_tup = list(test_tup) 
temp = sorted(test_tup) 
res = tuple(temp[:K] + temp[-K:]) 
print("The extracted values : " + str(res))  

#17 write a program to get current date and time 
import datetime  
current_time = datetime.datetime.now()  
    
print ("Time now at greenwich meridian is : " , end = "")  
print (current_time)

#18 write a program to convert time from 12 hour to 24 hour format 
  
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("08:05:45 PM"))   

#19 write a program to find the difference between two times 
  
  
# function to obtain the time in minutes form 
def difference(h1, m1, h2, m2): 
      
    # convert h1 : m1 into minutes 
    t1 = h1 * 60 + m1 
      
    # convert h2 : m2 into minutes  
    t2 = h2 * 60 + m2 
      
    if (t1 == t2):  
        print("Both are same times") 
        return 
    else: 
          
        # calculating the difference 
        diff = t2-t1 
          
    # calculating hours from difference 
    h = (int(diff / 60)) % 24
      
    # calculating minutes from difference 
    m = diff % 60
  
    print(h, ":", m) 
  
# Driver's code 
if __name__ == "__main__": 
      
    difference(7, 20, 9, 45) 
    difference(15, 23, 18, 54) 
    difference(16, 20, 16, 20) 
    
#20 write program to find yesterday, today and tomorrow 
  
# Import datetime and timedelta 
# class from datetime module 
from datetime import datetime, timedelta 
  
  
# Get today's date 
presentday = datetime.now() # or presentday = datetime.today() 
  
# Get Yesterday 
yesterday = presentday - timedelta(1) 
  
# Get Tomorrow 
tomorrow = presentday + timedelta(1) 
  
  
# strftime() is to format date according to 
# the need by converting them to string 
print("Yesterday = ", yesterday.strftime('%d-%m-%Y')) 
print("Today = ", presentday.strftime('%d-%m-%Y')) 
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y')) 

#21 write a program to remove all the characters except numbers and alphabets 
  
import re 
  
# initialising string 
ini_string = "123abcjw:, .@! eiw"
  
# printing initial string 
print ("initial string : ", ini_string) 
  
result = re.sub('[\W_]+', '', ini_string) 
  
# printing final string 
print ("final string", result) 

#22 write a program to merge dict using update() method
def Merge(dict1, dict2):
    return(dict2.update(dict1))
     
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
print(Merge(dict1, dict2))
print(dict2)

#23 write a program to print even length words in a string  
  
def printWords(s): 
    s = s.split(' ')  
    for word in s:  
        if len(word)%2==0: 
            print(word)  
# Driver Code  
s = "hello world" 
printWords(s)

#24 write a program to delete all duplicate letters in a string 

def removeDuplicate(str): 
    s=set(str) 
    s="".join(s) 
    print("Without Order:",s) 
    t="" 
    for i in str: 
        if(i in t): 
            pass
        else: 
            t=t+i 
        print("With Order:",t) 
      
str="helloworld"
removeDuplicate(str) 

#25 write a program to print Maximum frequency character in String 
  
# initializing string  
test_str = "Helloworld"
  
print ("The original string is : " + test_str) 
  
all_freq = {} 
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)  
  
print ("The maximum of all characters in Helloworld is : " + str(res)) 

#26 write a program to check if a string contains any special character 
  
import re 
def run(string): 
  
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
      
    if(regex.search(string) == None): 
        print("String is accepted") 
          
    else: 
        print("String is not accepted.") 
      
  
if __name__ == '__main__' : 
      
    # Enter the string 
    string = "Hello@World"
      
    # calling run function  
    run(string) 
    
#27 write a program to check if a string is binary or not 
def check(string) : 
    p = set(string) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        print("Yes") 
    else : 
        print("No") 
          
# driver code 
if __name__ == "__main__" : 
  
    string = "101010000111"
    check(string) 
   
#28 write a program to check whether a given string is Heterogram or not  
  
def heterogram(input): 
  
     alphabets = [ ch for ch in input if ( ord(ch) >= ord('a') and ord(ch) <= ord('z') )] 
  
     if len(set(alphabets))==len(alphabets): 
         print ('Yes') 
     else: 
         print ('No') 
  
# Driver program 
if __name__ == "__main__": 
    input = 'Hello World'
    heterogram(input) 

#29 write a program to check whether a given key already exists in a dictionary. 
  
def checkKey(dict, key): 
      
    if key in dict.keys(): 
        print("Present, ", end =" ") 
        print("value =", dict[key]) 
    else: 
        print("Not present") 
  
# Driver Code 
dict = {'a': 100, 'b':200, 'c':300} 
  
key = 'b'
checkKey(dict, key) 
  
key = 'w'
checkKey(dict, key) 

#30 write a program to check whether the string is a palindrome or not 
def isPalindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

#31 write a program that extract words starting with Vowel From A list
# initializing list 
test_list = ["have", "a", "good", "one"] 
  
# printing original list 
print("The original list is : " + str(test_list)) 
  
res = [] 
vow = "aeiou"
for sub in test_list: 
    flag = False
      
    # checking for begin char 
    for ele in vow: 
        if sub.startswith(ele): 
            flag = True 
            break
    if flag: 
        res.append(sub) 
  
# printing result  
print("The extracted words : " + str(res)) 

#32 write a program to replace vowels by next vowel using list comprehension + zip() 
  
test_str = 'helloworld'
print("The original string is : " + str(test_str)) 
vow = 'a e i o u'.split() 
temp = dict(zip(vow, vow[1:] + [vow[0]])) 
res = "".join([temp.get(ele, ele) for ele in test_str]) 
print("The replaced string : " + str(res)) 

#33 write a program to reverse words of string  
  
def rev_sentence(sentence):  
    words = sentence.split(' ')  
    reverse_sentence = ' '.join(reversed(words))  
    return reverse_sentence  
  
if __name__ == "__main__":  
    input = 'have a good day'
    print (rev_sentence(input)) 
    
#34 write a program to find the least Frequent Character in String 

test_str = "helloworld"
print ("The original string is : " + test_str) 
all_freq = {} 
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)  
  
print ("The minimum of all characters in the given word is : " + str(res)) 

#35 write a program to find the most frequent element in a list 
  
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 
  
List = [2, 1, 2, 2, 1, 3] 
print(most_frequent(List)) 

#36 write a program insert character after every character pair 
  
# initializing string  
test_str = "HellowWorld"

print("The original string is : " + test_str) 
res = ', '.join(test_str[i:i + 2] for i in range(0, len(test_str), 2)) 
 
print("The string after inserting comma after every character pair : " + res) 

#37 write a program to remove i-th indexed character from a string 
  
def remove(string, i):  
  
    a = string[ : i]  
    b = string[i + 1: ] 
    return a + b 
     
# Driver Code 
if __name__ == '__main__': 
      
    string = "HellowWorld"
      
    # Remove nth index element 
    i = 5
    
    # Print the new string 
    print(remove(string, i)) 

#38 write a program to check if a string has at least one letter and one number
def checkString(str): 
    
    flag_l = False
    flag_n = False
      
    for i in str: 
        
        # if string has letter 
        if i.isalpha(): 
            flag_l = True
  
        # if string has number 
        if i.isdigit(): 
            flag_n = True
      
    return flag_l and flag_n 
  
  
# driver code 
print(checkString('helloworld')) 
print(checkString('helloworld2020'))

#39 write a program extract least frequency element 

from collections import defaultdict 
test_list = [1, 3, 4, 5, 1, 3, 5] 
  
# printing original list  
print("The original list : " + str(test_list)) 
  
# Extract least frequency element 
res = defaultdict(int) 
for ele in test_list: 
   res[ele] += 1 
min_occ = 9999
for ele in res: 
    if min_occ > res[ele]: 
        min_occ = res[ele] 
        tar_ele = ele 
  
# printing result 
print("The minimum occurring element is : " + str(tar_ele)) 

#40 write a program to check 2 lists and find if any element is common
  
def common_data(list1, list2): 
    result = False
  
    for x in list1: 
  
        # traverse in the 2nd list 
        for y in list2: 
    
            # if one common 
            if x == y: 
                result = True
                return result  
                  
    return result 
      
# driver code 
a = [1, 2, 3, 4, 5] 
b = [5, 6, 7, 8, 9] 
print(common_data(a, b)) 
  
a = [1, 2, 3, 4, 5] 
b = [6, 7, 8, 9] 
print(common_data(a, b)) 

#41 write a program to find area of a triangle

a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
s = (a + b + c) / 2  
  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   

#42 write a program to swap two variables
x = input('Enter value of x: ')  
y = input('Enter value of y: ')  
  
temp = x  
x = y  
y = temp  
 
print('The value of x after swapping: {}'.format(x))  
print('The value of y after swapping: {}'.format(y)) 

#43 write a program to convert kilometers to miles

kilometers = float(input('How many kilometers?: '))  
conv_fac = 0.621371  
miles = kilometers * conv_fac  
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))  

#44 write a program to convert Celsius to Fahrenheit

celsius = float(input('Enter temperature in Celsius: '))  
fahrenheit = (celsius * 1.8) + 32  
print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))  

#45 write a program to display the calender

import calendar  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
  
print(calendar.month(yy,mm))  

#46 write a program to check if the year is a leap year

year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year))  
   
#47 write a program to check if the number is a prime numnber

num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  
   
#48 write a program to print all prime numbers between an interval

lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
           
#49 write a program to find the factorial of a number

num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       factorial = factorial*i  
   print("The factorial of",num,"is",factorial) 
   
#50 write a program to display the multiplication table of a number

num = int(input("Show the multiplication table of? "))  
# using for loop to iterate multiplication 10 times   
for i in range(1,11):  
   print(num,'x',i,'=',num*i)  
   
#51 write a program to print Fibonacci sequence

nterms = int(input("How many terms you want? "))  
# first two terms  
n1 = 0  
n2 = 1  
count = 2  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
elif nterms == 1:  
   print("Fibonacci sequence:")  
   print(n1)  
else:  
   print("Fibonacci sequence:")  
   print(n1,",",n2,end=', ')  
   while count < nterms:  
       nth = n1 + n2  
       print(nth,end=' , ')  
       # update values  
       n1 = n2  
       n2 = nth  
       count += 1  
       
#52 write a program to check Armstrong number

num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
   
#53 write a program to find Armstrong number in an interval

lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)  
            
#54 write a  program to find the sum of natural numbers

num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   # use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  

#55 write a  program to find LCM

def lcm(x, y):  
   if x > y:  
       greater = x  
   else:  
       greater = y  
  while(True):  
       if((greater % x == 0) and (greater % y == 0)):  
           lcm = greater  
           break  
       greater += 1  
   return lcm  
  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2)) 

#56 write a  program to find HCF

def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))  

#57 write a  program to convert decimal to binary, octal and hexadecimal
dec = int(input("Enter a decimal number: "))  
  
print(bin(dec),"in binary.")  
print(oct(dec),"in octal.")  
print(hex(dec),"in hexadecimal."  

#58 python program to find ascii value of a character

c = input("Enter a character: ")  
print("The ASCII value of '" + c + "' is",ord(c))

#59 write a program to make a simple calculator

# define functions  
def add(x, y):  
   """This function adds two numbers"""
   return x + y 
def subtract(x, y): 
   """This function subtracts two numbers""" 
   return x - y 
def multiply(x, y): 
   """This function multiplies two numbers""" 
   return x * y 
def divide(x, y): 
   """This function divides two numbers"""  
   return x / y  
# take input from the user  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")    
   
#60 write a  program to sort words in alphabetic order

my_str = input("Enter a string: ")  
# breakdown the string into a list of words  
words = my_str.split()  
# sort the list  
words.sort()  
# display the sorted words  
for word in words:  
   print(word)  
   
#61 write a program to print the elements of an array present on even position
arr = [1, 2, 3, 4, 5];     
     
print("Elements of given array present on even position: ");    
    
for i in range(1, len(arr), 2):    
    print(arr[i]);   
    
#62 write a program to sort the elements of the array

arr = [5, 2, 8, 7, 1];     
temp = 0;    
print("Elements of original array: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");    
     
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ");   
    
#63 write a program to check if the given number is a disarium number

def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
num = 175;    
rem = sum = 0;    
len = calculateLength(num);    
     
n = num;    
     
while(num > 0):    
    rem = num%10;    
    sum = sum + int(rem**len);    
    num = num//10;    
    len = len - 1;    
     
if(sum == n):    
    print(str(n) + " is a disarium number");    
else:    
    print(str(n) + " is not a disarium number");   
    
#64 write a program to print all disarium numbers between 1 and 100

def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
   
def sumOfDigits(num):    
    rem = sum = 0;    
    len = calculateLength(num);    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     
print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):    
    result = sumOfDigits(i);    
        
    if(result == i):    
        print(i),  
        
#65 write a program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)  

#66 write a program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)  

#67 write a program to multiply two matrices using nested loops


X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(X)):

   for j in range(len(Y[0])):

       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)   
   
#68 write a program to remove punctuation from a string 

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)

#69 write a program to shuffle a deck of card

import itertools, random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)

print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
   
#70 write a program to display the powers of 2 using anonymous function

terms = 10
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])

#71 write a program to add 2 binary numbers

num1 = '00001'
num2 = '10001'

sum = bin(int(num1,2) + int(num2,2))
print(sum)

#71 write a program to find simple interest 

p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))

# calculating simple interest
si = (p*r*t)/100

# printing the values
print("Principle amount: ", p)
print("Interest rate   : ", r)
print("Time in years   : ", t)
print("Simple Interest : ", si)

#72 write a program to find compound interest 

p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time in the years: "))

# calculating compound interest
ci =  p * (pow((1 + r / 100), t)) 

# printing the values
print("Principle amount  : ", p)
print("Interest rate     : ", r)
print("Time in years     : ", t)
print("compound Interest : ", ci)

#73 write a program to print a pattern of stars (*)

for row in range (0,5):
    for column in range (0, row+1):
        print ("*", end="")

    # ending row
    print('\r')
    
#74 write a program to return the absolute value in Python

def get_absolute_value(n):
	if n >= 0:
		return n
	else:
		return -n

print(get_absolute_value(101))

#75 write a program to find the power of a number

a = 10
b = 3

result = a**b

print (a, " to the power of ", b, " is = ", result)

#76 write a program to print the binary value of the numbers from 1 to N

n = int(input("Enter the value of N: "))

for i in range(1, n+1):
    print("Binary value of ", i, " is: ", bin(i))
    
#77 write a program to find number of bits necessary to represent an integer in binary

num = int(input("Enter an integer number: "))

bits = num.bit_length()

print("bits required to store ", num, " = ", bits)
print("binary value of ", num, " is = ", bin(num))

#78 write a program to find the difference between 2 lists

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 30, 60, 70]

print "list1:", list1
print "list2:", list2

print "Difference elements:"
print (list (set(list1) - set (list2)))

#79 write a program to add an element at specified index in a list

list = [10, 20, 30]
print (list)
list.insert (1, "ABC")
print (list)
list.insert (3, "PQR")
print (list)

#80 write a program to print EVEN length words of a string 
str = "Python is a programming language"

words = list(str.split(' '))

print "str: ", str
print "list converted string: ", words
print "EVEN length words:"
for W in words:
	if(len(W)%2==0 ):
		print W
        
#81 write a program to create N copies of a given string 

str1 = "Hello"
n = 3

str2 = str1 * 3 

print "str1: ", str1 
print "str2: ", str2

#82 write a program to extract the mobile number from the given string in Python

# importing the module
import re

# string
string='''hello you can call me at 018002089898.'''

# extracting the mobile number
Phonenumber=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d')
m=Phonenumber.search(string)

# printing the result 
print('mobile number found from the string : ',m.group())

#83 write a program to Capitalizes the first letter of each word in a string

def capitalize(text):
  return text.title()

str1 = "Hello world!"
str2 = "hello world!"
str3 = "HELLO WORLD!"
str4 = "includehelp.com is a tutorials site"

print("str1: ", str1)
print("str2: ", str2)
print("str3: ", str3)
print("str4: ", str4)
print()

#84 write a program to design a dice throw function

import random

def dice():
    return random.choice([1,2,3,4,5,6])
    
#85 write a program to print perfect numbers from the given list of integers

def checkPerfectNum(n) :
	i = 2;sum = 1;

	while(i <= n//2 ) :
		if (n % i == 0) :
			sum += i			
		
		i += 1
		if sum == n :
			print(n,end=' ')

if __name__ == "__main__" :

	print("Enter list of integers: ")
	list_of_intgers = list(map(int,input().split()))

	print("Given list of integers:",list_of_intgers)

	print("Perfect numbers present in the list is: ")
	for num in list_of_intgers :
		checkPerfectNum(num)
        
#86 write a program to convert meters into yards
num = float(input("Enter the distance measured in centimeter : "))

inc = num/2.54 
print("Distance in inch : ", inc)

#87 write a program Tower of Hanoi 

def hanoi(x):
    global repN
    repN += 1
    if x == 1:
        return 2
    
    else:
        return 3*hanoi(x-1) + 2
    
x = int(input("ENTER THE NUMBER OF DISKS: "))

global repN
repN =0

print('NUMBER OF STEPS: ', hanoi(x), ' :', repN)

#88 write a program to find variance of a dataset

def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot = tot + (x - mean)**2
    return tot/len(X)

# main code
#  a simple data-set 
sample = [1, 2, 3, 4, 5] 
print("variance of the sample is: ", variance(sample))

#89 write a program to find winner of the day

def find_winner_of_the_day(*match_tuple):
    team1_count = 0
    team2_count = 0
     
    for team_name in match_tuple :
         
        if team_name == "Team1" :
            team1_count += 1
        else :
            team2_count += 1
             
    if team1_count == team2_count :
        return "Tie"
         
    elif team1_count > team2_count :
        return "Team1"
     
    else :
        return "Team2"
     
     
if __name__ == "__main__" :
     
    print(find_winner_of_the_day("Team1","Team2","Team1"))
    print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
    print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
    
#90 write a program for swapping the value of two integers without third variable

x = int(input("Enter the value of x :"))
y = int(input("Enter the value of y :"))

(x,y) = (y,x)

print('Value of x: ', x, '\nValue of y: ', y, '\nWOO!! Values SWAPPEDDD')

#91 write a program to check eligibility for voting

# input age
age = int(input("Enter Age : "))

if age>=18:
        status="Eligible"
else:
    status="Not Eligible"

print("You are ",status," for Vote.")

#92 write a program to print the version information

import sys

print("Python version: ", sys.version)
print("Python version info: ", sys.version_info)

#93 write a program to find sum of all digits of a number

def sumDigits(num):
  if num == 0:
    return 0
  else:
    return num % 10 + sumDigits(int(num / 10))

x = 0
print("Number: ", x)
print("Sum of digits: ", sumDigits(x))
print()

#94 write a program to print double quotes with the string variable
str1 = "Hello world";

print("\"%s\"" % str1)
print('"%s"' % str1)
print('"{}"'.format(str1))

#95 write a program to Remove leading zeros from an IP address

import re
def removeLeadingZeros(ip):
    modified_ip = re.sub(regex, '.', ip)
    print(modified_ip)


if __name__ == '__main__' : 
	
	ip = "216.08.094.196"
	removeLeadingZeros(ip)

#96 write a program for binary search

def binary_search(l, num_find):

    start = 0
    end = len(l) - 1
    mid = (start + end) // 2
    
    found = False
    position = -1

    while start <= end:
        if l[mid] == num_find:
            found = True
            position = mid
            break
        
        if num_find > l[mid]:
            start = mid + 1
            mid = (start + end) // 2
        else:
            end = mid - 1
            mid = (start + end) // 2

    return (found, position)

if __name__=='__main__':
    
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 6
    found = binary_search(l, num)
    if found[0]:
        print('Number %d found at position %d'%(num, found[1]+1))
    else:
        print('Number %d not found'%num)
        
#97 write a program to copy odd lines of one file to another file

file1 = open('file1.txt', 'r') 
file2 = open('file2.txt', 'w') 

lines = file1.readlines() 
type(lines) 
for i in range(0, len(lines)): 
	if(i % 2 != 0): 
		file2.write(lines[i]) 

file1.close()
file2.close() 

file1 = open('file1.txt', 'r') 
file2 = open('file2.txt', 'r') 

str1 = file1.read()
str2 = file2.read()

print("file1 content...")
print(str1)

print() # to print new line

print("file2 content...")
print(str2)

file1.close()
file2.close()

#98 write a program to reverse a string that contains digits in Python

def reverse(n):
    s=str(n) 
    p=s[::-1]
    return p 

num = int(input('Enter a positive value: '))
print('The reverse integer:',reverse(num))

#99 write a program to input a string and find total number uppercase and lowercase letters

print("Input a string: ")
str1 = input()

no_of_ucase, no_of_lcase = 0,0

for c in str1:
    if c>='A' and c<='Z':
        no_of_ucase += 1
    if c>='a' and c<='z':
        no_of_lcase += 1

print("Input string is: ", str1)
print("Total number of uppercase letters: ", no_of_ucase)
print("Total number of lowercase letters: ", no_of_lcase)

#100 write a program to input a string and find total number of letters and digits

print("Input a string: ")
str1 = input()

no_of_letters, no_of_digits = 0,0

for c in str1:
    if (c>='a' and c<='z') or (c>='A' and c<='Z'):
        no_of_letters += 1
    if c>='0' and c<='9':
        no_of_digits += 1

print("Input string is: ", str1)
print("Total number of letters: ", no_of_letters)
print("Total number of digits: ", no_of_digits)