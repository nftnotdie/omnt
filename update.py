import json
from datetime import datetime

def update_status_json():
    # 读取当前时间的分钟
    current_minute = datetime.now().minute

    # 读取data/status.json的内容
    with open('data/status.json', 'r') as file:
        data = json.load(file)

    # 如果当前分钟是5的整数倍，则更新data/status.json的内容
    if current_minute % 2 == 0:
        data['status'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 将更新后的内容写回data/status.json
        with open('data/status.json', 'w') as file:
            json.dump(data, file, indent=2)

if __name__ == "__main__":
    update_status_json()
