import os
import numpy as np

src = "dataset/variance256/"
labels = ["canter", "trot", "walk"]
dst = "dataset/variance256_aug/"

for label in labels:
    src_dir = os.path.join(src, label)
    dst_dir = os.path.join(dst, label)
    os.makedirs(dst_dir, exist_ok=True)
    
    files = sorted(os.listdir(src_dir))
    
    for i, file in enumerate(files):
        src_path = os.path.join(src_dir, file)
        var_map = np.load(src_path)
        
        # --- Save original ---
        dst_path_orig = os.path.join(dst_dir, file)
        np.save(dst_path_orig, var_map)
        
        # --- Save flipped as new file ---
        flipped_map = np.fliplr(var_map)
        name, ext = os.path.splitext(file)
        dst_path_flip = os.path.join(dst_dir, f"{name}_flipped{ext}")
        np.save(dst_path_flip, flipped_map)
