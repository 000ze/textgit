date=open('split_text.txt')
for each_line in date:
    try:
        (role,line_spoken)=each_line.split(':') # 这是一个元组，1是指定‘:’。
        print(' ')
        print(role,end=" ")
        print('said:',end=" ")
        print(line_spoken,end=" ")
    except:
        pass
date.close()