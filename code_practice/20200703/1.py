# 生成式（推导式）的用法
# prices = {
#     'ZXC': 265,
#     'SAD': 2456,
#     'IQW': 114,
#     'WE': 452,
#     'NH': 5254,
#     'RTG': 254,
#     'YIKI': 254
# }
# # 用股票价格大于100元的股票构造一个新的字典
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)

# 嵌套的列表
# names = ['Jason','jackson','mary','gray']
# courses = ['Computer science','Chinese','Math']
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'please input the {course} [scores] of {name}: '))
#         print(scores)

# heapq模块（堆排序）
# import heapq

# list1 = [34, 25, 12, 45, 48, 78]
# list2 = [
#     {'name':'Jason', 'gender':'male', 'height':185},
#     {'name':'Allen', 'gender':'male', 'height':175},
#     {'name':'Mary','gender':'female','height':165},
#     {'name':'Jane','gender':'female','height':170}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nlargest(2, list2, key=lambda x: x['height']))

#collections模块
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
