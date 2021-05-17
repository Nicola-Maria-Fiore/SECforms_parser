from bs4 import BeautifulSoup
import os

def HTMLtoTEXT(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    content = soup.text.split(" ")
    content = [c for c in content if len(c)<=30]
    return " ".join(content)

def main():
    source_folder = "resources/html/encoding"
    out_folder = "results/html"

    for filename in os.listdir(source_folder):
        if filename.endswith(".html") or filename.endswith(".htm") or filename.endswith(".txt"):
            with open(os.path.join(source_folder, filename), 'r') as f:
                content = f.read()
            res = HTMLtoTEXT(content)
            with open(os.path.join(out_folder, filename), 'w') as f:
                f.write(res)       