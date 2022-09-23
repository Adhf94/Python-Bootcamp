# # with open("weather_data.csv", mode="r") as data:
# #     weather_data = []
# #     for datas in data:
# #         weather_data.append(datas.strip("\n''"))
# # print(weather_data)
# # import csv
# #
# # with open("weather_data.csv") as data:
# #     data = csv.reader(data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # # average_temp =round(sum(temp_list) / len(temp_list))
# # # print(average_temp)
# # print(data["temp"].max())
# # print(data[data.temp ==data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# f_temp = (monday_temp * 9/5) + 32
#
# print(f_temp)
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#primary_fur_color = data["Primary Fur Color"]
# print(primary_fur_color)
# primary_fur_color_dic = {
#     "Colors": ["red", "gray", "black"],
#     "Count": [0, 0, 0]
# }

# for color in primary_fur_color:
#     if color == "Gray":
#         primary_fur_color_dic["count"][1] += 1
#     if color == "Cinnamon":
#         primary_fur_color_dic["count"][0] += 1
#     if color == "Black":
#         primary_fur_color_dic["count"][2] += 1

# MANERA USANDO PANDAS ESTRICTAMENTE
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

primary_fur_color_dic = {
    "Colors": ["red", "gray", "black"],
    "Count": [red_squirrels_count, gray_squirrels_count, black_squirrels_count]
}
new_data = pandas.DataFrame(primary_fur_color_dic)
new_data.to_csv("Squirrel_color_count.csv")
print(new_data)
