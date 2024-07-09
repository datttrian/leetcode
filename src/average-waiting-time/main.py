customers = [[1, 2], [2, 5], [4, 3]]

arrival_time_0 = customers[0]
arrival_time_1 = customers[1]
arrival_time_2 = customers[2]

print(arrival_time_0)

time_customer_0 = arrival_time_0[0] + arrival_time_0[1]
print(time_customer_0)

print(time_customer_0 + arrival_time_1[1] - arrival_time_1[0])
