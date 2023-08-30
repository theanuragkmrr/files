# # with open("weather_data.csv","r") as data:
# #     print(data.readlines())
# # import csv
# #
# # with open("weather_data.csv") as data:
# #     d=csv.reader(data)
# #     temp=[]
# #     for row in d:
# #         if row[1]!="temp":
# #             temp.append(int(row[1]))
# #         # print(row[1])
# #     print(temp)
# import pandas
#
# data=pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# # data_dict=data.to_list()
# # print(data_dict)
#
# # temp=data["temp"].max()
# # print(temp)
# # data in a row
# # print(data[data.temp==temp])
#
# # monday=data[data.day=="Monday"]
# # print(monday.condition)
# # print(data["temp"])
# # fahrenheite=(monday.temp*1.8)+32
# # print(fahrenheite)
# data_dict={
#     "students":['Anurag','Anshika','Jatin','Saurabh'],
#     "scores":[34,35,80,50]
# }
# data=pandas.DataFrame(data_dict)
# print(data)
#
# # data_dict ko csv file me convert kr du
# data.to_csv("scores.csv")
#
#
import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey=len(data[data["Primary Fur Color"]=="Gray"])
Cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])
Black=len(data[data["Primary Fur Color"]=="Black"])
print(grey)
print(Cinnamon)
print(Black)
data_dict={
    "Fur color":['Greay','Red','Black'],
    "Count":[grey,Cinnamon,Black]
}
d=pandas.DataFrame(data_dict)
d.to_csv("Scoress.csv")