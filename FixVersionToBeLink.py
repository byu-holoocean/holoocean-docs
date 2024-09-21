import bs4 as bs
import os

for path, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            with open(os.path.join(path,file), "r", encoding='utf-8') as f:
                soup = bs.BeautifulSoup(f, "html.parser")
                # do something with soup
                depth = len(path.split("\\"))
                dots = "../" * (depth-1)
                versionHeader = soup.find("div", {"class": "version"})
                if versionHeader is None:
                    continue
                val = versionHeader.getText(strip=True)
                versionHeader.clear()
                taga = soup.new_tag("a", href=dots + "versionList.html", style="color: inherit")
                taga.string = val
                versionHeader.append(taga)
                # "<a href=" + dots + "\"versionList.html\" style=\"color: inherit\">" + val + "</a>"
                tempvar = soup
                with open(os.path.join(path,file), "w", encoding='utf-8') as f:
                    f.write(str(soup))