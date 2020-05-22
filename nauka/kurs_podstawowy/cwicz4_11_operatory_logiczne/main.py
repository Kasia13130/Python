IsWeekend = True
print("Is weekend =", IsWeekend)
Temperature = 22
print("Temperature =", Temperature)
ToDoList = ""
print("ToDoList =", ToDoList)
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ""
print("IsHappy =", IsHappy)
print("\n")


IsWeekend = True
print("Is weekend =", IsWeekend)
Temperature = 5
print("Temperature =", Temperature)
ToDoList = ""
print("ToDoList =", ToDoList)
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ""
print("IsHappy =", IsHappy)
print("\n")


IsWeekend = True
print("Is weekend =", IsWeekend)
Temperature = 5
print("Temperature =", Temperature)
ToDoList = ""
print("ToDoList =", ToDoList)
IsHappy = not IsWeekend and Temperature < 20 and ToDoList != ""
print("IsHappy =", IsHappy)
print("\n")


IsWeekend = True
print("Is weekend =", IsWeekend)
Temperature = 5
print("Temperature =", Temperature)
ToDoList = "Shopping"
print("ToDoList =", ToDoList)
IsHappy = not IsWeekend and Temperature >= 20 and ToDoList == "" \
    or not IsWeekend and Temperature < 20 and ToDoList != ""
print("IsHappy =", IsHappy)
print("\n")


IsWeekend = True
print("Is weekend =", IsWeekend)
Temperature = 25
print("Temperature =", Temperature)
ToDoList = ""
print("ToDoList =", ToDoList)
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == "" \
    or not IsWeekend and Temperature < 20 and ToDoList != ""
print("IsHappy =", IsHappy)
print("\n")

# cwiczenie logiczne
print("1")
isAutomaticMode = True              # True - tryb automatyczny wlaczony
is80PercentLight = True            # True - jest dzien, swiatla zgaszone;
                                    # False - jest ciemno, swiatla oswiecone o ile jest tryb automatyczny
isDirectLight = False                # True - slonce jest nisko, swiatla swieca
isRainy = False                      # True - niekorzystne warunki, swiatla swieca

turnLightsOn = isAutomaticMode and is80PercentLight and isDirectLight and isRainy == ""

print("Automatic mode:      ", isAutomaticMode)
print("Is the light good        ", is80PercentLight)
print("Is sun low:      ", isDirectLight)
print("Is it rainy:     ", isRainy)
print("TURN LIGHTS ON:      ", turnLightsOn)
print("\n")

print("1")
isAutomaticMode = True              # True - tryb automatyczny wlaczony
is80PercentLight = True            # True - jest dzien, swiatla zgaszone;
                                    # False - jest ciemno, swiatla oswiecone o ile jest tryb automatyczny
isDirectLight = False                # True - slonce jest nisko, swiatla swieca
isRainy = False                      # True - niekorzystne warunki, swiatla swieca

turnLightsOn = isAutomaticMode and (not is80PercentLight and isDirectLight and isRainy) == ""

print("Automatic mode:      ", isAutomaticMode)
print("Is the light good        ", is80PercentLight)
print("Is sun low:      ", isDirectLight)
print("Is it rainy:     ", isRainy)
print("TURN LIGHTS ON:      ", turnLightsOn)
print("\n")

print("2")
isAutomaticMode = True              # True - tryb automatyczny wlaczony
is80PercentLight = False            # True - jest dzien, swiatla zgaszone;
                                    # False - jest ciemno, swiatla oswiecone o ile jest tryb automatyczny
isDirectLight = False                # True - slonce jest nisko, swiatla swieca
isRainy = False                      # True - niekorzystne warunki, swiatla swieca

turnLightsOn = isAutomaticMode or is80PercentLight and isDirectLight and isRainy == ""

print("Automatic mode:      ", isAutomaticMode)
print("Is the light good        ", is80PercentLight)
print("Is sun low:      ", isDirectLight)
print("Is it rainy:     ", isRainy)
print("TURN LIGHTS ON:      ", turnLightsOn)
print("\n")

print("3")
isAutomaticMode = True              # True - tryb automatyczny wlaczony
is80PercentLight = True            # True - jest dzien, swiatla zgaszone;
                                    # False - jest ciemno, swiatla oswiecone o ile jest tryb automatyczny
isDirectLight = False                # True - slonce jest nisko, swiatla swieca
isRainy = True                      # True - niekorzystne warunki, swiatla swieca

turnLightsOn = isAutomaticMode or is80PercentLight and isDirectLight and isRainy == ""

print("Automatic mode:      ", isAutomaticMode)
print("Is the light good        ", is80PercentLight)
print("Is sun low:      ", isDirectLight)
print("Is it rainy:     ", isRainy)
print("TURN LIGHTS ON:      ", turnLightsOn)
print("\n")

print("4")
isAutomaticMode = True              # True - tryb automatyczny wlaczony
is80PercentLight = True            # True - jest dzien, swiatla zgaszone;
                                    # False - jest ciemno, swiatla oswiecone o ile jest tryb automatyczny
isDirectLight = True                # True - slonce jest nisko, swiatla swieca
isRainy = False                      # True - niekorzystne warunki, swiatla swieca

turnLightsOn = isAutomaticMode or is80PercentLight and isDirectLight and isRainy == ""

print("Automatic mode:      ", isAutomaticMode)
print("Is the light good        ", is80PercentLight)
print("Is sun low:      ", isDirectLight)
print("Is it rainy:     ", isRainy)
print("TURN LIGHTS ON:      ", turnLightsOn)
print("\n")

print("5")
isAutomaticMode = True              # True - tryb automatyczny wlaczony
is80PercentLight = False            # True - jest dzien, swiatla zgaszone;
                                    # False - jest ciemno, swiatla oswiecone o ile jest tryb automatyczny
isDirectLight = False                # True - slonce jest nisko, swiatla swieca
isRainy = True                      # True - niekorzystne warunki, swiatla swieca

turnLightsOn = isAutomaticMode or is80PercentLight and isDirectLight and isRainy == ""

print("Automatic mode:      ", isAutomaticMode)
print("Is the light good        ", is80PercentLight)
print("Is sun low:      ", isDirectLight)
print("Is it rainy:     ", isRainy)
print("TURN LIGHTS ON:      ", turnLightsOn)
print("\n")

print("6")
isAutomaticMode = False              # True - tryb automatyczny wlaczony
is80PercentLight = True            # True - jest dzien, swiatla zgaszone;
                                    # False - jest ciemno, swiatla oswiecone o ile jest tryb automatyczny
isDirectLight = False                # True - slonce jest nisko, swiatla swieca
isRainy = True                      # True - niekorzystne warunki, swiatla swieca

turnLightsOn = isAutomaticMode or is80PercentLight and isDirectLight and isRainy == ""

print("Automatic mode:      ", isAutomaticMode)
print("Is the light good        ", is80PercentLight)
print("Is sun low:      ", isDirectLight)
print("Is it rainy:     ", isRainy)
print("TURN LIGHTS ON:      ", turnLightsOn)
print("\n")