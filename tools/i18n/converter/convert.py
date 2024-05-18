import json

# 讀取 zh_CN.json 檔案
with open('zh_CN.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 提取 zh_CN.json 的鍵,並在前後加上雙引號
keys = [json.dumps(key, ensure_ascii=False) for key in data.keys()]

# 將鍵寫入 zh_CN.txt 文字檔,每個鍵佔一行
with open('zh_CN.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(keys))

# 驗證 zh_CN.txt 的每一行內容都在 zh_CN.json 中存在,並且是作為鍵存在的
fail_count = 0
with open('zh_CN.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        key = line.strip()
        if json.loads(key) not in data:
            print(f"驗證失敗: {key} 不存在於 zh_CN.json 中")
            fail_count += 1
        else:
            print(f"驗證成功: {key} 存在於 zh_CN.json 中")

# 顯示驗證失敗次數
print(f"\n驗證完成,總共有 {fail_count} 次驗證失敗")

# 讀取 TW.json 檔案
with open('TW.json', 'r', encoding='utf-8') as file:
    data_TW = json.load(file)

# 提取 TW.json 的值,並在前後加上雙引號
values_TW = [json.dumps(value, ensure_ascii=False) for value in data_TW.values()]

# 將值寫入 TW.txt 文字檔,每個值佔一行
with open('TW.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(values_TW))

# 驗證 TW.txt 的每一行內容都在 TW.json 中存在,並且是作為值存在的
fail_count_TW = 0
with open('TW.txt', 'r', encoding='utf-8') as file:
    lines_TW = file.readlines()
    for line in lines_TW:
        value = line.strip()
        if json.loads(value) not in data_TW.values():
            print(f"驗證失敗: {value} 不存在於 TW.json 中")
            fail_count_TW += 1
        else:
            print(f"驗證成功: {value} 存在於 TW.json 中")

# 顯示 TW.json 驗證失敗次數
print(f"\nTW.json 驗證完成,總共有 {fail_count_TW} 次驗證失敗")

# 讀取 zh_CN.txt 文字檔
with open('zh_CN.txt', 'r', encoding='utf-8') as file1:
    zh_CN_lines = file1.readlines()

# 讀取 TW.txt 文字檔
with open('TW.txt', 'r', encoding='utf-8') as file2:
    TW_lines = file2.readlines()

# 結合 zh_CN_lines 和 TW_lines 的內容
combined_lines = [f'{zh_CN_line.strip()}: {TW_line.strip()}' for zh_CN_line, TW_line in zip(zh_CN_lines, TW_lines)]

# 將結合後的內容寫入 zh_TW.json 檔案,使其成為有效的JSON格式
with open('zh_TW.json', 'w', encoding='utf-8') as output_file:
    output_file.write('{\n')
    output_file.write(',\n'.join(['  ' + line for line in combined_lines]))
    output_file.write('\n}')

