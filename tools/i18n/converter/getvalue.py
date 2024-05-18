import json

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
