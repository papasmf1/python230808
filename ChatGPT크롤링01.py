import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("li", class_="sh_blog_top")

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81%EC%97%90%EC%96%B4"
results_per_page = 10
total_pages = 100

# Create a new Excel workbook and select the active sheet
wb = Workbook()
ws = wb.active

# Set headers for columns
headers = ["Blog Title", "Blog URL", "Blog Date"]
ws.append(headers)

for page in range(1, total_pages + 1):
    start = (page - 1) * results_per_page + 1
    page_url = f"{base_url}&start={start}"
    
    blog_entries = crawl_page(page_url)
    
    for entry in blog_entries:
        blog_title = entry.find("a", class_="sh_blog_title").text
        blog_url = entry.find("a", class_="sh_blog_title")["href"]
        blog_date = entry.find("dd", class_="txt_inline").text
        
        # Append data to the Excel worksheet
        ws.append([blog_title, blog_url, blog_date])

# Save the Excel file
excel_filename = "c:\\work\\search_results.xlsx"
wb.save(excel_filename)
print("Search results saved to:", excel_filename)
