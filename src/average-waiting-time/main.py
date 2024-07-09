customers = [[1, 2], [2, 5], [4, 3]]

arrival_time_0 = customers[0]
arrival_time_1 = customers[1]
arrival_time_2 = customers[2]

print(arrival_time_0)

customer0_finish = arrival_time_0[0] + arrival_time_0[1]
customer0_wait = customer0_finish - arrival_time_0[0]


customer1_finish = customer0_finish + arrival_time_1[1]
customer1_wait = customer1_finish - arrival_time_1[0]


customer2_finish = customer1_finish + arrival_time_2[1]
customer2_wait = customer2_finish - arrival_time_2[0]

print(customer0_finish)
print(customer0_wait)
print(customer1_finish)
print(customer1_wait)
print(customer2_finish)
print(customer2_wait)

print((customer0_wait + customer1_wait + customer2_wait) / len(customers))


def averageWaitingTime(customers):  # type: ignore
    current = 0
    total = 0
    for arrival, time in customers:  # type: ignore
        if current < arrival:
            current = arrival  # type: ignore
        finish = current + time  # type: ignore
        wait = finish - arrival  # type: ignore
        total = total + wait  # type: ignore
        current = finish  # type: ignore
        print(finish, wait, total, current)  # type: ignore

    average = total / len(customers)  # type: ignore
    return average  # type: ignore


print(averageWaitingTime(customers))
print()
print(averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]))
