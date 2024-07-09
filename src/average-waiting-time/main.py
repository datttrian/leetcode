customers = [[1, 2], [2, 5], [4, 3]]

arrival_time_0 = customers[0]
arrival_time_1 = customers[1]
arrival_time_2 = customers[2]

print(arrival_time_0)

customer0_finish = arrival_time_0[0] + arrival_time_0[1]
print(customer0_finish)

customer1_finish = customer0_finish + arrival_time_1[1]
print(customer1_finish)

customer2_finish = customer1_finish + arrival_time_2[1]
print(customer2_finish)
