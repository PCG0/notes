#!/usr/local/bin/lua


--以只读（r）方式打开文件
file = io.open("test.txt", 'r')
--设置输入文件为 NewLuaFile.lua
io.input(file)
--输出
print(io.read(-1))
--关闭文件
io.close(file)
