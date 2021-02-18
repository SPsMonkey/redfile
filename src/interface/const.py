
padx=1
pady=5

names="张三 李四  老五  杨程亮     李光名"
Names = names.split()
# 把姓名分成2名一组，名字中间用空格隔开
groupname = []
for i in range(0, len(Names), 2):
    groupname.append(Names[i:i + 2])
#找到第一列名字最长长度
max1=0
for name in groupname:
    if len(name[0])>max1:
        max1=len(name[0])
#找到第二列名字最长长度
max2=0
for name in groupname:
    if len(name)==2:
        if len(name[1])>max2:
            max2=len(name[1])
#插入空格使得名字对齐
for name in groupname:
    n=max1-len(name[0])
    name[0]=name[0]+n*"　"
    if len(name)==2:
        n=max2-len(name[1])
        name[1]=name[1]+n*"　"
for i in range(0,len(groupname)):
    if len(groupname[i])==2:
        groupname[i]=groupname[i][0]+"　"+groupname[i][1]
    else:
        groupname[i]=groupname[i][0]

print (groupname)