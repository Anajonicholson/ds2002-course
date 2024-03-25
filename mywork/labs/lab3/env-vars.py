#!/c/Users/16073/AppData/Local/Microsoft/WindowsApps/python3



import os

os.environ["EYE_COLOR"] = "Blue"
os.environ["FAV_COLOR"] = "Purple"
os.environ["FAV_FOOTBALL"] = "Steelers"

os.environ["EYE_COLOR"] = input('What is your eye color?')
os.environ["FAV_COLOR"] = input('What is your favorite color?')
os.environ["FAV_FOOTBALL"] = input('What is your favorite football team?')

print(os.getenv("EYE_COLOR"))
print(os.getenv("FAV_COLOR"))
print(os.getenv("FAV_FOOTBALL"))
