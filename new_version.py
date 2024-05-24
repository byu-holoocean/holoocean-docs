import os
from bs4 import BeautifulSoup
import argparse
import copy

'''
A script to add a new version to the path, and update the index.html and versionList.html files
Usage: python new_version.py <version>
For when adding a new version of the docs to the github pages site.
'''

htmlfileVersions = "versionList.html"

def update_versions_file(version):
    tempvar = None
    with open(htmlfileVersions, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        links = soup.find_all("p", class_="versionLink")
        first_link = links[0]
        print("first link is: ")
        print(first_link)
        new_link = copy.copy(first_link)
        string_newlink = str(new_link)
        old_version = first_link.find("a")["href"]
        oldversion = old_version.split("/")[0]
        string_newlink = string_newlink.replace(oldversion, version)
        new_link = BeautifulSoup(string_newlink, 'html.parser')
        first_link.insert_before(new_link)
        tempvar = soup
    with open(htmlfileVersions, 'w', encoding='utf-8') as file:
        file.write(str(tempvar))

def update_index_file(version):
    tempvar = None
    with open("index.html", 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        meta = soup.find("meta", attrs={"name": "redirect"})
        metastr = str(meta)
        oldversion = metastr.split("/")[1]
        newmetastr = metastr.replace(oldversion, version)
        newmeta = BeautifulSoup(newmetastr, 'html.parser')
        meta.replace_with(newmeta)
        link = soup.find("a", attrs={"name": "redirectLink"})
        linkstr = str(link)
        oldversion = linkstr.split("/")[1]
        newlinkstr = linkstr.replace(oldversion, version)
        newlink = BeautifulSoup(newlinkstr, 'html.parser')
        link.replace_with(newlink)
        tempvar = soup
    with open("index.html", 'w', encoding='utf-8') as file:
        file.write(str(tempvar))



def main():
    parser = argparse.ArgumentParser(description='Add a folder to the path, and update index.html')
    parser.add_argument('folder', type=str, help='The folder to add to the path')
    args = parser.parse_args()
    version = args.folder
    print("version is: ", version)
    path = os.getcwd()
    print("path is: ", path)
    if not os.path.exists(version):
        os.mkdir(version)
    else:
        print("Folder already exists. Delete it and try again.")
        exit(1)

    update_versions_file(version)
    update_index_file(version)


if __name__ == "__main__":
    main()
