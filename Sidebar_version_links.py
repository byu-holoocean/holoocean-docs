import argparse
import os
import copy
from bs4 import BeautifulSoup

'''
A script to add version links to the sidebar in various html files
Usage: python Sidebar_version_links.py <version>
For when adding a new version of the docs to the github pages site.
'''

def update_version_header(file):
    tempvar = None
    with open(file, 'r', encoding='utf-8') as f:
        try:
            soup = BeautifulSoup(f, 'html.parser')
            version_header = soup.find("div", {"class": "version"})
            new_version = BeautifulSoup('<div class="version">Develop</div>', 'html.parser')
            version_header.replaceWith(new_version)
            tempvar = soup
        except Exception as e:
            print("Error in file: ", file)
            if file == "py-modindex.html":
                return
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(tempvar))


def update_sidebar(file, level, num_links=7):
    tempvar = None
    with open(file, 'r', encoding='utf-8') as f:
        try:
            soup = BeautifulSoup(f, 'html.parser')
            links = soup.find_all("li", {"class": "toctree-l1"})
            changelog = links[num_links-1]
            dots = "../"
            for i in range(level):
                dots += "../"
            new_link = BeautifulSoup('\n<li class="toctree-l1"><a class="reference internal" href=' + dots + 'versionList.html>Other Versions Documentation</a></li>', 'html.parser')
            changelog.insert_after(new_link)
            versionHeader = soup.find("div", {"class": "version"})
            val = versionHeader.getText(strip=True)
            versionHeader.replace_with(BeautifulSoup('<div class="version"><a href=' + dots + 'versionList.html style="color: inherit;">' + val + '</a></div>', 'html.parser'))
            # versionHeader.string = "<a href=" + dots + "\"versionList.html\" style=\"color: inherit\:>" + val + "</a>"
            tempvar = soup
        except Exception as e:
            print("Error in file: ", file)
            if file == "py-modindex.html":
                return
            print(soup)
            print(soup.find("div", {"class": "version"}))
            print(versionHeader)
            raise e
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(tempvar))

def main():
    parser = argparse.ArgumentParser(description='Add version links to the sidebar in various html files')
    parser.add_argument('folder', type=str, help='The folder to add to the path')
    args = parser.parse_args()
    version = args.folder
    isDevelop = False if version != "develop" else True
    print("version is: ", version)
    os.chdir(version)
    path = os.getcwd()
    for file in os.listdir():
        if file.endswith(".html"):
            update_sidebar(file, 0)
            if isDevelop:
                update_version_header(file)

    path0 = os.path.join(path, "changelog")

    path1 = os.path.join(path, "agents")
    path2 = os.path.join(path, "develop")
    path4 = os.path.join(path, "sensors")

    path3 = os.path.join(path, "holoocean")
    
    paths = [path1, path2, path4]
    for path in paths:
        os.chdir(path)
        for file in os.listdir():
            if file.endswith(".html"):
                if isDevelop:
                    update_version_header(file)
                update_sidebar(file, 1)
            elif os.path.isdir(file):
                os.chdir(file)
                for file in os.listdir():
                    if file.endswith(".html"):
                        if isDevelop:
                            update_version_header(file)
                        update_sidebar(file, 2)
                os.chdir("..")
    os.chdir(path)

    paths = [path0, path3]
    for path in paths:
        os.chdir(path)
        for file in os.listdir():
            if file.endswith(".html"):
                if isDevelop:
                    update_version_header(file)
                update_sidebar(file, 1)
    os.chdir("..")

    path = os.getcwd()
    
    pathu = os.path.join(path, "usage")
    pathe = os.path.join(path, "examples")
    os.chdir(pathu)
    for file in os.listdir():
        if file.endswith(".html"):
            if isDevelop:
                update_version_header(file)
            update_sidebar(file, 1)
    os.chdir(pathe)
    for file in os.listdir():
        if file.endswith(".html"):
            if isDevelop:
                update_version_header(file)
            update_sidebar(file, 1)
    pathe = os.path.join(pathe, "examples")
    os.chdir(pathe)
    for file in os.listdir():
        if file.endswith(".html"):
            if isDevelop:
                update_version_header(file)
            update_sidebar(file, 2)
    for file in os.listdir():
        if file.endswith(".html"):
            if isDevelop:
                update_version_header(file)
            update_sidebar(file, 2)
    os.chdir("..")
    os.chdir("..")
    path = os.getcwd()

    pathp = os.path.join(path, "packages")
    os.chdir(pathp)
    for file in os.listdir():
        if file.endswith(".html"):
            if isDevelop:
                update_version_header(file)
            update_sidebar(file, 1)
        elif os.path.isdir(file):
            os.chdir(file)
            for file in os.listdir():
                if file.endswith(".html"):
                    if isDevelop:
                        update_version_header(file)
                    update_sidebar(file, 2)
                elif os.path.isdir(file):
                    os.chdir(file)
                    for file in os.listdir():
                        if file.endswith(".html"):
                            if isDevelop:
                                update_version_header(file)
                            update_sidebar(file, 3)
                    os.chdir("..")
            os.chdir("..")
    os.chdir("..")
    return

if __name__ == "__main__":
    main()
        
    
    