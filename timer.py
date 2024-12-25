# All Libraries Installed :- 
import time
import winsound

# Taking Input :- 
countdown_time = int(input("Enter the countdown time in seconds: "))

# Displaying The Virtual Interface :- 
while countdown_time > 0:
    print("Time remaining:", countdown_time, "seconds")
    time.sleep(1)  # Wait for 1 second
    countdown_time -= 1

# For The Beep Sound :- 
winsound.Beep(700,2000)
print("Time's up!")
print("Thank You for giving us the opportunity to serve you .")
print("Hope you Have a Nice Day . Thank You!")
