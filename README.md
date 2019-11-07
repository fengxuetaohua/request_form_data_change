# request_form_data_change
loadrunner中使用web_submit_data()函数时，对于"Name=advanceDiscount", "Value= 0", ENDITEM,此类参数都需要从网站请求报文中的formdata中一点点复制粘贴，特别繁琐，
所以我编写了一个python程序，将网站请求报文中的formdata中的数据，例如，原网站请求报文中的formdata中的数据是：
advanceDiscount: 0
depart: Denver
departDate: 10/15/2019
arrive: Denver
returnDate: 10/16/2019
将其复制粘贴到本工程目录下的original_data .txt文件中，然后运行该cf.py文件，则在工程目录下直接生成result_data.txt文件，以上述内容为例，生成的result_data.txt文件为：
"Name=advanceDiscount", "Value= 0", ENDITEM,
"Name=depart", "Value= Denver", ENDITEM,
"Name=departDate", "Value= 10/15/2019", ENDITEM,
"Name=arrive", "Value= Denver", ENDITEM,
"Name=returnDate", "Value= 10/16/2019", ENDITEM,
因此，可将上述result_data.txt文件内容直接粘贴到web_submit_data()函数中需要的位置处。
