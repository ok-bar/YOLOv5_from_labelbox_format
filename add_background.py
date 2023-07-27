start=int(len(os.listdir(x_train_dir))*0.1)
med=start+int(len(os.listdir(x_val_dir))*0.1)
end=med+int(len(os.listdir(x_test_dir))*0.1)


for i in tqdm(range(0,start)):
    img=background_images[i]
    img='/content/drive/MyDrive/active_learn_data/train/2/'+img
    new_img=x_train_dir+'/'+background_images[i]
    shutil.copyfile(img, new_img)



for i in tqdm(range(start,med)):
    img=background_images[i]
    img='/content/drive/MyDrive/active_learn_data/train/2/'+img
    new_img=x_val_dir+'/'+background_images[i]
    shutil.copyfile(img, new_img)

for i in tqdm(range(med,end)):
    img=background_images[i]
    img='/content/drive/MyDrive/active_learn_data/train/2/'+img
    new_img=x_test_dir+'/'+background_images[i]
    shutil.copyfile(img, new_img)
