import math


wheel_base = float(input("Enter the wheel base (in meters): "))
steering_angle = float(input("Enter the steering angle (in degrees): "))


steering_angle_rad = math.radians(steering_angle)


turn_radius = wheel_base / math.sin(steering_angle_rad)


turn_radius = round(turn_radius, 3)


print(turn_radius)