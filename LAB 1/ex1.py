# Parameters
time_steps = 50
x = 0.0  # Initial state x(0)

# Open CSV file for writing
try:
    with open("state_data.csv", "w") as data_file:
        # Write header
        data_file.write("t,x_t\n")

        # Simulation loop
        for t in range(time_steps + 1):
            # Write current state
            data_file.write(f"{t},{x}\n")

            # State transition: x(t+1) = x(t) + 1
            x = x + 1.0

    print("Success! Data for 50 steps saved to state_data.csv")

except IOError:
    print("Error opening file!")