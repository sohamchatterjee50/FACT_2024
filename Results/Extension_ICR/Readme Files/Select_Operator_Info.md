1\) The code change for the select operator changes apply to the
Best_Selection_Operator, Random_Selection_Operator &
SPEA_Selection_Operator experiment.

2\) We run the experiment for the 3 variable non causal dataset with a
confidence of 0.75 .

3\) The code change is in the following file :

..Extension_ICR\\Best_Selection_Operator\\icr\\src\\mcr\\recourse\\recourse.py

where we have replaced default selection operator which is based on
NSGA-2 with BestSelect, RandomSelect & SPEA_2 based select operators
respectively. Ex: Original : toolbox.register(\"select\",
tools.selNSGA2) Change : toolbox.register(\"select\", tools.selBest)

4\) To run the experiment you use the same command :

Ex : sbatch Best_Selection.job

5\) The results would be available in the Best_Selection_Results,
Random_Selection_Results & SPEA_Selection_Results folder respectively.

6\) We have not used plots here as the experiment is run only for a
single confidence value.

7\) We have run the Best_Selection_Operator with the ear flag on, to
understand the impact of our experiment on the environment, However
other jobs were run without it.

The job file has the following flags on. #SBATCH \--ear=on #SBATCH
\--ear-policy=monitoring #SBATCH \--ear-verbose=1
