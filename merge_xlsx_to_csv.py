import pandas as pd
import openpyxl
import os
import sys

def process_xlsx(input_file, output_folder):
    # 获取输入文件名（不包括扩展名）
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    # 读取Excel文件
    workbook = openpyxl.load_workbook(input_file, read_only=True)
    
    # 获取所有工作表名称
    all_sheets = workbook.sheetnames
    
    # 筛选出以'W'开头并后跟数字的工作表
    w_sheets = [sheet for sheet in all_sheets if sheet.startswith('W') and sheet[1:].isdigit()]
    
    # 按数字顺序排序工作表
    w_sheets.sort(key=lambda x: int(x[1:]))
    
    # 处理每个工作表
    for sheet in w_sheets:
        df = pd.read_excel(input_file, sheet_name=sheet)
        
        # 保存单个工作表为CSV
        single_output_file = os.path.join(output_folder, f"{base_name}_{sheet}.csv")
        df.to_csv(single_output_file, index=False, encoding='utf-8-sig')
        
        # 删除CSV文件的前两行
        with open(single_output_file, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
        with open(single_output_file, 'w', encoding='utf-8-sig') as f:
            f.writelines(lines[2:])
        
        print(f"已将工作表 {sheet} 保存为 {single_output_file}，并删除了前两行")
    
    print(f"已处理文件 {input_file}")
    print(f"已处理以下工作表: {', '.join(w_sheets)}")
    print("------------------------")

def process_all_xlsx(input_file):
    # 创建输出文件夹
    output_folder = 'output_csv'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    if not os.path.exists(input_file):
        print(f"找不到指定的Excel文件：{input_file}")
        return
    
    process_xlsx(input_file, output_folder)
    
    print(f"已处理Excel文件：{input_file}")
    print(f"所有CSV文件已保存到 {os.path.abspath(output_folder)} 文件夹中。")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供Excel文件的路径作为参数。")
    else:
        input_file = sys.argv[1]
        process_all_xlsx(input_file)