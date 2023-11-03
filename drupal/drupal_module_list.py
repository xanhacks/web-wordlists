#!/usr/bin/env python3
import re

import requests
from bs4 import BeautifulSoup


SEARCH_URL = "https://www.drupal.org/project/project_module?f[0]=&f[1]=&f[2]=&f[3]=&f[4]=sm_field_project_type%3Afull&f[5]=&f[6]=&text=&solrsort=iss_project_release_usage%20desc&op=Search"
PROJECT_PATTERN = r"^/project/[a-z_]+$"
PAGE_MIN, PAGE_MAX = 1, 1335


def get_module_names(page):
    """Returns a list of Drupal module names from the given page."""
    module_names = set() 
    resp = requests.get(SEARCH_URL + "&page=" + str(page))
    soup = BeautifulSoup(resp.text, "html.parser")

    divs = soup.find_all("div", class_="node-project-module")
    for div in divs:
        anchors = soup.find_all("a")
        for anchor in anchors:
            if anchor.has_attr("href") and re.match(PROJECT_PATTERN, anchor["href"]):
                module_names.add(anchor["href"].split("/")[2])

    return module_names


def main():
    """Writes a list of Drupal module names to a file."""
    with open("drupal_modules_list.txt", "a") as f:
        for i in range(PAGE_MIN, PAGE_MAX + 1):
            print("Extracting module names from page", i, "...")
            module_names = get_module_names(i)
            f.write("\n".join(module_names))
            f.flush()

main()
