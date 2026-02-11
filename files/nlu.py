import math

# Activation Functions
def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# -------- Input Layer --------
inputs = [1.0, 0.5]   # Example input values
print("Input Layer:", inputs)

# -------- Hidden Layer --------
# Weights and Biases (Hardcoded)
w1 = [[0.2, 0.4],
      [0.7, 0.1]]
b1 = [0.5, -0.3]

hidden_outputs = []

for i in range(2):
    net = (inputs[0] * w1[i][0]) + (inputs[1] * w1[i][1]) + b1[i]
    activated = relu(net)
    hidden_outputs.append(activated)
    print(f"Hidden Neuron {i+1} Net = {net:.4f}, Activated (ReLU) = {activated:.4f}")

print("Hidden Layer Outputs:", hidden_outputs)

# -------- Output Layer --------
# Weights and Biases (Hardcoded)
w2 = [0.6, 0.9]
b2 = 0.2

net_output = (hidden_outputs[0] * w2[0]) + (hidden_outputs[1] * w2[1]) + b2
final_output = sigmoid(net_output)

print(f"\nOutput Neuron Net = {net_output:.4f}")
print(f"Final Output (Sigmoid) = {final_output:.4f}")