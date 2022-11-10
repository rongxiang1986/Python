import sys
import traceback


def raise_test():
    # raise IOError("异常生成测试")
    raise


try:
    raise_test()
    print("test")
except IOError as e:
    print(e)
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback)

finally:
    pass


