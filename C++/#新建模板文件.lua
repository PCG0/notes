#!/usr/local/bin/lua

function exgest(file)
   local f = io.open(file, "w")
   io.output(f)
   io.write("#include <bits/stdc++.h>\nusing namespace std;\n")
   io.close(f)
end

exgest("example.cpp")