import os
"""
实现的功能：
将类似于下面格式
    advanceDiscount: 0
    depart: Denver
    .cgifields: roundtrip
转换为：
    "Name=advanceDiscount", "Value=0", ENDITEM,
    "Name=depart", "Value=Denver", ENDITEM,
     "Name=.cgifields", "Value=roundtrip", ENDITEM,
"""


# 1 将original_data.txt文件中的数据读取出来
def read_data(file):
    # 打开txt文件流
    with open(file, "r", encoding="utf-8") as f:
        # 通过文件流调用读取的方法读取数据--->所有行
        data_list = f.readlines()
        # 新建列表 --》添加分割后的单行列表数据，lines存放读取的数据
        lines = []
        # 遍历
        for data in data_list:
            '''
            strip():去除字符串前后回车
            split():使用指定符号进行分割字符串并以列表格式返回分割后的数据
            '''
            # 把分割后的单行列表数据添加到整体的列中，并返回
            lines.append(data.strip().split(":"))
        # 如果txt文档第一行是标题，则可以从第二行开始返回，list每个元素为文件的一行数据，每个元素里又有n个元素，为文件一行的n个数据
        return lines[0:]


# 2 读取original_data.txt文件后，转换成需要的格式
def change_form():
    # 运行结果格式：[['depart', ' Denver'], ['departDate', ' 10/15/2019'],...]
    line_list = read_data("original_data .txt")
    lines = []
    # 遍历
    for data in line_list:
        # 例如['depart', ' Denver'],转为["Name=depart", "Value=Denver", ENDITEM,]
        str1 = '"'+'Name='+data[0]+'", "'+'Value='+data[1]+'", '+'ENDITEM,\n'
        lines.append(str1)
    return lines[0:]


# 3 将转换后的数据写入文件中
def write_file():
    with open("result_data.txt","w",encoding="utf-8") as f:
        line_list=change_form()
        for data in line_list:
            f.write(str(data))
    # 自动打开结果文件
    os.startfile("result_data.txt")



"""
    f.read() #读取所有数据，不适合有大量数据的txt文档
    f.readline() # 读取单行
    f.readlines() # 读取所有行，不适合有大量数据的txt文档
"""

if __name__ == '__main__':
    print(write_file())






