# Script to semi-automatically create pages for sector pictures page

import os, sys, re

entries = {}
IMAGE_MD = "![{}]({}) "

with os.scandir(sys.argv[1]) as it:
    for f in it:
        split = f.name.split(".")[:-1]
        s_id = int(split[0])
        entry = entries.get(s_id,
            {
                "regular": [],
                "nopart": [],
                "hacked": [],
                "unknown": []
            }
        )

        if re.search(r"hack\d+", split[1]):
            entry["hacked"].append(f.name)
        elif re.search(r"nopart\d+", split[1]):
            entry["nopart"].append(f.name)
        elif re.search(r"^\d+", split[1]):
            entry["regular"].append(f.name)
        else:
            entry["unknown"].append(f.name)

        entries[s_id] = entry

with open("!index.md", "w") as f:
    has_misc = True if 0 in entries else False

    f.write(f"title: !!FILL IN!!\n")
    f.write(f"template: _wikipage.html\n")

    for s_id, entry in sorted(entries.items()):
        if s_id == 0:
            continue
        f.write(f"# Sector {s_id}\n")
        if entry["regular"]:
            for img in entry["regular"]:
                f.write(IMAGE_MD.format(img[:-4], img))
            f.write("  \n")
        if entry["nopart"]:
            f.write("Hacked to not load partial sectors  \n")
            for img in entry["nopart"]:
                f.write(IMAGE_MD.format(img[:-4], img))
            f.write("  \n")
        if entry["hacked"]:
            f.write("!!!HACKED PLACEHOLDER!!!  \n")
            for img in entry["hacked"]:
                f.write(IMAGE_MD.format(img[:-4], img))
            f.write("  \n")
        if entry["unknown"]:
            f.write("!!!UNKNOWN PLACEHOLDER!!!  \n")
            for img in entry["unknown"]:
                f.write(IMAGE_MD.format(img[:-4], img))
            f.write("  \n")

    if has_misc:
        entry = entries[0]
        f.write(f"# Always loaded sections\n")
        if entry["regular"]:
            for img in entry["regular"]:
                f.write(IMAGE_MD.format(img[:-4], img))
            f.write("  \n")
        if entry["nopart"]:
            f.write("Hacked to not load partial sectors  \n")
            for img in entry["nopart"]:
                f.write(IMAGE_MD.format(img[:-4], img))
            f.write("  \n")
        if entry["hacked"]:
            f.write("!!!HACKED PLACEHOLDER!!!  \n")
            for img in entry["hacked"]:
                f.write(IMAGE_MD.format(img[:-4], img))
            f.write("  \n")
        if entry["unknown"]:
            f.write("!!!UNKNOWN PLACEHOLDER!!!  \n")
            for img in entry["unknown"]:
                f.write(IMAGE_MD.format(img[:-4], img))
            f.write("  \n")
