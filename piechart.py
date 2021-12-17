import matplotlib.pyplot as plt 
import pandas as pd
df = pd.read_csv('wine.data')
country_data =df["country"]
medel_data =df["gold_medel"]
plt.pie(model_data,labels=country_data)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show()
