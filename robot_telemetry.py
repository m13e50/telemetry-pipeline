def validate(data):
    robot_id=data.get("robot_id", "unknown")
    battery=data.get("battery_pct")
    if not isinstance(battery, int) or isinstance(battery,bool):
        print(f"[ERROR] {robot_id}: battery_pct must be an int, got {battery!r}")
    elif battery<0 or battery>100:
        print(f"[ERROR] {robot_id}: battery_pct {battery} out of range (0-100)")
    else:
       print(f"robot {robot_id} is at battery {battery}%") 
