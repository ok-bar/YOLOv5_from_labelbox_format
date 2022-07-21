import os
from pathlib import Path
from tqdm import tqdm
import random
import shutil



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
  
  


random.seed(42)



def train_test_val_split(source_imgs,source_labels,root_path,tr_dst,tst_dst,val_dst,tr_size,tst_size):
  source_img=source_imgs
  source_label = source_labels
  destination_tr = tr_dst
  destination_tst = tst_dst
  destination_val = val_dst
  tr_split=int(len(source_img)*tr_size)
  tst_split=int(len(source_img)*(1-tst_size))
  os.makedirs(destination_tr, exist_ok=True)
  os.makedirs(destination_tst,  exist_ok=True)
  os.makedirs(destination_val,  exist_ok=True)

  os.makedirs(destination_tr+'/images',exist_ok=True)
  os.makedirs(destination_tr+'/labels',exist_ok=True)
  os.makedirs(destination_tst+'/images',exist_ok=True)
  os.makedirs(destination_tst+'/labels',exist_ok=True)
  os.makedirs(destination_val+'/images',exist_ok=True)
  os.makedirs(destination_val+'/labels',exist_ok=True)


  print('creating train data set...')
  for i in tqdm(range(0,tr_split)):
    # img=source_imgs+'/'+source_img[i]
    img=source_img[i]
    new_img=destination_tr+'/images'+'/'+source_img[i].split('/')[-1]
    shutil.copyfile(img, new_img)
    
    # msk=source_labels+'/'+source_label[i]
    msk=source_label[i]
    new_mask=destination_tr+'/labels'+'/'+source_label[i].split('/')[-1]
    shutil.copyfile(msk, new_mask)

  print('creating test data set...')

  for i in tqdm(range(tr_split,tst_split)):
    # img=source_imgs+'/'+source_img[i]
    img=source_img[i]
    new_img=destination_tst+'/images'+'/'+source_img[i].split('/')[-1]
    shutil.copyfile(img, new_img)
    # msk=source_labels+'/'+source_label[i]
    msk=source_label[i]
    new_mask=destination_tst+'/labels'+'/'+source_label[i].split('/')[-1]
    shutil.copyfile(msk, new_mask)

  print('creating validation data set...')
  for i in tqdm(range(tst_split,len(source_img)-1)):
    # img=source_imgs+'/'+source_img[i]
    img=source_img[i]
    new_img=destination_val+'/images'+'/'+source_img[i].split('/')[-1]
    shutil.copyfile(img, new_img)
    # msk=source_labels+'/'+source_label[i]
    msk=source_label[i]
    new_mask=destination_val+'/labels'+'/'+source_label[i].split('/')[-1]
    shutil.copyfile(msk, new_mask)

  x_train_dir = os.path.join(destination_tr, 'images')
  y_train_dir = os.path.join(destination_tr, 'labels')

  x_test_dir = os.path.join(destination_tst, 'images')
  y_test_dir = os.path.join(destination_tst, 'labels')

  x_val_dir = os.path.join(destination_val, 'images')
  y_val_dir = os.path.join(destination_val, 'labels')

  print('the number of image in the train: ',len(os.listdir(x_train_dir)))
  print('the number of image in the test: ',len(os.listdir(x_test_dir)))
  print('the number of image in the validation: ',len(os.listdir(x_val_dir)))

  return x_train_dir,y_train_dir,x_test_dir,y_test_dir,x_val_dir,y_val_dir



