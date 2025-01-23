import sys
import re

def normalize_separator(line):
    """
    将输入中的所有横线符号替换为统一的 `—`
    """
    # 匹配所有可能的横线符号（包括 -、—、– 等）
    return re.sub(r'[-—–]', '—', line)

# 读取所有输入行
lines = [line.strip() for line in sys.stdin if line.strip()]

# 初始化总和列表
sums = [0, 0, 0, 0]

for line in lines:
    # 统一分隔符
    normalized_line = normalize_separator(line)
    # 分割每行的数字
    parts = normalized_line.split('—')
    if len(parts) != 4:
        continue  # 忽略格式不正确的行
    try:
        nums = list(map(int, parts))
    except ValueError:
        continue  # 忽略包含非数字的行
    # 累加各部分数值
    for i in range(4):
        sums[i] += nums[i]

# 格式化并输出结果
result = '—'.join(map(str, sums))
print(result)