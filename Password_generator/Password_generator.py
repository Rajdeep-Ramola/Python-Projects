import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','+','-','/','?',';',':','_']
nletters=int(input("How many letters do you want in password?\n"))
nsymbols=int(input("How many symbols do you want in password?\n"))
nnumbers=int(input("How many numbers do you want in password?\n"))
password_list=[]
for char in range(1,nletters+1):
    password_list+=random.choice(letters)
for char in range(1,nsymbols+1):
    password_list+=random.choice(symbols)
for char in range(1,nnumbers+1):
    password_list+=random.choice(numbers)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f"Password generated: {password}")
