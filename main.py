import subprocess
import sys
import os
import shutil
import tkinter as tk
from tkinter import filedialog

def clear_output_folder(folder_path):
    print(f"正在清除 {folder_path} 文件夹...")
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'清除文件 {file_path} 时出错: {e}')
    else:
        os.makedirs(folder_path)
    print(f"{folder_path} 文件夹已清除。")

def run_script(script_name, *args):
    print(f"正在运行 {script_name}...")
    result = subprocess.run([sys.executable, script_name] + list(args), capture_output=True, text=True)
    if result.returncode != 0:
        print(f"运行 {script_name} 时出错:")
        print(result.stderr)
        sys.exit(1)
    print(result.stdout)
    print(f"{script_name} 运行完成。")

def select_excel_file():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(
        title="选择Excel文件",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    return file_path

def main():
    # 清除output_csv文件夹
    output_folder = 'output_csv'
    clear_output_folder(output_folder)

    # 使用文件选择器获取Excel文件路径
    excel_path = select_excel_file()
    if not excel_path:
        print("未选择文件，程序退出。")
        return

    print(f"选择的文件路径：{excel_path}")

    # 获取Excel文件名（不包括扩展名）
    excel_filename = os.path.splitext(os.path.basename(excel_path))[0]

    # 运行merge_xlsx_to_csv.py，并传入Excel文件路径
    run_script('merge_xlsx_to_csv.py', excel_path)

    # 运行csv_handler_stats_analyzer.py，并传入Excel文件名
    run_script('csv_handler_stats_analyzer.py', excel_filename)

    print(f"统计结果已保存到 {excel_filename}_stats_result.txt 文件中，请查看。")

if __name__ == "__main__":
    main()