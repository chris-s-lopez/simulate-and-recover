# simulate-and-recover
- EZ Diffusion Model Methodology uses 3 parameters Boundary Separation (0.5 - 2.0), drfit rate (0.5-2.0), and non-decision time (0.1 - 0.5)

- this was used to generate reaction times and accuracy data, and whether the estimated values were similar to the original simulated values 

- The simulation runs 1,000 times across different sample sizes (N = 10, 40, 4000).
- Within simulate.py, bias and squared error were measured to see how well it recovered the true/real parameters 

- The output of simulate.py follows this structure (N, (α_true, ν_true, τ_true), (α_est, ν_est, τ_est))
-  N = number of trials 
-  α_true = simulated Boundary separation
-  ν_true = simulated drift rate 
-  τ_true = simulated non decision time 

- α_est = recovered Boundary separation
- ν_est = recovered drift rate 
- τ_est = recovered non decision time 

### 1 - Small Sample size N=10
- Drift rate had highest estimation error - the most unstable (low negatives - high postives)
- non decision time was unreliable, sometimes producing NaN values
- Boundary separation, was most stable, but still had variable significance
### N = 10 inference 
- small N is not sufficient for accurate/true parameter estimation
- drift rate and non decision time need larger smaple sizes to be considered stable/meaningfull

### 2 - Medium Sample Size N = 40 
- drift rate still varibale (more stable than N = 10), less extreme
- Boundary seperation: stablizes significantly, closer to thier true values !
- non decision time: better than N= 10, reduced number of errors

### N = 40 inference 
- increaasing szie significantly reduces errors in boundary separation as well as non-decision time
- drift rate is still unstable (but less extreme)

### 3 - Large Sample Size N = 4000
- Boundary separation is highly accurate, was able to be recovered
- drift rate: shows improvemnt, but there were still extreme values - large errors
- Non-decision time - highly stable, larger N improves recovery

### N = 4000 inference 
- increasing the sample size to 4000 greatly influenced the significance of the estimation accuracy
- drift rate still remained the most difficult parameter to estimate - still extreme values
- Boundary seperation and non-decison time were well recovered

## Conclusions 
- EZ diffision Model performs better with larger sample sizes
- Drift Rate remianed to be the most difficult paramter to estimaye than Boundary seperation and Non-decision time
- N = 10 was the least reliable sample size
- N = 40 showed accurate recovery
- while N = 4000 produced reliable estimates

# Reflection/problems encountered 

I ran into trouble  running test.sh, where the script was unable to read simulate.py
and failed to import numpy. Even though numpy was installed and functioning correctly in simulate.py, the
problem was because I was not working inside the class-container. After switching to the 
class container and setting it up, I noticed that the Python interpreter was different from the one I 
had been using.

I realized that numpy was installed for Python 3.9, while the container was using Python 3.12, 
and raising the Module not found error. Fixing this took so much time, but I eventually resolved 
it by creating a virtual environment (venv) in Python 3.12. Within this venv, I installed 
numpy and scipy (I am not certain if installingscipy/numpy was necessary or if it was already satisfied, but it worked) 
After setting up the virtual environment, I modified test.sh to ensure that it properly logged the 
results for each sample size. And both tests ran successfully ! 
