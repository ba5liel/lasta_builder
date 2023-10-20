from bs4 import BeautifulSoup
import core


from bs4 import BeautifulSoup

def fix_meta_file(filepath):
    print(f"Processing {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Remove the specified <link> tags
    tags_to_remove = [
        {"href": "index.html", "hreflang": "en", "rel": "alternate"},
        {"href": "index.html", "hreflang": "x-default", "rel": "alternate"},
        {"href": "https://www.scnsoft.de/", "hreflang": "de", "rel": "alternate"},
        {"href": "fi.html", "hreflang": "fi", "rel": "alternate"},
        {"href": "ar.html", "hreflang": "ar", "rel": "alternate"}
    ]

    for tag in tags_to_remove:
        for link in soup.find_all("link", tag):
            link.decompose()

    # Alter the <meta> tag with property `og:image`
    meta_og_image = soup.find("meta", property="og:image")
    if meta_og_image:
        meta_og_image['content'] = "bundles/app/img/areas/lasta-digital-logo.png"
    else:
        new_meta_tag = soup.new_tag("meta", content="bundles/app/img/areas/lasta-digital-logo.png", property="og:image")
        soup.head.append(new_meta_tag)

    # Add favicon related tags
    favicon_tags = [
        {"rel": "apple-touch-icon", "sizes": "120x120", "href": "/favicon/apple-touch-icon.png"},
        {"rel": "icon", "type": "image/png", "sizes": "32x32", "href": "/favicon/favicon-32x32.png"},
        {"rel": "icon", "type": "image/png", "sizes": "16x16", "href": "/favicon/favicon-16x16.png"},
        {"rel": "manifest", "href": "/favicon/site.webmanifest"}
    ]

    for tag_attrs in favicon_tags:
        if not soup.find("link", tag_attrs):
            new_tag = soup.new_tag("link", **tag_attrs)
            soup.head.append(new_tag)

    # Add meta tags
    meta_tags = [
        {"name": "msapplication-TileColor", "content": "#da532c"},
        {"name": "theme-color", "content": "#ffffff"}
    ]

    for tag_attrs in meta_tags:
        if not soup.find("meta", tag_attrs):
            new_tag = soup.new_tag("meta",  content=tag_attrs["content"])
            soup.head.append(new_tag)

    modified_content = str(soup)
    
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print(f"Finished processing {filepath}")


def start():
    starting_filepath = f"{core.BASEPATH}index.html"

    fetched_filepaths = core.get_html_links_from_section(starting_filepath, 'header', 'header')

    print(f"Fetched URLs: {len(fetched_filepaths)}")
    fix_meta_file(core.BASEPATH + "index.html")
    return
    for path in fetched_filepaths:
        try:
            print(f"Processing path {path}")
            fix_meta_file(path)
        except FileNotFoundError:
            print(f"Warning: File {path}")


    print("Replacement done!")
if __name__ == "__main__":
    start()
