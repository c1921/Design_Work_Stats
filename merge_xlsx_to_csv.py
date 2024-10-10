import pandas as pd
import openpyxl
import os
import glob

def process_xlsx(input_file):
    # 获取输入文件名（不包括扩展名）
    base_name = os.path.splitext(input_file)[0]
    merged_output_file = f"{base_name}.csv"
    
    # 读取Excel文件
    workbook = openpyxl.load_workbook(input_file, read_only=True)
    
    # 获取所有工作表名称
    all_sheets = workbook.sheetnames
    
    # 筛选出以'W'开头并后跟数字的工作表
    w_sheets = [sheet for sheet in all_sheets if sheet.startswith('W') and sheet[1:].isdigit()]
    
    # 按数字顺序排序工作表
    w_sheets.sort(key=lambda x: int(x[1:]))
    
    # 读取并处理工作表
    dfs = []
    for sheet in w_sheets:
        df = pd.read_excel(input_file, sheet_name=sheet)
        
        # 保存单个工作表为CSV并删除前两行
        single_output_file = f"{base_name}_{sheet}.csv"
        df.to_csv(single_output_file, index=False, encoding='utf-8-sig')
        
        # 删除单个工作表CSV文件的前两行
        with open(single_output_file, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
        with open(single_output_file, 'w', encoding='utf-8-sig') as f:
            f.writelines(lines[2:])
        
        print(f"已将工作表 {sheet} 保存为 {single_output_file}，并删除了前两行")
        
        # 为合并准备数据
        df = pd.concat([df, pd.DataFrame([{}])], ignore_index=True)
        df = pd.concat([df, pd.DataFrame([{'时间': f'===={sheet}===='}])], ignore_index=True)
        dfs.append(df)
    
    # 合并所有数据框
    merged_df = pd.concat(dfs, ignore_index=True)
    
    # 导出合并后的CSV文件
    merged_df.to_csv(merged_output_file, index=False, encoding='utf-8-sig')
    
    # 删除合并CSV文件的前两行
    with open(merged_output_file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    with open(merged_output_file, 'w', encoding='utf-8-sig') as f:
        f.writelines(lines[2:])
    
    print(f"已处理文件 {input_file}")
    print(f"已合并以下工作表: {', '.join(w_sheets)}")
    print(f"合并结果已导出为 {merged_output_file}，并删除了前两行，添加了工作表分隔标记")
    print("------------------------")

def process_all_xlsx():
    # 获取当前目录下所有的xlsx文件
    xlsx_files = glob.glob("*.xlsx")
    
    if not xlsx_files:
        print("当前目录下没有找到xlsx文件。")
        return
    
    for xlsx_file in xlsx_files:
        process_xlsx(xlsx_file)
    
    print(f"共处理了 {len(xlsx_files)} 个xlsx文件。")

if __name__ == "__main__":
    process_all_xlsx()