import pandas as pd


file_path = './data/fourth_task.txt'
df = pd.read_csv(file_path)

average_price = df['price'].mean()
max_price = df['price'].max()
min_rating = df['rating'].min()

with open('fourth_task_results.txt', 'w', encoding="utf-8") as f:
    f.write(f"Средняя цена {average_price}\n")
    f.write(f"Максимальная цена {max_price}\n")
    f.write(f"Минимальный рейтинг {min_rating}")

filtered_df = df[df['status'] == 'Awaiting Review']

output_file_path = 'fourth_task_modified_data.csv'
filtered_df.to_csv(output_file_path, index=False)