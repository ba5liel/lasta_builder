import re
from bs4 import BeautifulSoup
import core


from bs4 import BeautifulSoup
new_schedule_html = f"""<div class="schedule-snippet-wrap-btn">
<a class="schedule-snippet-wrap-link js-track-click lazy no-bg entered error" data-bg="./schedule-call-bg.svg" data-track-element="button" href="{core.BASEPATH}about/company/contact-us-discuss-your-needs.html" rel="nofollow" target="" data-ll-status="error" style="background-image: url(&quot;./schedule-call-bg.svg&quot;);">
<img alt="schedule-call" class="lazy" height="64" src="./schedule-call-snippet.svg" width="70">
                        Schedule a call
                      </a>
</div>"""
def replace_social_share_value_in_file(filepath):
    print(f"Processing {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    
    soup = BeautifulSoup(content, 'html.parser')
    # Explicitly find the <header> element with class "header"
    schedule_dev = soup.find("div", class_="schedule-snippet-wrap-btn")
    if schedule_dev:
        schedule_dev.replace_with(BeautifulSoup(new_schedule_html, 'html.parser'))

    modified_content = str(soup)

    replace_http  = re.compile(re.escape('scnsoft.com'))

    modified_content = replace_http.sub("lasta.digital", content)

    replace_site_name  = re.compile(re.escape('ScienceSoft'))

    modified_content = replace_site_name.sub("LastaDigital", modified_content)

    replace_phone_number1  = re.compile(re.escape('1 214 306 6837'))

    modified_content = replace_phone_number1.sub("1 571 365 1523", modified_content)
    replace_phone_number1  = re.compile(re.escape('1 972 454 4730'))

    modified_content = replace_phone_number1.sub("251 961 186 323", modified_content)
    replace_phone_number1  = re.compile(re.escape('scnsoft.com'))

    modified_content = replace_phone_number1.sub("lasta.digital", modified_content)
    
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
