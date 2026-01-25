import os
import numpy as np
import cv2

dir = "dataset/preprocessed/edges/"
labels = ["canter", "trot", "walk"]

src = "dataset/variance_big_256/"

T = 32
W = 256
H = 256

def compute_variance(edges_dir, start, sample, label):

    sum_ = np.zeros((W,H), dtype=np.float32)
    sum_sq = np.zeros((W,H), dtype=np.float32)

    for i in range(start * T, start * T + T):
        frame = np.load(edges_dir + f"{str(i+1).zfill(7)}.npy").astype(np.float32)
        resized = cv2.resize(frame, (W,H), interpolation=cv2.INTER_AREA)
        sum_ += resized
        sum_sq += resized ** 2
        
    mean = sum_ / T
    var = (sum_sq / T) - (mean ** 2)

    
    var_norm = cv2.normalize(var, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    os.makedirs(src + label + "/", exist_ok=True)
    
    sample = sample[:-4] + str(start) + sample[-3:]
    np.save(src + label + "/" + sample, var_norm)

for label in labels:
    for sample in os.listdir(dir + label + "/"):
        print(f"Computing variance for sample {sample} of action '{label}':")
        
        edges_dir = dir + label + "/" + sample + "/"
        
        seq = 0
        
        while len(os.listdir(edges_dir)) > T * (seq + 1) :
            compute_variance(edges_dir, seq, sample, label)
            seq +=1
        