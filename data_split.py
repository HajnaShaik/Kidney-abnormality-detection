import os
import shutil
import random

# Define paths to the original dataset and the destination directories
original_dataset_dir = 'D:\\Kidney abnormality detection\\Dataset'
base_dir = 'D:\\Kidney abnormality detection\\train_test_val'
os.makedirs(base_dir, exist_ok=True)

# Define subdirectories for train, validation, and test sets
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Define subdirectories for each class within train, validation, and test sets
classes = ['tumor', 'cyst', 'stone', 'normal']
for cls in classes:
    os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(validation_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(test_dir, cls), exist_ok=True)

# Define the proportions of data to be used for training, validation, and testing (e.g., 60-20-20)
train_ratio = 0.6
val_ratio = 0.2
test_ratio = 0.2

# Iterate over each class and copy images into train, validation, and test directories
for cls in classes:
    cls_dir = os.path.join(original_dataset_dir, cls)
    fnames = [f for f in os.listdir(cls_dir) if f.endswith('.jpg')]  # Assuming images are in JPEG format
    
    # Shuffle the list of filenames
    random.shuffle(fnames)
    
    # Calculate split indices
    train_split_index = int(train_ratio * len(fnames))
    val_split_index = int((train_ratio + val_ratio) * len(fnames))
    
    # Copy images to train directory
    for fname in fnames[:train_split_index]:
        src = os.path.join(cls_dir, fname)
        dst = os.path.join(os.path.join(train_dir, cls), fname)
        shutil.copyfile(src, dst)
    
    # Copy images to validation directory
    for fname in fnames[train_split_index:val_split_index]:
        src = os.path.join(cls_dir, fname)
        dst = os.path.join(os.path.join(validation_dir, cls), fname)
        shutil.copyfile(src, dst)
    
    # Copy images to test directory
    for fname in fnames[val_split_index:]:
        src = os.path.join(cls_dir, fname)
        dst = os.path.join(os.path.join(test_dir, cls), fname)
        shutil.copyfile(src, dst)

print("Dataset splitting completed.")
