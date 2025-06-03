class Task:
    def __init__(self, date_start, date_end, description):
        self.Date_start = date_start
        self.Date_end = date_end
        self.Description = description

list = [
    Task("19.05.2025", "20.05.2025", "Математика"),
    Task("20.05.2025", "20.05.2025", "Физкультура"),
    Task("20.05.2025", "21.05.2025", "История"),
    Task("21.05.2025", "22.05.2025", "Физика"),
    Task("22.05.2025", "23.05.2025", "Информационные технологии")
]

latest_task = list[0]
for task in list:
    if task.Date_end > latest_task.Date_end:
        latest_task = task

print("Занятие, заканчивающиеся позже всех: ", latest_task.Description, latest_task.Date_start, latest_task.Date_end)