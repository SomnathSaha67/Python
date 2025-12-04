traffic_light=input("Enter the traffic light color (red, yellow, green): ").lower()
if traffic_light=="red":
    print("Stop")
elif traffic_light=="yellow":
    print("Get ready")
elif traffic_light=="green":
    print("Go")
else:
    print("Light is broken")