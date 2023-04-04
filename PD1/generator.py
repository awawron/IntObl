import random


def generate_input(machine_count, job_count, random_length=False):
    re = []
    machine_count -= 1  # so there is n machines instead of n+1
    for i in range(job_count):
        job = []
        if random_length:
            length = random.randint(0, machine_count) + 1
            biggest = 0
            counter = 1
            for j in range(length):
                machine = random.randint(biggest, machine_count -
                                         length + counter)
                job.append((machine, random.randint(1, 20)))
                biggest = machine + 1
                counter += 1
        else:
            for j in range(machine_count + 1):
                job.append((j, random.randint(1, 20)))

        re.append(job)

    return re


# check = generate_input(20, 20, True)
# for i in check:
#     print(i)

m1 = generate_input(10, 10, False)
# m2 = generate_input(12, 8, True)
# m3 = generate_input(10, 10, True)

l1 = generate_input(20, 20, False)
# l2 = generate_input(20, 30, True)
# l3 = generate_input(20, 20, True)

# all_inputs = [m1, m2, m3, l1, l2, l3]
all_inputs = [m1, l1]
with open('input.txt', 'w') as f:
    for i in all_inputs:
        for j in i:
            f.write(str(j))
        f.write("\nlmao\n")
