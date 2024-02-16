 1) If there is a package related issue, please use the following
commands to install the missing packages.

srun pip install
/home/scur1004/Results/Reproducibility_ICR/icr/requirements.txt

srun pip install pyro-ppl srun pip install pandas==1.3.5 srun pip
install scipy==1.7.3 srun pip install seaborn==0.11.2 srun pip install
tqdm==4.62.3 srun pip install jax srun pip install numpyro srun pip
install torch srun pip install numpy

srun pip install -e /home/scur1004/Results/Reproducibility_ICR/icr

2\) Once the packages are installed, go to the job file for the
respective dataset and make sure to specifiy the confidence value for
which you want the results. Example (0.75,0.85 etc.)

3\) In the job files (ex Run_7\_var_covid.job), you will see the main
run command :

srun python \'scripts/run_experiments.py\' \'7var-covid\' 20000 200 0.75
2999
\'/home/scur1004/Results/Reproducibility_ICR/Reproducibility_Results/7var-covid/\'
3 \--NGEN 700 \--POP_SIZE 300 \--n_digits 1 \--nr_refits 5
\--predict_individualized True \--model_type rf

-the argument 0.75 is the confidence for which the results will be
obtained -NGEN specifies the number of generations -POP_SIZE specifies
the population size. -the path :
\'/home/scur1004/Results/Reproducibility_ICR/Reproducibility_Results/7var-covid/\'
is the path where the results will be stored -the value 3 corressponds
to the number of iterations you want to run the code for.

4\) After setting the desired parameters in the job file the job file
can be queued on snellius, using the following command:

sbatch Run_7\_var_covid.job

5\) Once the the file is queued a output file will be generated for
example Results_Conf_75_7var_covid.out and the results will be added to
a folder under the specified path in the job file.

6\) To read the result of each individual confidence value for a
specific dataset :  - Go the results folder for example
/Reproducibility_ICR/Reproducability_Results  - Navigate to the dataset
for which you want to see the results  - There you would see multiple
folders having a name like
N4000_Nrec200_gam0.75_t0.5_lbd300.0_nit3_NGEN600_POPS300_28, here the
0.75 after the term gam in the name refers to the confidence level.  -
Select the folder for the desired confidence level and you should be
able to see the aggregated results in csv format as well as different
folders corressponding to results for each iteration.

7\) Once you have obtained the result for all possible confidence
values, run the Run_Plot.job in a similar way, to obrain the plots and
the overall summary.
