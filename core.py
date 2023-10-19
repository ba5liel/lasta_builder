from bs4 import BeautifulSoup
BASEPATH = "../lasta.digital/lasta.digital/"

def get_html_links_from_section(filepath, section_tag, section_class):
    print(f"get_html_links_from_header {filepath}")
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    header = soup.find(section_tag, class_=section_class)
    if not header:
        return []
   
    links = [BASEPATH + a['href'] for a in header.find_all('a', href=True) if a['href'].endswith('.html')]
    return links

def replace_header_in_file(filepath, new_html, section_tag, section_class):
    print(f"Opening {filepath}")
    # 1. Read the file's content
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace("<![endif]-->", "<!--[endif]-->")
    content = content.replace("<![endif] -->", "<!--[endif]-->")
    # 2. Modify the content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    # Explicitly find the <header> element with class "header"
    header = soup.find(section_tag, class_=section_class)
    if header:
        header.replace_with(BeautifulSoup(new_html, 'html.parser'))
        modified_content = str(soup)

    modified_content = str(soup)

    # 3. Write the modified content back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(modified_content)
    

def start(section_tag, section_class, new_section_content):
    starting_filepath = f"{BASEPATH}index.html"
    new_html = new_section_content

    fetched_filepaths = get_html_links_from_section(starting_filepath, 'header', 'header')

    print(f"Fetched URLs: {len(fetched_filepaths)}")

    # replace_header_in_file(starting_filepath, new_html, section_tag, section_class)
    # return
    for path in fetched_filepaths:
        try:
            print(f"Processing path {path}")
            replace_header_in_file(path, new_html,section_tag, section_class)
        except FileNotFoundError:
            print(f"Warning: File {path}")


    print("Replacement done!")