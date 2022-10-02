#August/14/2022
#------------------------------------------TEMPERATURE CONVERTER
x = 0
print("Temperature Converter")
temp1 = int(input("Enter Temperature"))
print("You Entered" +" "+str(temp1))

print("""
Select Temperature to Convert to

1. Celcius to Kelvin        

2. Celcius to fahrenheit

3. Kelvin to celcius

4. Kelvin to fahrenheit

5. farenheit to kelvin

6. farenheit to celcius

""")
while x<= 6:
    selct = (input("Select operation number"))
    if selct == ("1"):
            ans = temp1 + 273.15
            print(str(ans) + "°K")
    elif selct == ("2"):
            ans = (temp1 * 9/5) + 32
            print (str(ans)+"°F")
    elif selct == ("3"):
            ans = temp1 - 273.15
            print (str(ans)+"°C")
    elif selct == ("4"):
            ans = (temp1 - 273.15) * 9/5 + 32
            print (str(ans)+"°F")
    elif selct  == ("5"):
            ans = (temp1 -32) * 5/9 + 273.15
            print (str(ans)+"°K")
    elif selct == ("6"):
           ans = (temp1 -32) * 5/9
           print (str(ans)+"°C")   
    elif selct > ("6"):
        print("Invalid Input")
    if selct == "Quit" :
               break
x += 1            
#------------------------------------------------------------|            

# #fahrenheit to kelvin
# #Formula
# (32°F − 32) × 5/9 + 273.15 = 273.15K 
# #kelvin to celcius
# #Formula
# 32K − 273.15 = -241.1°C
# #to fahrenheit
# #Formula
# (32°C × 9/5) + 32 = 89.6°F
# #celcius to kelvin
# #Formula
# 32°C + 273.15 = 305.15K
# #kelvin to fahrenheit
# #Formula	
# (32K − 273.15) × 9/5 + 32 = -402.1°F
# #fahrenheit to celcius
# #Formula	
# (45°F − 32) × 5/9 = 7.222°C



