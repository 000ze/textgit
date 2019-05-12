try:
     date=open('split_text.txt')
     for each_line in date:
        if each_line.find(':')!=-1:
            (role,line_spoken)=each_line.split(':',1)  # 这是一个元组，1是指定
            print(' ')
            print(role,end=" ")
            print('said:',end=" ")
            print(line_spoken,end=" ")
     date.close()
except:
    pass
    print('Sorry,there is an error')