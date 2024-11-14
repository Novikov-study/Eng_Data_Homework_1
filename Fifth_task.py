import pandas as pd
from bs4 import BeautifulSoup

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def parse_html_to_table(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    return pd.read_html(str(table))[0]

def save_df_to_csv(df, output_path):
    df.to_csv(output_path, index=False)


input_path = './data/fifth_task.html'
output_path = 'fifth_task_result.csv'

html_content = read_html_file(input_path)
df = parse_html_to_table(html_content)
save_df_to_csv(df, output_path)


