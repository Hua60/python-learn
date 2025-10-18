import json

# 读取数据文件
f = open("D:/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]

print("前10个省份名称和确诊人数：")
for i, province_data in enumerate(province_data_list[:10]):
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    print(f"{i+1}. '{province_name}': {province_confirm}")

