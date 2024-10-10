import csv
from collections import defaultdict

# 初始化一个嵌套的defaultdict来存储每个对接人的统计数据
stats = defaultdict(lambda: {'新': 0, '改': 0, '套': 0, '修': 0, '出差': 0})

# 读取CSV文件
with open('2024.9.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # 获取对接人
        handler = row['对接人']
        
        # 统计各项数据
        for category in ['新', '改', '套', '修', '出差']:
            value = row.get(category, '0')
            if value.isdigit():
                stats[handler][category] += int(value)

# 打印统计结果
print("每个对接人的统计数据:")
for handler, data in stats.items():
    print(f"\n对接人: {handler}")
    for category, count in data.items():
        print(f"{category}: {count}")