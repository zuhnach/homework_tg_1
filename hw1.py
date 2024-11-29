def make_task():
    dict_task = {}
    for _ in range(3):
        date = input("Введите дату: ")
        task = input("Введите задачу: ")
        dict_task[date] = task
    print(dict_task)
make_task()