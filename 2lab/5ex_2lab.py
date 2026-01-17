with open("5ex.txt", encoding="utf-8") as f:
    N = int(f.readline().strip())
    dates = []
    names = []
    costs = []

    for i in range(N):
        line = f.readline().strip()
        if not line:
            continue
        date, name, cost = line.split()
        dates.append(date)
        names.append(name)
        costs.append(int(cost))

count_list = {}
for i in range(N):
    if count_list.get(names[i]) == None:
        count_list.update({names[i]:1})
    else:
        new_val = count_list.get(names[i]) + 1
        count_list.update({names[i]: new_val})

sorted_count_list = sorted(count_list.items(), key=lambda item: item[1], reverse=True)

sum_for_dates = {}

for i in range(N):
    if sum_for_dates.get(dates[i]) == None:
        sum_for_dates.update({dates[i]:costs[i]})
    else:
        new_val = sum_for_dates.get(dates[i]) + costs[i]
        sum_for_dates.update({dates[i]: new_val})

sorted_dates = sorted(sum_for_dates.items())

max_cost = 0
max_index = 0
for i in range(N):
    if costs[i] > max_cost:
        max_cost = costs[i]
        max_index = i

print()
print("Счетчик купленных пицц:")
for name, count in sorted_count_list:
    print(f"{count} - {name}.")

print()
print("Суммарная стоимость по дням:")
for date, total in sorted_dates:
    print(f"{date}: {total} руб.")

print()
print("Самый дорогой заказ:")
print(dates[max_index] + " " + names[max_index] + " " + str(costs[max_index]))

print()
print("Средняя стоимость по всем заказам:")
print("{:.2f}".format(sum(costs)/N))