new_list = []
l = [1,2,3,4,5,6,7,8,]
print("true") if True else print("false""")
#new_list = [i for i in l if i%2==0] # list comrehension
new_list = (i for i in l if i%2==0)#generator comrehenion
print(new_list)