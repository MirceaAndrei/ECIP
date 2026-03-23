import numpy as np

# Parameters
time_steps = 50
window_size = 5
x_true = 0.0

# Random setup (AWGN: mean 0, std dev 2)
np.random.seed(0)  # optional

observations = []

try:
    with open("filter_results.csv", "w") as data_file:
        # CSV Header
        data_file.write("t,True_State,Noisy_Observation,Estimated_State\n")

        for t in range(time_steps + 1):
            # 1. Generate True State and Noisy Observation
            z_t = x_true + np.random.normal(0.0, 2.0)
            observations.append(z_t)

            # 2. Moving Average Estimate
            if len(observations) < window_size:
                x_est = np.mean(observations)
            else:
                x_est = np.mean(observations[-window_size:])

            # 3. Log data
            data_file.write(f"{t},{x_true},{z_t},{x_est}\n")

            # 4. Update true state
            x_true += 1.0

    print("Success! Results saved to filter_results.csv")

except IOError:
    print("Error opening file!")