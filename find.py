import openpyxl

#file1='./test_data/IM_message.xlsx'
#file2='./test_data/Mido_Copywrite.xlsx'
excel1=openpyxl.open("./test_data/IM_message.xlsx")
excel2=openpyxl.open("./test_data/Mido_write.xlsx")
def read(a,index):
    for sheet in a.sheetnames:
        a_t=a[sheet]
        for v1 in a_t.values:
            return v1[index]
result1=read(excel1,3)
result2=read(excel2,0)
if result1==result2:
    print(result1)
else:
    print('没有相同的数据')



