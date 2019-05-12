try:
    data=open('u.txt')
    print(date.readline(),end=' ')

except IOError as err:
    print('file error'+str(err))
finally:
    if data in locals():
        data.close()


