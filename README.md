# Excel数据处理与统计工具

## 项目简介

这是一个用于处理Excel文件并生成统计报告的Python工具。它可以将Excel文件中的特定工作表转换为CSV文件，然后分析这些CSV文件并生成详细的统计报告。

## 主要功能

1. 将Excel文件中以'W'开头的工作表转换为CSV文件
2. 分析CSV文件，统计每个对接人每周的工作情况
3. 生成包含详细统计信息的报告

## 使用方法

1. 运行主程序：

   ```bash
   python main.py
   ```

2. 在弹出的文件选择器中选择要处理的Excel文件

3. 程序将自动执行以下步骤：
   - 清理输出文件夹
   - 将Excel文件中的特定工作表转换为CSV文件
   - 分析CSV文件并生成统计报告

4. 查看生成的统计报告（文件名格式：`{excel文件名}_stats_result.txt`）

## 文件说明

- `main.py`: 主程序，协调整个处理流程
- `merge_xlsx_to_csv.py`: 将Excel文件转换为CSV文件
- `csv_handler_stats_analyzer.py`: 分析CSV文件并生成统计报告

## 统计内容

- 每个对接人每周的工作类型数量（新、改、套、修、出差）
- 每个对接人每周参与的项目及次数

## 注意事项

- 确保Excel文件中包含以'W'开头并后跟数字的工作表
- 统计结果将保存在与输入Excel文件同名的文本文件中
- 中间生成的CSV文件将保存在`output_csv`文件夹中

## 环境要求

- Python 3.x
- 需要安装以下Python库：
  - pandas
  - openpyxl
  - tkinter（通常已包含在Python标准库中）

## 安装依赖

运行以下命令安装所需的Python库：

```bash
pip install pandas openpyxl
```
