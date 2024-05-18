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
