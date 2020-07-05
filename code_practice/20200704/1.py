# # 简单排序算法
# def select_sort(items, comp=lambda x,y:x<y)
#     items = items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i+1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items

'算法'
'''穷举法'''
fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5
    
