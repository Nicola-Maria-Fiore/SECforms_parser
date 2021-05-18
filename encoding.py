import os

encoding="utf-8-sig"
path="html"

path_resources="resources/"+path+"/files/"
path_results="resources/"+path+"/encoding/"
dirs=os.listdir(path_resources)

i=0
for file in dirs:

    input_file=path_resources+file
    with open(input_file, 'r') as f:
        unicode_text=f.read()
        encoded_unicode = unicode_text.encode(encoding)
    out_file=path_results+file

    with open(out_file, 'wb') as f:
        f.write(encoded_unicode)
        f.close()  
    print("{} - {}".format(str(i), input_file))
    i=i+1
