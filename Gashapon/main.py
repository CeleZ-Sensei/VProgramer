import random

def datalist():
    # ID:Percent
    droprate  = {1:18, 2:18, 3:18, 4:15, 5:15, 6:6, 7:6, 8:4}
    datalist = []

    len_droprate = len(droprate)
    for i in range(1, len_droprate+1):
        var = droprate[i]
        for y in range(1, var+1):
            datalist.append(i);

    return datalist

def main():
    mapping = {1:"รีดีม1", 2:"รีดีม2", 3:"รีดีม3", 4:"รีดีม4", 5:"รีดีม5", 6:"รีดีม6", 7:"รีดีม7", 8:"รีดีม8"}
    data = datalist()
    index = random.randint(0, 99)
    random.shuffle(data)
    data_id = data[index]
    print("ID:", mapping[data_id])

main()
