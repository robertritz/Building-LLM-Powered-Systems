import csv
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os
import json
from tqdm import tqdm

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash-latest",
                              generation_config={"response_mime_type": "application/json"})

def fetch_wikipedia_page(url):
    response = requests.get(url)
    return response.text

def extract_book_entries(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')
    print(len(tables))
    rows = []
    for table in tables:
        table_rows = table.find_all('tr')[1:]
        rows.extend(table_rows)
    print("Found", len(rows), "rows.")
    return [' '.join(row.stripped_strings) for row in rows]

def extract_book_info(text):
    prompt = """
    Extract the following information from this book entry:
    - Book Title
    - Author
    - Language
    - Approximate sales

    Book entry:
    {text}

    Return the information in JSON format.
    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "Book Title": {
          "type": "string",
          "description": "The title of the book"
        },
        "Author": {
          "type": "string",
          "description": "The name of the book's author"
        },
        "Language": {
          "type": "string",
          "description": "The language in which the book is written"
        },
        "Approximate sales": {
          "type": "string",
          "description": "The approximate number of sales for the book in USD"
        }
      },
      "required": ["Book Title", "Author", "Language", "Approximate sales"],
      "additionalProperties": false
    }
    """
    response = model.generate_content(prompt.replace("{text}", text))
    return json.loads(response.text)

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Book Title', 'Author', 'Language', 'Approximate sales'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Main execution
url = "https://en.wikipedia.org/wiki/List_of_best-selling_books"
html = fetch_wikipedia_page(url)
book_entries = extract_book_entries(html)

extracted_data = []
for entry in tqdm(book_entries[:10]):
    book_info = extract_book_info(entry)
    extracted_data.append(book_info)

save_to_csv(extracted_data, 'bestselling_books.csv')
