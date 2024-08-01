import requests
from bs4 import BeautifulSoup

# URL của trang web cần lấy dữ liệu
url = 'https://sv.ut.edu.vn/lich-theo-tuan.html'

# Lấy nội dung trang web
response = requests.get(url)
html_content = response.text

# Phân tích cú pháp HTML
soup = BeautifulSoup(html_content, 'html.parser')
# Trích xuất thông tin (ví dụ: lấy tiêu đề)
title = soup.title.string

# In thông tin
print(f'Tiêu đề trang web: {title}')
