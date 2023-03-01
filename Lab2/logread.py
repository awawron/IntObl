with open("log.txt", "r") as file:
    logs = file.read().split(" ")

def filter_logs(logs):
    re = []
    for log in logs:
        if log == '\n' or log == '':
            pass
        else:
            re.append(log)
    return re

filtered = filter_logs(logs)

i = 0
time = 0
generations = 0
counter = 0
for item in filtered:
    counter += 1
    if i == 0 or i == 1:
        i += 1
        time += float(item)
    elif i == 2:
        generations += int(item)
        i = 0

avg_time = time / counter
avg_gens = generations / counter

print(avg_time)
print(avg_gens)