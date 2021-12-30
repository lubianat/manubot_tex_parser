import os
import re

file = "manuscript.tex"

os.system(f'grep "includegraphics" {file} > graphic_lines.txt')


with open("graphic_lines.txt", "r") as f:
    images = f.read()

original_links = re.findall("{.*}", images)

print(original_links)
links = [
    link.replace(
        "{images/",
        "https://raw.githubusercontent.com/lubianat/quali_phd/main/content/images/",
    )
    for link in original_links
]
print(links)

links = [
    link.replace(
        "{",
        "",
    )
    for link in links
]

links = [
    link.replace(
        "}",
        "",
    )
    for link in links
]

for link in links:
    print(f"Downloading {link}")

    file_name = link.split("/")[-1].replace("?raw=true", "")
    os.system(f"wget {link} -O images/{file_name}")

os.system(f"cd -")
os.system("pwd")

os.system("pwd")
with open(file) as f:
    manuscript = f.read()


original_links = [
    link.replace(
        "{",
        "",
    )
    for link in original_links
]

original_links = [
    link.replace(
        "}",
        "",
    )
    for link in original_links
]
for link in original_links:

    image_ending = link.split("/")[-1]
    print(image_ending)

    manuscript = manuscript.replace(link, f"images/{image_ending}")


manuscript = manuscript.replace("?raw=true", "")

manuscript = manuscript.replace(".svg", ".svg.png")

manuscript = manuscript.replace(
    "\includegraphics{", "\includegraphics[width=0.85\columnwidth]{"
)
manuscript = manuscript.replace(
    "\includegraphics[width=0.85\textwidth,height=\textheight]",
    "\includegraphics[width=0.85\columnwidth]",
)

print(manuscript)

with open(f"processed_{file}", "w+") as f:
    f.write(manuscript)

os.system(
    """
    bash convert_svgs.bash
    """
)
