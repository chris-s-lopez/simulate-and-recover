import numpy as np
from scipy.stats import binom, norm, gamma
import argparse

def simulate_and_recover(N, iterations=1000):
    results = []
    
    for _ in range(iterations):
        # random parameters
        alpha_true = np.random.uniform(0.5, 2.0)  # boundary separation
        nu_true = np.random.uniform(0.5, 2.0)     # drift rate
        tau_true = np.random.uniform(0.1, 0.5)    # nondecision time
        
        # forward equations
        y = np.exp(-alpha_true * nu_true)
        R_pred = 1 / (y + 1)
        M_pred = tau_true + (alpha_true / (2 * nu_true)) * ((1 - y) / (1 + y))
        V_pred = (alpha_true / (2 * nu_true**3)) * ((1 - 2 * alpha_true * nu_true * y - y**2) / (y + 1)**2)
        
        # observed 
        R_obs = binom.rvs(N, R_pred) / N  # Simulated accuracy
        M_obs = norm.rvs(M_pred, np.sqrt(V_pred / N))  # Simulated mean RT
        V_obs = gamma.rvs((N - 1) / 2, scale=(2 * V_pred) / (N - 1))  # Simulated variance RT
        
        # compute inverse equations
        if R_obs > 0 and R_obs < 1:  # Ensure log calculation is valid
            L = np.log(R_obs / (1 - R_obs))
            nu_est = np.sign(R_obs - 0.5) * 4 * np.sqrt(L * (R_obs**2 * L - R_obs * L + R_obs - 0.5) / V_obs)
            alpha_est = L / nu_est if nu_est != 0 else np.nan
            tau_est = M_obs - (alpha_est / (2 * nu_est)) * ((1 - np.exp(-nu_est * alpha_est)) / (1 + np.exp(-nu_est * alpha_est)))
            
            # compute bias and squared error
            bias = (alpha_true - alpha_est, nu_true - nu_est, tau_true - tau_est)
            squared_error = tuple(b**2 for b in bias)
            
            results.append((N, bias, squared_error))
    
    return results

if __name__ == "__main__":
     # Define the number of iterations and sample size manually
    iterations = 1000
    N_values = [10, 40, 4000]
    
    for N in N_values:
        results = simulate_and_recover(N, iterations)
        
        # Save results to file
        output_file = f"results_N{N}.log"
        with open(output_file, "w") as f:
            for entry in results:
                f.write(f"{entry}\n")
        
        print(f"Simulation for N={N} completed. Results saved in {output_file}")
    
    # Save results to file
   # with open(f"results_N{args.N}.log", "w") as f:
    #    for entry in results:
     #       f.write(f"{entry}\n")
    
    #print(f"Simulation for N={args.N} completed. Results saved in results_N{args.N}.log")
