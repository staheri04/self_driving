def calculate_steering_angle (x_offset, y_offset)
	import math
	angle = math.degrees(math.atan2(x_offset, y_offset))
	return angle
