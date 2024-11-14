def read_file():
    with open("./data/third_task.txt", encoding="utf-8") as file:
        lines = file.readlines()
        table = []
        for line in lines:
            words = line.strip().split(" ")
            table.append(words)
        return table

def change_na(table):

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "N/A":
                table[i][j] = (table[i][j-1] + int(table[i][j-1])) / 2
            else:
                table[i][j] = int(table[i][j])

def filter_table(table):
    result = []
    for row in table:
        count = 0
        sum = 0
        for num in row:
            if num % 5 == 0:
                count += 1
                sum += num
        if count > 0:
            result.append(sum / count)
        else:
                result.append("")

    return result

def write_results(result):
    with open("third_task_result.txt", "w", encoding="utf-8") as file:
        for res in result:
            file.write(f"{res}\n")









table = read_file()
change_na(table)
result = filter_table(table)
print(result)
write_results(result)