#contents of document.txt
#list = ["1abc2",
#"pqr3stu8vwx",
#"a1b2c3d4e5f",
#"treb7uchet"]

with open ("input.txt", "r") as f:
     lines = f.readlines()

def get_first_num(string):
        for index, value in enumerate(string):
            if value.isdigit()==True:
                return string[index]
            
def get_last_num(string):
     for index,value in enumerate(string[::-1]):
        if value.isdigit() ==True:
            return string[(len(string)- index -1)]

total = 0

for line in lines:
     first = get_first_num(line)
     last = get_last_num(line)
     composite = first+last
     total += int(composite)

print(total)  
