import boto3
from braket.aws import AwsDevice
from braket.circuits import Circuit
from braket.devices import LocalSimulator

device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")

# Create a circuit with one qubit
circuit = Circuit().h(0).measure(0)

# Simulate the circuit using the local simulator
device = LocalSimulator()
result = device.run(circuit).result()

# Print the result of the simulation
counts = result.measurement_counts
print(counts)