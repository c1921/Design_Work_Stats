import subprocess
import sys
import os

def run_script(script_name):
    print(f"正在运行 {script_name}...")
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"运行 {script_name} 时出错:")
        print(result.stderr)
        sys.exit(1)
    print(result.stdout)
    print(f"{script_name} 运行完成。")

def main():
    # 确保output_csv文件夹存在
    if not os.path.exists('output_csv'):
        os.makedirs('output_csv')

    # 运行merge_xlsx_to_csv.py
    run_script('merge_xlsx_to_csv.py')

    # 运行csv_handler_stats_analyzer.py
    run_script('csv_handler_stats_analyzer.py')

if __name__ == "__main__":
    main()