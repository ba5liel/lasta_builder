from bs4 import BeautifulSoup
import core


from bs4 import BeautifulSoup

def replace_anchor_value_in_file(filepath, known_path: list[str]):
    print(f"Processing {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    main = soup.find("main")
    if not main:
        return
    
    anchors_linking_to_known_path = [x.split('/')[-1] for x in known_path]
    
    anchors = main.find_all('a', href=True)
    for a in anchors:
        last_segment = a['href'].split('/')[-1]
        
        if a['href'].endswith('.html') and last_segment not in anchors_linking_to_known_path:
            a['href'] = 'javascript:void(0);'

    modified_content = str(soup)
    
    with open("test.html", 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print(f"Finished processing {filepath}")


def start():
    starting_filepath = f"{core.BASEPATH}index.html"

    fetched_filepaths = core.get_html_links_from_section(starting_filepath, 'header', 'header')

    print(f"Fetched URLs: {len(fetched_filepaths)}")

    for path in fetched_filepaths:
        try:
            print(f"Processing path {path}")
            replace_anchor_value_in_file(path, fetched_filepaths)
        except FileNotFoundError:
            print(f"Warning: File {path}")


    print("Replacement done!")
if __name__ == "__main__":
    start()
