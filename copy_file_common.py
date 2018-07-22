#copy some *.png to D:\{local time}
import os
import time
import shutil
import re

panfu = "D:/"
file_finder = 'label.png'
re_format = "(.*)\.(png|bmp|jpg|gif)"

def make_dir_by_time():
    '''mkdir by localtime'''
    stime = time.asctime(time.localtime())
    stime = stime.replace(':', '-')
    #print(stime)
    global panfu
    file_name =  panfu + stime
    #print(file_name)
    try:
        os.makedirs(file_name)
    except OSError as e:
        print(e)

    return file_name

def find_and_copy_png(path, name, dst):
    '''
        path:with right most  e.g:c:/test
        name:right most e.g:test
        dst:destnation path copy to
    '''
    global re_format
    folder_elems = os.listdir(path)
    for index, finder in enumerate(folder_elems):
        re_obj = re.match(re_format, finder)
        if re_obj:
            postfix = re_obj.group(2)
            s = path + '/' + finder
            d = dst + '/' + name + '_' + str(index) + '.' + postfix
            shutil.copy(s, d)
            print("copy from %s to %s" % (s, d))

def main():
    cur_path = os.getcwd()
    print('current path:' + str(cur_path))

    folder_elems = os.listdir(cur_path)
    print(folder_elems)

    dst = ''
    for looper in folder_elems:
        path_and_looper = str(cur_path) + '/' + str(looper)
        if os.path.isdir(path_and_looper):
            print('search *.png in ' + path_and_looper)
            if '' == dst:
                dst = make_dir_by_time()
                print("create folder:" + dst)
                if '' == dst:
                    return
                    
            find_and_copy_png(path_and_looper, looper, dst)
        else:
            continue

if __name__ == "__main__":
    main()