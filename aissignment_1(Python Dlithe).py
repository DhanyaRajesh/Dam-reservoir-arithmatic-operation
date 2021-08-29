d_cap = 250e100 #dam reservoir's capacity

wat = 199.5e85 #current water amount

r_wat = 25e8 #water from rain

u_less = 25e8 * 25 / 100 #625000000.0

rem_w = 25e8 - u_less #1875000000.0 remaining water

cur_wat = wat + rem_w #1.995e+87 current water amount

cur_wat1 = cur_wat + (cur_wat * 0.15) #2.29425e+87 water increased by storm

cur_wat2 = cur_wat1 + (cur_wat1 * 0.5)#5% ground water = 3.441375e+87

cur_wat3 = cur_wat2 - (cur_wat2 * 0.5)#5% water evaporated = 1.7206875e+87

cur_w = cur_wat3 - (cur_wat3*0.15)#15% for irrigation

print("The current water level is ",cur_w)





