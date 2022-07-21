import os
from pathlib import Path
from tqdm import tqdm

def split_to_images_labels(path):
  img_paths=[]
  txt_paths=[]

  for root,sub,files in os.walk(path):
    for file in files:
      file=root+file
      if file.endswith('jpeg'):
        img_paths.append(file)
      else:
        txt_paths.append(file)
  data_size = len(img_paths)
  label_size = len(txt_paths)
  print(f'number of images in the dataset is: {data_size}')
  print(f'number of labels in the dataset is: {label_size}')
  return img_paths,txt_paths

def unique_images(img_paths,txt_paths):
  unique_img_paths=[]
  unique_txt_paths=[]
  files_size=[]


  for i in tqdm(range(len(img_paths))):
    f_size=Path(img_paths[i]).stat().st_size
    if f_size in files_size:
      pass
    else:
      files_size.append(f_size)
      unique_img_paths.append(img_paths[i])
      unique_txt_paths.append(txt_paths[i])
  unique_data=len(unique_img_paths)
  print(f'number of unique images in the dataset is: {unique_data}')
