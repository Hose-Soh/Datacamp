# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title("Hours_Worked")

# Add y-axis label
plt.ylabel("Days")

# Legend
plt.legend()
# Display plot
plt.show()