import os
import sys
from PIL import Image


full=[]
compressed=[]

for file in os.listdir(sys.argv[1]):
    if "jpg" in file:
        im= Image.open(sys.argv[1] + file)
        
        w= im.size[0]
        h= im.size[1]
        
        compress_im= im.resize((int((w/4)), int((h/4))), Image.ANTIALIAS)
        
        compress_im.save(sys.argv[1] + 'small_' + file, quality=80)
        
        compressed.append('small_' + file)
        full.append(file)


file = sys.argv[1] + "index.html"
f= open(file, "a")

f.write('<html><body>')
for i in range(0, len(full)):
    f.write('<a href="' + full[i] + '"> <img src="' + compressed[i] + '" width=100%> </a> </br></br>')
f.write('</body></html>')

f.close()
