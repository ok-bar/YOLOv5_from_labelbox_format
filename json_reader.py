from sys import path_hooks
from tqdm import tqdm
from urllib import request
import os
from PIL import Image
import requests
import PIL


def load_images(data,images_folder):
    save_to_folder=images_folder
    names = []
    count=0
    if os.path.exists(save_to_folder):
                     pass
    else:
              os.makedirs(name=save_to_folder,exist_ok=True)
              
    for i in tqdm(range(len(data))):
      if data.iloc[i,:]['Skipped']==True:
        pass
      else:
                file_name=data.iloc[i,:]['ID']
                img=data.iloc[i,:]['Labeled Data']
                

                try:
                  im = Image.open(requests.get(img, stream=True).raw if img.startswith('http') else img)
                  width, height = im.size  # image size
                  req=request.urlretrieve(img, save_to_folder+os.sep+f'{file_name}.jpeg')
                  a=data.iloc[i,:]['Label']['objects']
                  listy=[]
                  count+=1
                
                  for j in range(len(a)):
                          top, left, h, w = a[j]['bbox'].values() # top, left, height, width
                          xywh = [(left + w / 2) / width, (top + h / 2) / height, w / width, h / height]  # xywh normalized
                          path=save_to_folder+'/'+f'{file_name}.txt'
                          cls = a[j]['value']  # class name
                          if cls not in names:
                                names.append(cls)
                          obj=0,*xywh
                          listy.append(obj)
                  with open(path, 'w') as f:
                    for t in listy:
                      f.write(' '.join(str(s) for s in t) + '\n')
                except PIL.UnidentifiedImageError:
                      print(img)
                
    print(f'number of images is {count}')
    return names
                    

names=load_images(data,path)              
print(f'classes: {names}')
