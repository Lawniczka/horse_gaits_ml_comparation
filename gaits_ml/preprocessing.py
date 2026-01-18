import cv2
import os
import numpy as np

dir = "dataset/horseactionrecognition/crop_"
labels = ["canter", "trot", "walk"]
suffix = "pic_nobacklastobst/"

def preprocess_edges(grayscale_dir, edges_dir, src):        
    if os.path.exists(grayscale_dir) and os.path.exists(edges_dir):
        print("  Already processed, skipping.")
        return

    os.makedirs(grayscale_dir, exist_ok=True)
    os.makedirs(edges_dir, exist_ok=True)

    files = sorted(os.listdir(src))
    print(f"Found   {len(files)} files...", end=' \r')

    for frame in files:
        img = cv2.imread(src + frame)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        np.save(grayscale_dir + os.path.splitext(frame)[0], gray.astype(np.uint8))
        
        gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

        grad_mag = np.sqrt(gx**2 + gy**2)
        grad_mag = cv2.normalize(grad_mag, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        values = grad_mag[grad_mag > 0].ravel()

        t2 = np.percentile(values, 95)
        t1 = 0.4 * t2

        edges = cv2.Canny(img, t1, t2)
        np.save(edges_dir + os.path.splitext(frame)[0], edges.astype(np.uint8))

    print(f"Loaded")

def fix_names(edges_dir, grayscale_dir):
    files = sorted(os.listdir(edges_dir))

    for i, file in enumerate(files):
        os.rename(edges_dir + file, edges_dir + f"{str(i+1).zfill(7)}.npy")
        os.rename(grayscale_dir + file, grayscale_dir + f"{str(i+1).zfill(7)}.npy")
        
    print (f"Fixed names for {edges_dir}")
        
        
for label in labels:
    for sample in os.listdir(dir + label + suffix):
        print(f"Processing sample {sample} for action '{label}':")
        
        src = dir + label + suffix + sample + "/"
        grayscale_dir   = "dataset/preprocessed/grayscale/" + label + '/' + str(sample).zfill(4) + "/"
        edges_dir       = "dataset/preprocessed/edges/" + label + '/' + str(sample).zfill(4) + "/"
        
        #preprocess_edges(grayscale_dir, edges_dir, src)
        fix_names(edges_dir, grayscale_dir)