import csv
from collections import defaultdict
import glob

# 初始化一个嵌套的defaultdict来存储每个对接人每周的统计数据
stats = defaultdict(lambda: defaultdict(lambda: {'新': 0, '改': 0, '套': 0, '修': 0, '出差': 0}))

# 获取所有CSV文件
csv_files = glob.glob('2024.9_W*.csv')

for file in csv_files:
    # 从文件名中提取周数
    week = file.split('_W')[1].split('.csv')[0]
    
    # 读取CSV文件
    with open(file, 'r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        
        for row in csv_reader:
            # 获取对接人
            handler = row['对接人']
            
            # 统计各项数据
            for category in ['新', '改', '套', '修', '出差']:
                value = row.get(category, '0')
                if value.isdigit():
                    stats[handler][week][category] += int(value)

# 打印统计结果
print("每个对接人每周的统计数据:")
for handler, weeks_data in stats.items():
    print(f"\n对接人: {handler}")
    for week, data in weeks_data.items():
        print(f"  第{week}周:")
        for category, count in data.items():
            print(f"    {category}: {count}")