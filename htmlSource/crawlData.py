import requests
from bs4 import BeautifulSoup

for i in range(1, 31):
    file_path = f"html_day{i}.txt"
    file_content = ""
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
    soup = BeautifulSoup(file_content, "html.parser")
    title = soup.title
    term_elements = soup.find_all("span", class_="TermText")
    for term_element in term_elements:
        content = term_element.get_text()
    output_file = f"../vocabularySource/vocabulary_{i}.txt"
    with open(output_file, "a", encoding="utf-8") as file:
        for term_element in term_elements:
            content = term_element.get_text()
            file.write(content + '\n')
    print(f"Kết quả đã được ghi vào {output_file}")

