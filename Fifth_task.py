import pandas as pd
from bs4 import BeautifulSoup

file_path = './data/fifth_task.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')
df = pd.read_html(str(table))[0]

output_path = 'fifth_task_result.csv'
df.to_csv(output_path, index=False)


