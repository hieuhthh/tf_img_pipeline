from utils import *

settings = get_settings()
globals().update(settings)

des = path_join(route, 'dataset')

mkdir(des)
# force_mkdir(des)

def count_file(route):
    file_count = sum(len(files) for _, _, files in os.walk(route))
    return file_count

def move_folder(route, pad=None):
    if pad is None:
        pad = route.split('/')[-1]

    print(pad, len(os.listdir(route)))

    for filename in os.listdir(route): 
        from_folder = route + '/' + filename
        to_folder = des + '/' + pad + filename

        if len(from_folder) < 1:
            print("Empty folder:", from_folder)
            continue

        try:
            shutil.copytree(from_folder, to_folder)
        except:
            print('Already have:', from_folder)

print('N class before:', len(os.listdir(des)))
print('N image before:', count_file(des))

from_folder = '/home/huynx2/hieunmt/other/tf_img_pipeline/unzip/dataset'
move_folder(from_folder)

print('N class:', len(os.listdir(des)))
print('N image:', count_file(des))

    