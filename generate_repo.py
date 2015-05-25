#!/usr/bin/env python3.4

from configparser import ConfigParser
from urllib.parse import urlparse, urlunparse
from urllib.request import urlopen
import json
import sys

urls = open("pkglist.txt", "r")

repo_json = json.loads('{"packages": []}')

for url in urls:
    pkg_name, url = url.split()
    
    pkg_json = None
    try:
        with urlopen(url + "/repo.json") as f:
            pkg_json = f.read(524288).decode("utf-8")
        pkg_json = json.loads(pkg_json)
    except:
        print(sys.exc_info()[0])
        pkg_json = None

    if not pkg_json:
        continue

    try:
        pkg_json["name"]
        pkg_json["description"]
        pkg_json["version"]
        pkg_json["repo"]
    except:
        print(sys.exc_info()[0])
        continue

    if "branch" not in pkg_json.keys():
        pkg_json["branch"] = "master"

    pkg_json["pkg_name"] = pkg_name

    repo_json["packages"].append(pkg_json)


repo_output = open("repo.json", "wb")
repo_output.write(json.dumps(repo_json, sort_keys=True, indent=4).encode("utf-8"))
repo_output.write(b"\n")
repo_output.close()

