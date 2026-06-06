devices = [
    "Sensor_1",
    "Gateway",
    "Router",
    "Server",
    "Monitor"]

print("Available Network Devices:")

for device in devices:
    print(device)

def send_data(source, destination):
    print(f"Data transferred from {source} to {destination}")

send_data("Sensor_1", "Server")
