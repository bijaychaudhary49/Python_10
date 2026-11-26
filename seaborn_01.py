import seaborn as sns
import matplotlib.pyplot as plt

ram = sns.load_dataset("iris")

sns.barplot(data=ram, x="species", y="petal_width", palette="deep")

# sns.barplot(data=data, x="subject", y="marks", hue="subject", palette="magma", legend=True)
# plt.xlabel("Subject")
# plt.ylabel("marks")
plt.title("Species vs petal_width")
plt.show()