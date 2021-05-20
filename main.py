import sys
import encoding

if __name__ == "__main__":
    if sys.argv[1]=="-encoding" and len(sys.argv)>1:
        charset=sys.argv[2]
        path=sys.argv[3]
        encoding.main(charset, path)
    else:
        print("incorrect arguments - error")
    print("done")
