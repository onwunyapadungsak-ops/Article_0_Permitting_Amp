import matplotlib.pyplot as plt
import pandas as pd

#graphกูยาวชิบหายเลยวะสัส
#sol1 เปลี่ยนx scale
#sol2 maket the text less longer

#--------Organization Graph-----------

df = pd.read_csv("cleaned_goleta_permits - Goleta_Zoning_Permits.csv")

bar_height = 0.5
bar_color = "#307473"

organization = df["Organization Name"].value_counts().sort_values()
print(organization)

fig = plt.figure(num="Figure", figsize=(10, 5))
ax = fig.add_subplot(111)

# ax.set_xticks([0, 4, 8, 12])
graph2 = plt.barh(organization.index, organization.values, height=bar_height, color=bar_color, align='center')
plt.subplots_adjust(left=0.3)
plt.yticks(fontsize = 5)


plt.title("Company/Organization that requested the most permits")
plt.xlabel("Permits Requested")
plt.ylabel("Company/Organization")

plt.show()