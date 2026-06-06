import simpy

def sensor(env):
    while True:
        print(f"Time {env.now}: Sensor generated data")
        yield env.timeout(3)

def monitor(env):
    while True:
        print(f"Time {env.now}: Network status checked")
        yield env.timeout(6)

env = simpy.Environment()

env.process(sensor(env))
env.process(monitor(env))

env.run(until=24)
