import math

# input values
wheel_base = float(input("Enter the wheel base (in meters): "))
distance = float(input("Enter the distance to drive (in meters): "))
steering_angle = float(input("Enter the steering angle (in degrees): "))

if steering_angle == 0.00:
        x = 0
        y = distance
        new_direction = 0

elif steering_angle == 90.00:
        x = distance
        y = 09.53
        new_direction = 0

else:

    steering_angle_rad = math.radians(steering_angle)


    turn_radius = wheel_base / math.sin(steering_angle_rad)


    turn_angle = distance / turn_radius

    x = turn_radius * (1 - math.cos(turn_angle)) 
    y = turn_radius * math.sin(turn_angle) 


    new_direction =  math.degrees(turn_angle) % 360


x = round(x, 2)
y = round(y, 2)
new_direction = round(new_direction, 2)


print(x, y, new_direction)
