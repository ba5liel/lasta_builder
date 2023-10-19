import re
from bs4 import BeautifulSoup
import core


from bs4 import BeautifulSoup

def replace_social_share_value_in_file(filepath):
    print(f"Processing {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    replace_http  = re.compile(re.escape('scnsoft.com'))

    modified_content = replace_http.sub("lasta.digital", content)

    replace_site_name  = re.compile(re.escape('ScienceSoft'))

    modified_content = replace_site_name.sub("LastaDigital", modified_content)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(modified_content)
    print(f"Finished processing {filepath}")


def start():
    starting_filepath = f"{core.BASEPATH}index.html"

    fetched_filepaths = core.get_html_links_from_section(starting_filepath, 'header', 'header')

    print(f"Fetched URLs: {len(fetched_filepaths)}")

    for path in fetched_filepaths:
        try:
            print(f"Processing path {path}")
            replace_social_share_value_in_file(path)
        except FileNotFoundError:
            print(f"Warning: File {path}")


    print("Replacement done!")
if __name__ == "__main__":
    start()
