import math

# input values
wheel_base = float(input("Enter the wheel base (in meters): "))
num_segments = int(input("Enter the number of segments: "))

distances = []
steering_angles = []
"""
for i in range(num_segments):
    distances.append(float(input(f"Enter the distance for segment {i+1} (in meters): ")))
    steering_angles.append(float(input(f"Enter the steering angle for segment {i+1} (in degrees): ")))
"""
x = 0
y = 0
new_direction = 0

for i in range(num_segments):
    distance = float(input(f"Enter the distance for segment {i+1} (in meters): "))
    steering_angle = float(input(f"Enter the steering angle for segment {i+1} (in degrees): "))

    if steering_angle == 0.00:
        x += distance * math.sin(math.radians(new_direction))
        y += distance * math.cos(math.radians(new_direction))
        new_direction = new_direction
        print (round(x, 2),round(y, 2),round(new_direction % 360, 2))

    elif steering_angle == 90.00:
        x += distance * math.cos(math.radians(new_direction))
        y += distance * math.sin(math.radians(new_direction))
        new_direction = new_direction
        print (round(x, 2),round(y, 2),round(new_direction % 360, 2))

    else:
        steering_angle_rad = math.radians(steering_angle)
        turn_radius = wheel_base / math.sin(steering_angle_rad)
        turn_angle = distance / turn_radius

        xx = turn_radius * (1 - math.cos(turn_angle)) 
        yy = turn_radius * math.sin(turn_angle)
        direction = math.degrees(turn_angle) % 360
        

        theta_rad = math.radians(new_direction)
        x += xx * math.cos(theta_rad) + yy * math.sin(theta_rad)
        y += - xx * math.sin(theta_rad) + yy * math.cos(theta_rad)
        new_direction += direction
        print (round(x, 2),round(y, 2),round(new_direction % 360, 2))

x = round(x, 2)
y = round(y, 2)
direction = round(new_direction % 360, 2)

print(x, y, direction)

