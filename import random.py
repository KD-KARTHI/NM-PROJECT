import random
import time

def get_sensor_data():
    """Simulates lane and obstacle data from vehicle sensors."""
    data = {
        "lane_position": random.choice(["center", "left", "right"]),
        "obstacle_distance": random.randint(5, 100)  # in meters
    }
    return data

def ai_vehicle_decision(data):
    """Simple rule-based AI decisions for driving."""
    actions = []

    if data["lane_position"] == "left":
        actions.append("Adjusting right to stay in lane.")
    elif data["lane_position"] == "right":
        actions.append("Adjusting left to stay in lane.")
    else:
        actions.append("Maintaining lane position.")

    if data["obstacle_distance"] < 20:
        actions.append("Obstacle detected! Slowing down and preparing to stop.")
    else:
        actions.append("Path is clear. Maintaining speed.")

    return actions

def main():
    print("=== AI Autonomous Vehicle Simulator ===\n")
    for i in range(5):
        print(f"\n[Sensor Reading {i+1}] Gathering vehicle data...")
        time.sleep(1)
        data = get_sensor_data()
        print(f"Lane Position: {data['lane_position']}")
        print(f"Obstacle Distance: {data['obstacle_distance']} m")

        decisions = ai_vehicle_decision(data)
        print("\nAI Decisions:")
        for decision in decisions:
            print(f"- {decision}")
        time.sleep(2)

if __name__ == "__main__":
    main()
