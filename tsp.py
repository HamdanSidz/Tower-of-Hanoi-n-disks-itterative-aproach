from itertools import permutations

def tsp(cities,distances):

    diff_paths = permutations(cities)

    diff_paths_1 = []
    for i in diff_paths:
        diff_paths_1.append(list(i))

       # print(i)

    sav = " "
    for i in range(len(diff_paths_1)):
        for j in range(len(cities)):
            if j == 0:
                sav = diff_paths_1[i][j]
            elif j == len(cities)-1:
                diff_paths_1[i].append(sav)
        sav = " "

    #print(diff_paths_1)

    dic = {}
    for i in range(len(cities)):
        dic[cities[i]] = i
 
    #print(dic)

    for i in range(len(diff_paths_1)):
        for j in range(len(cities)+1):
            city = diff_paths_1[i][j]
            diff_paths_1[i][j] = dic[city]

    #print(diff_paths_1)
    
    fact = 1
    for i in range(1,len(cities)+1):
        fact*=i

    #print(fact)
    real_val = fact//len(cities)
    #print(real_val)

    city = input("Enter your starting point/city name: ")
    city = dic[city]
    
    #print(city)

    index = 0
    found = False
    for i in range(len(diff_paths_1)):
        if found == True:
            break
        for j in range(len(cities)):
            if diff_paths_1[i][j] == city:
                index = i
                found = True
                break
            else:
                break    

    #print(index)


    short_path_dic = {}
    cal_cost = []

    route = 0
    for i in range(1,real_val+1):
        for j in range(len(cities)):
            route += distances[diff_paths_1[index][j]][diff_paths_1[index][j+1]]
            
        cal_cost.append(route)
        short_path_dic[route] = diff_paths_1[index]
        route = 0

        #print(index)
        index+=1 
        
        
    #print(short_path_dic)
    #print(cal_cost)

    for i in range(len(cal_cost)):
        for j in range(len(cal_cost)):
            if cal_cost[i] < cal_cost[j]:
                temp = cal_cost[i]
                cal_cost[i] = cal_cost[j]
                cal_cost[j] = temp

    #print(cal_cost)

    arr = short_path_dic[cal_cost[0]]
    #print(arr)

    for i in range(len(arr)):
        arr[i] = arr[i]+1 

    print(F"Shortest path from city {city+1} to all others is: {short_path_dic[cal_cost[0]]} and path measured is {cal_cost[0]}.")


def city_info():

    cities = []
    no_city = int(input("enter total cities you have in your route: "))
    for i in range(no_city):
        city = input("enter all cities name you have, one by one: ")
        cities.append(city)

    distances = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    

    #for input from user of cities to cities distance 
    
    """ distances = []
    distance = []

    for i in range(len(cities)):
        for j in range(len(cities)):
            dis = int(input(f"Enter city {cities[i]} distance to city {cities[j]}: "))
            distance.append(dis)

        distances.append(distance)
        distance = []

     
    for i in range(len(cities)):
        for j in range(len(cities)):
            print(distances[i][j], end=" ")

        print() 
          """

    tsp(cities,distances)


city_info()
