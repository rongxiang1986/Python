
import cgitb
cgitb.enable(format='text')

f = open("test.txt", "r")
f.write("写入内容")
f.close()