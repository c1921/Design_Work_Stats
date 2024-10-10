import csv
from collections import defaultdict
import glob
import os
import sys

def save_stats_to_file(stats, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("每个对接人每周的统计数据:\n")
        for handler, weeks_data in stats.items():
            f.write(f"\n对接人: {handler}\n")
            for week, data in sorted(weeks_data.items(), key=lambda x: int(x[0])):
                f.write(f"  第{week}周:\n")
                for category, count in data.items():
                    f.write(f"    {category}: {count}\n")

# 初始化一个嵌套的defaultdict来存储每个对接人每周的统计数据
stats = defaultdict(lambda: defaultdict(lambda: {'新': 0, '改': 0, '套': 0, '修': 0, '出差': 0}))

# 获取output_csv目录下的所有CSV文件
csv_files = glob.glob(os.path.join('output_csv', '*.csv'))

for file in csv_files:
    # 从文件名中提取周数
    week = os.path.basename(file).split('_W')[1].split('.csv')[0]
    
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

# 获取Excel文件名作为前缀
excel_filename = sys.argv[1] if len(sys.argv) > 1 else "default"

# 保存统计结果到文本文件
output_file = f'{excel_filename}_stats_result.txt'
save_stats_to_file(stats, output_file)

print(f"统计结果已保存到 {output_file}")

# 打印统计结果（可选，如果你还想在控制台看到结果）
print("每个对接人每周的统计数据:")
for handler, weeks_data in stats.items():
    print(f"\n对接人: {handler}")
    for week, data in sorted(weeks_data.items(), key=lambda x: int(x[0])):
        print(f"  第{week}周:")
        for category, count in data.items():
            print(f"    {category}: {count}")