import os
import sys

#PATH
path="html"
#path="table"
#path="xml"

#ENCODING
charset="utf-8-sig"

path_resources="resources/"+path+"/files/"
path_results="resources/"+path+"/encoding/"
dirs=os.listdir(path_resources)
for i,value in enumerate(dirs):
    file_path=path_resources+value
    with open(file_path, 'r') as f:
        unicode_text=f.read()
        encoded_unicode = unicode_text.encode(charset)
    file_path=path_results+value
    with open(file_path, 'wb') as f:
        f.write(encoded_unicode)
        f.close()  
    print("{} - {}".format(str(i), value))
print("done")
        

