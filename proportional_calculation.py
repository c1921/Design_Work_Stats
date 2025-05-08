import sys
import re

def normalize_separator(line):
    """
    将输入中的所有横线符号替换为统一的 `—`
    """
    return re.sub(r'[-—–]', '—', line)

def print_usage():
    """
    打印使用说明
    """
    print("\n使用说明：")
    print("1. 每行输入4个数字，用横线分隔（支持 - 或 — 或 – 符号）")
    print("2. 示例格式：1-2-3-4 或 1—2—3—4")
    print("3. 输入完成后按 Ctrl+Z (Windows) 或 Ctrl+D (Unix) 结束输入")
    print("4. 程序将计算每列数字的总和\n")

def validate_line(line, line_number):
    """
    验证输入行格式并返回错误信息
    """
    normalized_line = normalize_separator(line)
    parts = normalized_line.split('—')
    
    if len(parts) != 4:
        return f"错误（第{line_number}行）：格式不正确，每行必须包含4个数字"
    
    try:
        nums = list(map(int, parts))
        return None
    except ValueError:
        return f"错误（第{line_number}行）：包含非数字字符"

def main():
    print_usage()
    
    # 读取所有输入行
    lines = [line.strip() for line in sys.stdin if line.strip()]
    
    if not lines:
        print("错误：没有输入数据")
        return

    # 初始化总和列表，改为4个元素
    sums = [0, 0, 0, 0]
    valid_lines = 0

    for i, line in enumerate(lines, 1):
        error = validate_line(line, i)
        if error:
            print(error)
            continue
            
        normalized_line = normalize_separator(line)
        nums = list(map(int, normalized_line.split('—')))
        # 累加各部分数值
        for j in range(4):
            sums[j] += nums[j]
        valid_lines += 1

    if valid_lines > 0:
        print("\n计算结果：")
        result = '—'.join(map(str, sums))
        print(result)
        print(f"\n成功处理 {valid_lines} 行数据")
    else:
        print("\n没有有效的数据行可以计算")

if __name__ == "__main__":
    main()