import pandas as pnds
import matplotlib.pylab as plt
import seaborn as sns

# fetch data

data = pnds.read_csv("data.csv")
data = pnds.DataFrame(data) #* convert data to data frame
data["price"] = data["price"].str.replace("$", "").str.replace(",", "").astype(float) #* convert type price data to float and remove ($, ,) from prices

# create charts

fig, axs = plt.subplots(4,1, figsize=(8,10)) #? split and scale charts

sns.histplot(data["price"], bins=48, kde=True, ax=axs[0])
axs[0].set_title("Price Distribution")

sns.scatterplot(x="property_type", y="price", data=data, ax=axs[1])
axs[1].set_title("property_type vs. Price")

sns.scatterplot(x="neighbourhood", y="price", data=data, ax=axs[2])
axs[2].set_title("Location vs. Price")

sns.scatterplot(x="availability_365", y="price", data=data, ax=axs[3])
axs[3].set_title("Availability vs. Price")
axs[3].set_xlabel("Days")
axs[3].set_ylabel("Price")

plt.show() #! show charts