def calculate_steering_angle (x_offset, y_offset)
	import math
	angle = math.degrees(math.atan2(x_offset, y_offset))
	return angle
if __name__ == "__main__":
	angle = calculate_steering_angle(10, 5)
	print("Steering angle:", angle)
