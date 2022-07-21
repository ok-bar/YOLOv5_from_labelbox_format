def background_for_yolo(x_train_dir,background_path):

  background_images=os.listdir(background_path)
  for i in tqdm(range(len(background_images))):
      img=background_images[i]
      img=background_path+img
      new_img=x_train_dir+'/'+background_images[i]
      shutil.copyfile(img, new_img)

