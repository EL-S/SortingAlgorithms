from random import randint

lst = [69, 27, 56, 51, 35, 52, 14, 39, 57, 89, 29, 94, 30, 63, 73, 76, 37, 3, 34, 19, 31, 96, 17, 83, 11, 61, 65, 82, 5, 40, 88, 1, 6, 71, 44, 55, 85, 95, 42, 2, 45, 79, 70, 36, 22, 93, 23, 97, 26, 49, 48, 67, 80, 50, 62, 25, 92, 20, 21, 68, 60, 72, 9, 43, 74, 81, 64, 84, 87, 75, 24, 15, 100, 8, 53, 18, 66, 38, 28, 54, 91, 10, 98, 86, 59, 99, 16, 47, 13, 41, 77, 32, 58, 33, 7, 46, 90, 78, 4, 12]

def move_pivot_to_end():
    global sorted_list
    pivot = sorted_list[pivot_index]
    swap(pivot_index, -1)
    return pivot

def swap(index1, index2):
    global sorted_list
    value1 = lst[index1]
    value2 = lst[index2]
    sorted_list[index1] = value2
    sorted_list[index2] = value1
    
def swap_if_bigger(index1, index2):
    global sorted_list
    value1 = sorted_list[index1]
    value2 = sorted_list[index2]
    if value1 > value2:
        sorted_list[index1] = value2
        sorted_list[index2] = value1
        return True
    return False

pivot_index = randint(0,len(lst)-1)

sorted_list = lst

pivot = move_pivot_to_end()

print(pivot)

while True:
    for i in range(pivot_index+1):
        left_item = sorted_list[i]
        if left_item > pivot:
            left_index = i
            break
    for i in range(pivot_index,len(sorted_list),-1):
        right_item = sorted_list[i]
        if right_item < pivot:
            right_index = i
            break
    try:
        print(left_index)
        print(right_index)
        status = swap_if_bigger(left_index, right_index)
    except:
        pass
    print(sorted_list)



print(pivot)
print(sorted_list)


print(lst)
