man=[]
other=[]
try:
     date=open('split_text.txt')
     for each_line in date:
        if each_line.find(':')!=-1:
            (role,line_spoken)=each_line.split(':',1)  # 这是一个元组，1是指定

            if role=='Man':
                 line_spoken = line_spoken.upper()  # upper()用于清空空格
                 man.append(line_spoken)

            elif role=='Other man':
                 line_spoken = line_spoken.upper()  # strip()用于清空空格
                 other.append(line_spoken)
        else:
            print('type error')

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

