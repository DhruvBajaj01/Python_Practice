# given a target sum and an array of digits
# choose the least number of digits which adds on to make the target_sum
# each digit can be used any number of times

def best_sum(target, array, table):
    table[0] = []
    for i in range(len(table)):
        if(table[i] != None):
            for j in array:
                combination = [*table[i], j]
                try:
                    if(table[i+j] == None or len(table[i+j]) > len(combination)):
                        table[i+j] = combination
                except:
                    continue
    return(table[target])


target = int(input("Enter target sum: "))
array = list(
    map(int, input("Enter space separated values for array: ").split()))
table = []
for i in range(target+1):
    table.append(None)

print("least number of coins required to get the combination:",
      best_sum(target, array, table))
