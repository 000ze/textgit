import re
content='This (百度)www.baidu.com'
print(len(content))
result=re.search('\(百度\)www\.(.*)\.com',content,re.S)
print(result)
print(result.group(1))

