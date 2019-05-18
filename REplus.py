import re

content='7df7fd8fy9aerew9d8sf'
result=re.sub('\d+','',content)
pattern=re.compile('\d+')
result2=re.sub(pattern,'',content)
print(result)
print(result2)