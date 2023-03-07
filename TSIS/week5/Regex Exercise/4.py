import re
with open(r'C:\Dauekel\python\TSIS\week5\row.txt',encoding='utf-8') as file:
    content= file.read()
result=re.findall("^[A-Z][a-z]+",content)
print(result)