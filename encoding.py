import os

path_resources="C:/Python/files/"
encoding="utf8"
path_results="C:/Python/encoding/"

dirs=os.listdir(path_resources)
for file in dirs:
    input_file=path_resources+file
    with open(input_file, 'r') as f:
        unicode_text=f.read()
        encoded_unicode = unicode_text.encode(encoding)
    out_file=path_results+file
    with open(out_file, 'wb') as f:
        f.write(encoded_unicode)
        f.close()