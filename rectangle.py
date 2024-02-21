from djitellopy import Tello
import time

print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

print("Takeoff!")
tello.takeoff()

#print("Sleep for 5 seconds")
#time.sleep(3)

print("Move Forward")
tello.move_forward(60)

print("Rotate Clockwise")
tello.rotate_clockwise(90)

print("Move Forward")
tello.move_forward(60)

print("Rotate Clockwise")
tello.rotate_clockwise(90)

print("Move Forward")
tello.move_forward(80)

print("Rotate Clockwise")
tello.rotate_clockwise(90)

print("Move Forward")
tello.move_forward(80)

print("Rotate Clockwise")
tello.rotate_clockwise(90)


#print("Sleep for 5 seconds")
#time.sleep(5)


print("landing")
tello.land()
print("touchdown.... goodbye")
