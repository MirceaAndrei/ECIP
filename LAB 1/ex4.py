import numpy as np


time_steps = 50
window_size = 10  
x_true = 0.0      


np.random.seed(0)  


observations = []

try:
    with open("analysis_results.csv", "w") as data_file:
        
        data_file.write("t,True_State,Observation,MA_Estimate\n")

       
        for t in range(time_steps + 1):
           
            z_t = x_true + np.random.normal(0.0, 2.0)
            observations.append(z_t)

            
            current_size = len(observations)
            start_idx = max(0, current_size - window_size)

            window = observations[start_idx:current_size]
            x_est = sum(window) / len(window)

            
            data_file.write(f"{t},{x_true},{z_t},{x_est}\n")

          
            x_true += 1.0

    print("Simulation Finished. File 'analysis_results.csv' generated.")

except IOError:
    print("Error: Could not create data file.")