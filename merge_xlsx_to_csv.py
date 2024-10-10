import pandas as pd
import openpyxl
import os
import glob

def merge_xlsx_to_csv(input_file):
    # 获取输入文件名（不包括扩展名）
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.csv"
    
    # 读取Excel文件
    workbook = openpyxl.load_workbook(input_file, read_only=True)
    
    # 获取所有工作表名称
    all_sheets = workbook.sheetnames
    
    # 筛选出以'W'开头并后跟数字的工作表
    w_sheets = [sheet for sheet in all_sheets if sheet.startswith('W') and sheet[1:].isdigit()]
    
    # 按数字顺序排序工作表
    w_sheets.sort(key=lambda x: int(x[1:]))
    
    # 读取并合并工作表
    dfs = []
    for sheet in w_sheets:
        df = pd.read_excel(input_file, sheet_name=sheet)
        dfs.append(df)
    
    # 合并所有数据框
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # 导出为CSV文件
    merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    # 删除CSV文件的前两行
    with open(output_file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    with open(output_file, 'w', encoding='utf-8-sig') as f:
        f.writelines(lines[2:])
    
    print(f"已处理文件 {input_file}")
    print(f"已合并以下工作表: {', '.join(w_sheets)}")
    print(f"结果已导出为 {output_file}，并删除了前两行")
    print("------------------------")

def process_all_xlsx():
    # 获取当前目录下所有的xlsx文件
    xlsx_files = glob.glob("*.xlsx")
    
    if not xlsx_files:
        print("当前目录下没有找到xlsx文件。")
        return
    
    for xlsx_file in xlsx_files:
        merge_xlsx_to_csv(xlsx_file)
    
    print(f"共处理了 {len(xlsx_files)} 个xlsx文件。")

if __name__ == "__main__":
    process_all_xlsx()