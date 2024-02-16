1\) The code change for the mutation changes apply to the
Synthetic_Dataset experiment.

2\) We create our own 4 variable synthetic dataset and run the
experiment for a confidence of 0.75 . (NOTE : We have called it a 5
variable synthetic dataset by mistake as it cosnists of 5 variables in
total which includes 4 causal and 1 outcome variable, so it is actually
a 4 variable dataset.)

3\) The main code change is in the following file :

..Extension_ICR\\Synthetic_Dataset\\icr\\src\\mcr\\causality\\scms\\examples.py

Here we have added a new SCM by the name SCM_5\_VAR_SYNTHETIC,

SCM_5\_VAR_SYNTHETIC = GenericSCM( dag=DirectedAcyclicGraph(
adjacency_matrix=np.array(\[\[0, 1, 1, 1, 0\], \[0, 0, 0, 1, 1\], \[0,
1, 0, 1, 1\], \[0, 0, 0, 0, 1\], \[0, 0, 0, 0, 0\]\]),
var_names=\[\'x1\', \'x2\', \'x3\', \'x4\',\'y\'\] ),
noise_dict={\'x1\': normal_dist, \'x2\': normal_dist, \'x3\':
normal_dist_small_var, \'x4\':normal_dist_small_var, \'y\': unif_dist},
fnc_dict={y_name: sigmoidal_binomial}, fnc_torch_dict={y_name:
sigmoidal_binomial_torch}, sigmoidal=\[y_name\], costs=\[1.0, 1.0,
1.0,1.0\], y_name=y_name )

4\) To run the experiment you use the same command :

sbatch Synthetic_Dataset.job

also insde the job file the run command has the new dataset as a runtime
argument (5var-synthetic).

5\) The results would be available in the Synthetic_Dataset_Results
folder.

6\) We have not used plots here as the experiment is run only for a
single confidence value.
