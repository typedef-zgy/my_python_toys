#copy some *.png to D:\{local time}
import os
import time
import shutil

panfu = "D:/"
file_finder = 'label.png'

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
    global file_finder
    folder_elems = os.listdir(path)

    if file_finder in folder_elems:
        s = path + '/' + file_finder
        d = dst + '/' + name + '.png'
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