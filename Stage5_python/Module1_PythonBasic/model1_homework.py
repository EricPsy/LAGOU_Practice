import os
import math

def check(dirpath):
    """检查文件夹名字是否存在"""
    if not os.path.exists(dirpath):
        print('文件夹不存在，请重新输入')
        return False
    if not os.path.isdir(dirpath):
        print('输入的不是文件夹名称，请重新输入')
        return False
    else:
        return True

def calculate_size(dirpath):
    """计算文件夹下面文件大小"""
    file_list = os.listdir(dirpath)
    total_size = 0
    for item in file_list:
        file_path = os.path.join(dirpath, item) #拼接出单个文件的路径
        total_size += os.path.getsize(file_path)
    return int(total_size)

def transfer_size(size):
    """将文件大小带上合适的单位"""
    size = int(size)
    kb = 1024
    mb = int(math.pow(1024,2))
    gb = int(math.pow(1024,3))
    tb = int(math.pow(1024,4))
    if size < 1024:
        final_size = '%.2f %s' % (size, 'Byte')
        return final_size
    if size in range(1024,mb):
        final_size = '%.2f %s' % (size/kb, 'KB')
        return final_size
    if size in range(mb,gb):
        final_size = '%.2f %s' % (size/mb, 'MB')
        return final_size
    if size in range(gb,tb):
        final_size = '%.2f %s' % (size/gb, 'GB')
        return final_size
    else:
        final_size = '%.2f %s' % (size/tb, 'TB')
        return final_size

if __name__ == '__main__':
    """主程序：输入目标文件夹路径并计算该文件夹大小"""
    while True:
        path = input('input the path of directory:')
        if check(path):
            print(path)
            break
        else:
            print(path)
            continue
    final_size = transfer_size(calculate_size(path))
    print(final_size)




