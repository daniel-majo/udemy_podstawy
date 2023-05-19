#1. sterownik automatycznego włączania światel w samochodzie

isAutomaticMode = True  # światła włączone przez kierowcę na Auto
is80PercentLight = True # światła zgaszone, prawdopodobnie mamy dzień
isDirectLight = True   # światła świecą ale nie jest jeszcze ciemno
isRainy = True          # niekorzystne warunki: mgła, deszcz

turnLightsOn = (isAutomaticMode and (not is80PercentLight or isDirectLight\
                or isRainy))

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

# 2. światła powinny się NIE świecić
##isAutomaticMode = True  # światła włączone przez kierowcę na Auto
##is80PercentLight = True # światła zgaszone, prawdopodobnie mamy dzień
##isDirectLight = False   # światła świecą ale nie jest jeszcze ciemno
##isRainy = False          # niekorzystne warunki: mgła, deszcz
##
##turnLightsOn = (isAutomaticMode and (not is80PercentLight or isDirectLight\
##                or isRainy))
##
##print("Automatic mode:   ",isAutomaticMode)
##print("Is the light good:",is80PercentLight)
##print("Is sun low:       ",isDirectLight)
##print("Is it rainy:      ",isRainy)
##print("TURN LIGHTS ON:   ",turnLightsOn)

# 3. światła powinny się świecić
##isAutomaticMode = True  # światła włączone przez kierowcę na Auto
##is80PercentLight = False # światła zgaszone, prawdopodobnie mamy dzień
##isDirectLight = False   # światła świecą ale nie jest jeszcze ciemno
##isRainy = False          # niekorzystne warunki: mgła, deszcz
##
##turnLightsOn = (isAutomaticMode and (not is80PercentLight or isDirectLight\
##                or isRainy))
##
##print("Automatic mode:   ",isAutomaticMode)
##print("Is the light good:",is80PercentLight)
##print("Is sun low:       ",isDirectLight)
##print("Is it rainy:      ",isRainy)
##print("TURN LIGHTS ON:   ",turnLightsOn)

# 4. światła powinny się świecić
##isAutomaticMode = True  # światła włączone przez kierowcę na Auto
##is80PercentLight = True # światła zgaszone, prawdopodobnie mamy dzień
##isDirectLight = False   # światła świecą ale nie jest jeszcze ciemno
##isRainy = True          # niekorzystne warunki: mgła, deszcz
##
##turnLightsOn = (isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy))
##                
##print("Automatic mode:   ",isAutomaticMode)
##print("Is the light good:",is80PercentLight)
##print("Is sun low:       ",isDirectLight)
##print("Is it rainy:      ",isRainy)
##print("TURN LIGHTS ON:   ",turnLightsOn)

# 5. światła powinny się świecić
##isAutomaticMode = True  # światła włączone przez kierowcę na Auto
##is80PercentLight = True # światła zgaszone, prawdopodobnie mamy dzień
##isDirectLight = True   # światła świecą ale nie jest jeszcze ciemno
##isRainy = False          # niekorzystne warunki: mgła, deszcz
##
##turnLightsOn = (isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy))
##                
##print("Automatic mode:   ",isAutomaticMode)
##print("Is the light good:",is80PercentLight)
##print("Is sun low:       ",isDirectLight)
##print("Is it rainy:      ",isRainy)
##print("TURN LIGHTS ON:   ",turnLightsOn)

# 6. światła powinny się świecić
##isAutomaticMode = True  # światła włączone przez kierowcę na Auto
##is80PercentLight = False # światła zgaszone, prawdopodobnie mamy dzień
##isDirectLight = False  # światła świecą ale nie jest jeszcze ciemno
##isRainy = True          # niekorzystne warunki: mgła, deszcz
##
##turnLightsOn = (isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy))
##                
##print("Automatic mode:   ",isAutomaticMode)
##print("Is the light good:",is80PercentLight)
##print("Is sun low:       ",isDirectLight)
##print("Is it rainy:      ",isRainy)
##print("TURN LIGHTS ON:   ",turnLightsOn)

# 7. światła nie powinny się świecić
##isAutomaticMode = False  # światła włączone przez kierowcę na Auto
##is80PercentLight = True # światła zgaszone, prawdopodobnie mamy dzień
##isDirectLight = False  # światła świecą ale nie jest jeszcze ciemno
##isRainy = True          # niekorzystne warunki: mgła, deszcz
##
##turnLightsOn = (isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy))
##                
##print("Automatic mode:   ",isAutomaticMode)
##print("Is the light good:",is80PercentLight)
##print("Is sun low:       ",isDirectLight)
##print("Is it rainy:      ",isRainy)
##print("TURN LIGHTS ON:   ",turnLightsOn)
