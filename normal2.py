#Голубева Лидия Ильинична
# Задание-1:
def fibonacci(n, m):
        res = []
        last = 0
        next = 1
        for i in range(m + 1):
            if i >= n: res.append(next)
            last, next = next, next + last
        return res

# Задача-2:
def sort_to_max(origin_list):
    result = origin_list[:]
    for i in range(1, len(origin_list)):
        t = i
        while (result[t] < result[t - 1]) and (t > 0):
            result[t], result[t - 1] = result[t - 1], result[t]
            t -= 1
    return result
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
def filtered_fnctn(function,impl):
    output_impl = []
    for i in range(len(impl)):
        if function(impl[i]) == True:
            output_impl.append(impl[i])
    return output_impl
function = lambda x: type(x) == str
impl = [9, 'bchlr', -22,  56, 'g']
print(filtered_fnctn(function,impl))

# Задача-4:
def parallelogramm(a1,a2,a3,a4):
    def centerspot(a,b):
        return ((a[0]+b[0])/2,(a[1]+b[1])/2)
    if a1 == a3: return False
    return centerspot(a1,a3) == centerspot(a2,a4)