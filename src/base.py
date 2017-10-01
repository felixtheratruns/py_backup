import sys
import inspect

def exit(*args):
    print('Exiting . . . because:')
    print(*args)
    callerframerecord = inspect.stack()[1]    # 0 represents this line
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    print(info.filename)                       # __FILE__     -> Test.py
    print(info.function)                       # __FUNCTION__ -> Main
    print(info.lineno)                         # __LINE__     -> 13
    sys.exit()
 
