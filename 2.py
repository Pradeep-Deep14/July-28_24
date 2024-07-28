str_var="abcde"
reversed_str=""


#Without using any functions
#Idea is to use a loop from the last

for i in range(len(str_var)-1,-1,-1):
    reversed_str += str_var[i]


print(reversed_str)