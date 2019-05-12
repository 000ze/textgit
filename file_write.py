
man=[]
other=[]
try:
     date=open('split_text.txt')
     for each_line in date:
        if each_line.find(':')!=-1:
            (role,line_spoken)=each_line.split(':',1)  # 这是一个元组，1是指定
            line_spoken=line_spoken.strip() #strip()用于清空空格
            if role=='Man':
                 man.append(line_spoken)
                 man.append()
            elif role=='Other man':
                 other.append(line_spoken)
                 other.append('\n')
        else:
            print('error')

     date.close()
except:
    pass
    print('Sorry,there is an error')
try:
    man_file=open('man_data.txt','w')
    other_file=open('other_date.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print('file error')


