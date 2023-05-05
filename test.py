import math

def calculate_turn_radius(wheel_base, steering_angle):
    steering_angle_rad = math.radians(steering_angle)
    turn_radius = wheel_base / math.sin(steering_angle_rad)
    return round(turn_radius, 2)

def calculate_position_direction(wheel_base, distance, steering_angle):
    if steering_angle == 0.00:
        x = 0
        y = distance
        new_direction = 0
    else:
        turn_radius = calculate_turn_radius(wheel_base, steering_angle)
        turn_angle = distance / turn_radius
        x = turn_radius * (1 - math.cos(turn_angle))
        y = turn_radius * math.sin(turn_angle)
        new_direction = math.degrees(turn_angle) % 360
    return round(x, 2), round(y, 2), round(new_direction, 2)

def calculate_position_direction_segments(wheel_base, segments, distances, steering_angles):
    x, y, new_direction = 0, 0, 0
    for distance, steering_angle in zip(distances, steering_angles):
        dx, dy, dtheta = calculate_position_direction(wheel_base, distance, steering_angle)
        theta_rad = math.radians(new_direction)
        x += dx * math.cos(theta_rad) + dy * math.sin(theta_rad)
        y += - dx * math.sin(theta_rad) + dy * math.cos(theta_rad)
        new_direction += dtheta
    return round(x, 2), round(y, 2), round(new_direction % 360, 2)

# input values
wheel_base = float(input("Enter the wheel base (in meters): "))
segments = int(input("Enter the number of segments: "))
distances = [float(input(f"Enter the distance to drive for segment {i+1} (in meters): ")) for i in range(segments)]
steering_angles = [float(input(f"Enter the steering angle for segment {i+1} (in degrees): ")) for i in range(segments)]

x, y, new_direction = calculate_position_direction_segments(wheel_base, segments, distances, steering_angles)

print(x, y, new_direction)