import matplotlib.pyplot as plt
  
male_salaries = [3000, 3500, 3000, 3500, 4000] 
female_salaries = [2500, 3000, 2500, 3000, 3500] 
  
plt.bar(range(len(male_salaries)), male_salaries, width=0.35, 
            label='Male Salaries') 
  
plt.bar([x+0.35 for x in range(len(female_salaries))], 
            female_salaries, width=0.35, 
            label='Female Salaries') 
  
plt.xlabel('Employee') 
plt.ylabel('Salaries') 
plt.title('Salaries per Gender') 
plt.legend(loc="upper right") 
plt.show()