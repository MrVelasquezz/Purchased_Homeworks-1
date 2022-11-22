import math
import numpy as np
import matplotlib.pyplot as plt

def sorter(i):
    return i[1]

with open('dane.txt', 'r+') as file:
    lines = file.readlines()
    
    city_dict = {}
    
    general_avg_in_city = {
        "cities": [],
        "people": []
    }
    
    acc_val_in_city = {
        "city": [],
        "people_m": [],
        "people_k": [],
        "people_m_a": [],
        "people_k_a": [],
    }
    
    avg_age = {
        "city": [],
        "avg_age_m": [],
        "avg_age_k": [],
        "older_than_50_m": [],
        "older_than_50_k": [],
        "younger_than_50_m": [],
        "younger_than_50_k": []
    }
    
    
    
    for x in lines:                     #main data parser
        parsed_data = x.replace('\n', '').split(';')
        city_key_list = list(city_dict.keys())
        if(city_key_list.count(parsed_data[4]) == 0):
            city_dict[parsed_data[4]] = []
        city_dict[parsed_data[4]].append(parsed_data)   
      
    for x in city_dict:                 #counts bewohner in der stadter
        general_avg_in_city["cities"].append(x)
        general_avg_in_city["people"].append(len(city_dict[x]))
    
    for x in city_dict:                 #counts more accurate m and k
        acc_val_in_city["city"].append(x)
        m = []
        k = []
        for y in city_dict[x]:
            
            lz_yob = f'{y[0][0]}{y[0][1]}'
            lz_mon = f'{y[0][2]}{y[0][3]}'
            yob = 0
            
            lz_yob = int(lz_yob)
            lz_mon = int(lz_mon)
            
            #print(y[0], numb)
            if int(lz_yob) < 2:
                yob = 2022 - (2000 + lz_yob)
            else:
                yob = 2022 - (1900 + lz_yob)
            
            y[0] = yob
            
            if y[3] == 'm':
                m.append(y)
            else: 
                k.append(y)
                
        acc_val_in_city["people_m"].append(m)
        acc_val_in_city["people_k"].append(k)
        acc_val_in_city["people_m_a"].append(len(m))
        acc_val_in_city["people_k_a"].append(len(k))
        
    for x in range(len(acc_val_in_city["city"])):
        avg_age_m = 0
        avg_age_k = 0
        name_m = []
        name_k = []
        older_50_m = []
        younger_50_m = []
        older_50_k = []
        younger_50_k = []
        for y in acc_val_in_city["people_m"][x]:
            avg_age_m += int(y[0])
            if int(y[0]) < 50:
                 younger_50_m.append(y)
            else:
                older_50_m.append(y)
        for y in acc_val_in_city["people_k"][x]:
            avg_age_k += int(y[0])
            if int(y[0]) < 50:
                 younger_50_k.append(y)
            else:
                older_50_k.append(y)
                
        avg_age["city"].append(acc_val_in_city["city"][x])
        avg_age["avg_age_m"].append(math.floor(int(avg_age_m)/len(acc_val_in_city["people_m"][x])))
        avg_age["avg_age_k"].append(math.floor(int(avg_age_m)/len(acc_val_in_city["people_k"][x])))
        avg_age["older_than_50_m"].append(len(older_50_m))
        avg_age["younger_than_50_m"].append(len(younger_50_m))
        avg_age["older_than_50_k"].append(len(older_50_k))
        avg_age["younger_than_50_k"].append(len(younger_50_k))
        
     
fig = plt.subplots(figsize=(15, 6))      
plt.barh(np.array(general_avg_in_city["cities"]), np.array(general_avg_in_city["people"]))
plt.xlabel("Count of people from town", fontweight='bold', fontsize="12")
plt.ylabel("Cities", fontweight='bold', fontsize="12")
plt.grid()
plt.show()

fig = plt.subplots(figsize=(16, 8))
barWidth = 0.4

br_m = np.arange(len(acc_val_in_city["people_m_a"]))
br_k = [x + barWidth for x in br_m]

plt.barh(br_m, acc_val_in_city["people_m_a"], color="blue", edgecolor=["none"], height=barWidth, label="Men")
plt.barh(br_k, acc_val_in_city["people_k_a"], color="red", edgecolor=["none"], height=barWidth, label="Women")
 
plt.xlabel("Cities", fontweight='bold', fontsize="12")
plt.ylabel('Peole in this city', fontweight='bold', fontsize="12")
plt.yticks([r + barWidth for r in range(len(acc_val_in_city["people_m_a"]))], acc_val_in_city["city"])
plt.legend()
plt.grid()
plt.show()       

barWidth = 0.2
plt.subplots(figsize=(22, 6))
plt.subplot(1, 2, 1)

br_m_a = np.arange(len(avg_age["avg_age_m"]))
br_m_o = [x + barWidth for x in br_m]
br_m_y = [x + barWidth for x in br_m_o]

plt.barh(br_m, avg_age["avg_age_m"], color="blue", edgecolor=["none"], height=barWidth, label="Avg age")
plt.barh(br_m_o, avg_age["older_than_50_m"], color="red", edgecolor=["none"], height=barWidth, label="Older then 50")
plt.barh(br_m_y, avg_age["younger_than_50_m"], color="green", edgecolor=["none"], height=barWidth, label="Younger than 50")
plt.title("Men age")
plt.xlabel("Cities", fontweight='bold', fontsize="12")
plt.ylabel('Peole in this city', fontweight='bold', fontsize="12")
plt.yticks([r + barWidth for r in range(len(avg_age["avg_age_m"]))], avg_age["city"])
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)

br_k_a = np.arange(len(avg_age["avg_age_k"]))
br_k_o = [x + barWidth for x in br_k]
br_k_y = [x + barWidth for x in br_k_o]

plt.barh(br_k, avg_age["avg_age_k"], color="pink", edgecolor=["none"], height=barWidth, label="Avg age")
plt.barh(br_k_o, avg_age["older_than_50_k"], color="blue", edgecolor=["none"], height=barWidth, label="Older then 50")
plt.barh(br_k_y, avg_age["younger_than_50_k"], color="green", edgecolor=["none"], height=barWidth, label="Younger than 50")
plt.title("Women age")
plt.xlabel("Cities", fontweight='bold', fontsize="12")
plt.ylabel('Peole in this city', fontweight='bold', fontsize="12")
plt.yticks([r + barWidth for r in range(len(avg_age["avg_age_k"]))], avg_age["city"])
plt.legend()
plt.grid()
plt.show()       