from bs4 import BeautifulSoup
import os

def HTMLtoTEXT(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup.text

def main():
    source_folder = "resources/html"
    out_folder = "results/html"

    for filename in os.listdir(source_folder):
        if filename.endswith(".html") or filename.endswith(".htm") or filename.endswith(".txt"):
            with open(os.path.join(source_folder, filename), 'r') as f:
                content = f.read()
            res = HTMLtoTEXT(content)
            with open(os.path.join(out_folder, filename), 'w') as f:
                f.write(res)       