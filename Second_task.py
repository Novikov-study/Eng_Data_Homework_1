def read_file():
    with open("./data/second_task.txt", encoding="utf-8") as file:
        lines = file.readlines()
        table = []
        for line in lines:
            words = line.strip().split(" ")
            table.append(list(map(int, words)))
        return table

def sum_negative_nums(table):
    result = []
    for row in table:
        negative_sum = 0
        for num in row:
            if num < 0:
                negative_sum += num
        result.append(abs(negative_sum))
    return result

def mid_sum(result):
        return sum(result) / len(result) if result else 0

def write_results(result):
    with open("second_task_result.txt", "w", encoding="utf-8") as file:
        for res in result:
            file.write(f"{res}\n")
        file.write("___\n")
        average = mid_sum(result)
        file.write(f"{average}\n")

table = read_file()
negative_sums = sum_negative_nums(table)
write_results(negative_sums)









