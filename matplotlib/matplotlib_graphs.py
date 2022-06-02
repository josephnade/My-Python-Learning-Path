import matplotlib.pyplot as plt

'''
# Stack Plot
years = [2011, 2012, 2013, 2014, 2015]
player1 = [10, 12, 13, 20, 8]
player2 = [21, 23, 24, 25, 27]
player3 = [4, 5, 3, 6, 12]


plt.plot([], [], color="r", label="player1")
plt.plot([], [], color="b", label="player2")
plt.plot([], [], color="y", label="player3")

plt.stackplot(years,player1,player2,player3,colors=["r","b","y"])
plt.title("Goals according to Years")
plt.xlabel("Years")
plt.ylabel("Goals")
plt.legend()

'''
# Pie Plot
'''
goal_types = ["Penalty", "Shot on Goal", "Freekick"]
goals = [12, 35, 7]
colors = ["r", "y", "b"]
plt.pie(goals, labels=goal_types, colors=colors, shadow=True, explode=(0.05, 0.05, 0.05),autopct="%1.1f%%")
plt.title("Goals according to Goal Types")
'''
'''
# Bar Plot
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label = "BMW",width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label = "Audi",width=0.5)
plt.xlabel("Day")
plt.ylabel("Distance (km)")
plt.title("Car Information")
plt.legend()
'''

# Histogram Plot
'''
ages = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115]
groups_ages = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages,groups_ages,histtype="bar",rwidth=0.8)
plt.xlabel("Groups of Ages")
plt.ylabel("Number of People")
plt.title("Histogram Graphic")

plt.show()
'''