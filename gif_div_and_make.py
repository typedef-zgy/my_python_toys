#-*- coding: UTF-8 -*-  

import os
from PIL import Image
import imageio

folder_path = "F:\\my_python_toys\\src\\"
file_list = ["a.gif", "b.gif", "c.gif", "d.gif"]

def analyseImage(path):
    '''
    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode 
    before processing all frames.
    '''
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results


def processImage(path):
    '''
    Iterate the GIF, extracting each frame.
    '''
    mode = analyseImage(path)['mode']
    
    im = Image.open(path)

    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')
    
    try:
        while True:
            print ("saving %s (%s) frame %d, %s %s" % (path, mode, i, im.size, im.tile))
            
            '''
            If the GIF uses local colour tables, each frame will have its own palette.
            If not, we need to apply the global palette to the new frame.
            '''
            if not im.getpalette():
                im.putpalette(p)
            
            new_frame = Image.new('RGBA', im.size)
            
            '''
            Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
            If so, we need to construct the new frame by pasting it on top of the preceding frames.
            '''
            if mode == 'partial':
                new_frame.paste(last_frame)
            
            new_frame.paste(im, (0,0), im.convert('RGBA'))
            new_frame.save('%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i), 'PNG')

            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass

def mix_pic():
    mix_file_list = []
    for i in range(0, 8):
        if i % 2 == 0:
            mix_file_list.append(folder_path + "a-" + str(i) + ".png")
        else:
            mix_file_list.append(folder_path + "b-" + str(i) + ".png")
        #mix_file_list.append(folder_path + "c-" + str(i) + ".png")
        #mix_file_list.append(folder_path + "d-" + str(i) + ".png")
    mix_file_list.append(folder_path + "final.bmp")
    print(mix_file_list)

    img_list = []
    for x in mix_file_list:
        try:
            img_list.append(imageio.imread(x))
        except: 
            continue
        
    imageio.mimsave(folder_path + 'jiqi.gif', img_list, 'GIF', duration = 0.2)



def main():
    '''
        for File_Looper in file_list:
        File = folder_path + File_Looper
        processImage(File)
    '''
    mix_pic()

if __name__ == "__main__":
    main()