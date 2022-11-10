import sys
import traceback


f = open("test.txt", "r")

try:
    f.write("写入内容")
except IOError as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback)

else:
    print("写入文件成功")
finally:
    f.close()