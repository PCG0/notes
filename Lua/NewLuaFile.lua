#!/usr/local/bin/lua


require "socket"
function sleep(sec)
    socket.select(nil, nil, sec)
end

function Num(num1, num2)
	if num1 > num2 then 
		result = num1;
	else 
		result = num2; 
	end
	return result;
end

print("两值比较最大值为 ",Num(10,4))
print("两值比较最大值为 ",Num(5,6))


myprint = function(param)
   print("这是打印函数 -   ##",param,"##")
end

function add(num1,num2,functionPrint)
   result = num1 + num2
   -- 调用传递的函数参数
   functionPrint(result)
end
myprint(10)
-- myprint 函数作为参数传递
add(2,0,myprint)