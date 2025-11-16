import matplotlib.pyplot as plt
import pandas as pd

#--------graph1-----------

df = pd.read_csv("Goleta_Zoning_Permits.csv")

df["Name"] = df["First Name"].str.capitalize() + " " + df["Last Name"].str.capitalize()

count = df["Name"].value_counts().sort_values() #56 people
print(type(count))

# count_topten = count[46:56:][:]
# print(count_topten)

bar_height = 0.7
bar_color = "#307473"

fig = plt.Figure(figsize=(20, 10))

graph1 = plt.barh(count.index, count.values, height=bar_height, color=bar_color, align='center')
# #
plt.title("Most people who have requested a permit")
plt.xlabel("Permits Requested")
plt.ylabel("people")

plt.xticks(fontsize = 6)
plt.yticks(fontsize = 3)

#plt.ylim(len(count) - 11, len(count)) #top 10
# #
count_topten = count[46:56:][:]
name_dict = dict(count_topten)
# #
# ax.bar_label(count_topten.item)
 # plt.text(0.3, 20, "Lonnei Roy", fontsize = 10)

# for name in name_dict:
#     print(name)
 #     x_pos = 20
#     y_pos = 0 #starting
#     plt.text(x_pos, name, name, fontsize = 10)
#     y_pos += bar_height

plt.show()