# 讀取 zh_CN.txt 文字檔
with open('zh_CN.txt', 'r', encoding='utf-8') as file1:
    zh_CN_line = file1.readlines()

# 讀取 TW.txt 文字檔
with open('TW.txt', 'r', encoding='utf-8') as file2:
    TW_line = file2.readlines()

# 結合 zh_CN_line 和 TW_line 的內容
combined_lines = [f'{zh_CN_line.strip()}: {TW_line.strip()}' for zh_CN_line, TW_line in zip(zh_CN_line, TW_line)]

# 將結合後的內容寫入 zh_TW.json 檔案,使其成為有效的JSON格式
with open('zh_TW.json', 'w', encoding='utf-8') as output_file:
    output_file.write('{\n')
    output_file.write(',\n'.join(['  ' + line for line in combined_lines]))
    output_file.write('\n}')

