# printer(elements)
# - Accepts a list
# - Prints every element of the list
def printer(elements):
    for element in elements:
        print(element)


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
def to_celsius(temperatures):

    
    cTemp=[]

    for temp in temperatures:
        
        cTemp.append((temp-32)*(5/9))
        
        #print(cTemp.append((temp-32)*(5/9)))
        print(cTemp)


        #print(temp)
    return cTemp



# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
def hottest_days(temperatures, threshold):
    myTemp=[]
    for temp in temperatures:
        if temp >= threshold:
            myTemp.append(temp)
    print(temp)
    print(myTemp)
    return myTemp
            


# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
def print_hottest_days(temperatures, threshhold):
    
     printer(to_celsius(hottest_days(temperatures, threshhold)))
x = [10,1,2,5,20,56,70,-1]
print(type(x[3]))
print((x[3]))
print_hottest_days(x,25)
    
    