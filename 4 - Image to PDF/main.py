import sys
import img2pdf
import os
# to run "python3 main.py image.jpg"
filepath = sys.argv[1]
if os.path.isdir(filepath):
    with open("output.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(img2pdf.convert(imgs))
elif os.path.isfile(filepath):
    if filepath.endswith(".jpg"): #jpg
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(filepath))
else:
    print("please input file or dir")
