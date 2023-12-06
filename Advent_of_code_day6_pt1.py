def clear_data(data):
    while True:
        if "" in data:
            data.remove("")
        else:
            break
    data = list(map(int,data))
    return data
data1 = clear_data(open("input.txt").read().split("\n")[0].split(":")[1].split(" "))
data2 = clear_data(open("input.txt").read().split("\n")[1].split(":")[1].split(" "))

index_to_distance = {}
for i in range(len(data1)):
    index_to_distance[i]= data2[i]
def get_distance(time,total):
    return (total-time)*time
ways = 1
for i in range(len(data1)):
    wins = 0
    z = data1[i]
    for y in range(z + 1):
        if get_distance(y,z) > index_to_distance[i]:
            wins +=1
    ways = ways * wins

print(ways)





