task_types = [
    ["Program Logic / Coding", 6],
    ["UI / Output Formatting", 3],
    ["Testing & Debugging", 2],
    ["Documentation / README", 2],
    ["Presentation Slides", 2]
]

project_title = input("Project : ")
group_name = input("Group : ")

print(" ")
print("==========================================")
print("COM 103 PROJECT -- TASK TYPES")
print("==========================================")

for i in range(len(task_types)):
    task = task_types[i]
    print(str(i + 1) + ". " + task[0] + " [" + str(task[1]) + "h]")

print("==========================================")
print(" ")

assignments = []

for i in range(4):
    print("--- TASK " + str(i + 1) + " ---")
    task_number = input("Task number (0 to skip): ")

    if task_number == "0":
        print(" ")

    elif task_number == "1" or task_number == "2" or task_number == "3" or task_number == "4" or task_number == "5":
        member_name = input("Member name: ")
        status = input("Status (done/pending): ")

        selected_task = task_types[int(task_number) - 1]
        task_name = selected_task[0]
        task_hours = selected_task[1]

        if status == "done":
            points = 2
        elif status == "pending":
            points = 1
        else:
            points = 1

        assignments.append([task_name, task_hours, member_name, status, points])
        print(" ")

    else:
        print("Invalid task number.")
        print(" ")

total_earned = 0
for i in range(len(assignments)):
    task = assignments[i]
    total_earned = total_earned + task[4]

max_possible = 2 * len(assignments)

if max_possible > 0:
    progress = int((total_earned / max_possible) * 100)
else:
    progress = 0

if progress >= 75:
    project_status = "PROJECT READY!"
elif progress >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"

print("================================================")
print(project_title + " -- TASK BOARD")
print("================================================")
print("Project : " + project_title)
print("Group : " + group_name)
print("------------------------------------------------")

for i in range(len(assignments)):
    task = assignments[i]
    print("[" + str(i + 1) + "] " + task[0] + " [" + str(task[1]) + "h]")
    print("Assigned to : " + task[2])
    print("Status : " + task[3])
    print("Points : " + str(task[4]) + " / 2")
    print(" ")

print("------------------------------------------------")
print("Points Earned : " + str(total_earned) + " / " + str(max_possible))
print("Progress : " + str(progress) + "%")
print("Project Status : " + project_status)
print("================================================")