import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4]
# y = [1,4,9,16]
# plt.plot(x, y, "o--g")
# #matplotlib style yazıp oradaki veriler ile görselleştirebiliriz.
# plt.axis([0,6,0,20]) #x sınırlarını 0dan 6 ya y sınırlarını 0dan 20ye sınırlar.
#
# plt.title("Graphic Title")
# plt.xlabel("X label")
# plt.ylabel("Y label")

# x = np.linspace(0,2,100)
# plt.plot(x , x , label = "linear" , color = "red")
# plt.plot(x , x**2, label = "quadratic",color = "green")
# plt.plot(x, x**3, label = "qubic", color = "yellow")
#
# plt.title("Title")
# plt.xlabel("X label")
# plt.ylabel("Y label")
# plt.legend()

# x = np.linspace(0, 2, 100)
# # fig,axs = plt.subplots(3)
# #
# # axs[0].plot(x, x ,  color ="red")
# # axs[0].set_title("linear")
# # axs[1].plot(x, x**2, color = "yellow" )
# # axs[1].set_title("quadratic")
# # axs[2].plot(x, x**3, color = "green")
# # axs[2].set_title("qubic")
# #
# # plt.tight_layout()

# x = np.linspace(0,2,100)
# fig,axs = plt.subplots(2,2)
# fig.suptitle("Graphic Title")
#
# axs[0,0].plot(x, x, color = "red")
# axs[0,1].plot(x, x**2, color = "yellow")
# axs[1,0].plot(x, x**3, color = "green")
# axs[1,1].plot(x, x**4, color = "blue")

import pandas as pd

df = pd.read_csv("C:/Users/Asus/PycharmProjects/learningpython/pandas/pandas/datasets/nba.csv")
df.drop(["Number"], axis=1).groupby("Team").mean()

df.plot(subplots=True)
plt.legend()
plt.show()
