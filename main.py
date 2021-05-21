import os
import sys

def encoding(charset, path):
    path_resources="resources/"+path+"/files/"
    path_results="resources/"+path+"/encoding/"
    dirs=os.listdir(path_resources)
    for i,item in enumerate(dirs):
        file_path=path_resources+item
        with open(file_path, 'r') as f:
            unicode_text=f.read()
            encoded_unicode = unicode_text.encode(charset)
        file_path=path_results+item
        with open(file_path, 'wb') as f:
            f.write(encoded_unicode)
            f.close()  
        print("{} - {}".format(str(i), item))
    print("done")
        
if __name__ == "__main__":
    if sys.argv[1]=="-encoding" and len(sys.argv)>1:
        charset=sys.argv[2]
        path=sys.argv[3]
        encoding(charset, path)
    else:
        print("incorrect arguments - error")
