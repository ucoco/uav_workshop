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


print("Move Forward")
tello.move_right(60)



print("Move Forward")
tello.move_back(60)



print("Move Forward")
tello.move_left(60)



#print("Sleep for 5 seconds")
#time.sleep(5)


print("landing")
tello.land()
print("touchdown.... goodbye")
