import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)


# 查找最新生成的测试报告
def get_new_file(files):
    lists = os.listdir(files)
    lists.sort(key=lambda fn: os.path.getmtime(files+fn))
    file_ = os.path.join(files, lists[-1])
    print(file_)
    return file_





