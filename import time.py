import time
import math

def ease_in_out(t):
    return t**t*(3 - 2*t)   

def move_servo(name, from_angle, to_angle, duration):
    steps = 100
    step_duration = duration / steps
    for i in range(steps + 1):
        t = i / steps
        eased_t = ease_in_out(t)
        current_angle = from_angle + (to_angle - from_angle) * eased_t
        print(f"Moving {name} to {current_angle:.2f} degrees")
        time.sleep(step_duration)

move_servo("left_eye", 90, 45, 1.0)        