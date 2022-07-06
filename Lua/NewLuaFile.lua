#!/usr/local/bin/lua

-- local str=io.read("*a")
-- file = io.open("test1.txt", 'w')
-- io.input(file)-- 设置输入文件为 NewLuaFile.lua
-- io.write(str)
-- io.flush()
-- io.close()

function exgest(file)
   local f = io.open(file, "w")
   io.output(f)
   io.write("#include <bits/stdc++.h>\nusing namespace std;\n")
   io.close(f)
end

exgest("example.cpp")