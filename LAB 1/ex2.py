import numpy as np

# Parameters
time_steps = 50
x_true = 0.0  # Initial true state
mean = 0.0
std_dev = 2.0

# Set random seed (optional, pentru reproducibilitate)
np.random.seed(0)

try:
    with open("noisy_state.csv", "w") as data_file:
        # Header
        data_file.write("t,True_State,Noisy_Measurement\n")

        for t in range(time_steps + 1):
            # Generate Gaussian noise
            v_t = np.random.normal(mean, std_dev)
            z_t = x_true + v_t

            # Write to file
            data_file.write(f"{t},{x_true},{z_t}\n")

            # State evolution: x(t+1) = x(t) + 1
            x_true = x_true + 1.0

    print("Simulation complete. Data saved to noisy_state.csv")

except IOError:
    print("Error opening file!")