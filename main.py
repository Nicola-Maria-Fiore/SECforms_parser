import sys
import txt
import encoding
import Html
import table
import clean
import xml

if __name__ == "__main__":
    if sys.argv[1]=="-txt":
        txt.main()
    elif sys.argv[1]=="-txt -report":
        txt.checkFiles()
    elif sys.argv[1]=="-encoding" and len(sys.argv)>1:
        charset=sys.argv[2]
        path=sys.argv[3]
        encoding.main(charset, path)
    elif sys.argv[1]=="-html":
        Html.main()
    elif sys.argv[1]=="-table" and len(sys.argv)>1:
        delimiter=sys.argv[2]
        encloser=sys.argv[3]
        table.main(delimiter, encloser)

    elif sys.argv[1]=="-clean":
        clean.main()
    elif sys.argv[1]=="-xml":
        xml.main()    
    else:
        print("Incorrect arguments!")

    print("Done!")
