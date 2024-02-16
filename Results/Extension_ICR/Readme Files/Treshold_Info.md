1\) The experiment and the results are in the Threshold_Change folder.

2\) There are no code changes for this experiment,

3\) We run the experiment for the 7 variable covid dataset with a
confidence of 0.75 .

4\) To run the experiment you use the same command :

Ex : sbatch Threshold_Change.job

5\) In the job file, to the run command we add an additional runtime
argument \'\--thresh 0.8\', which specifies the treshold which we are
running the experiment for. The default value for this 0.5.

original command : srun python \'scripts/run_experiments.py\'
\'7var-covid\' 20000 200 0.75 2999
\'/home/scur1004/ICR_Threshold_Change/Threshold_Change/7var-covid/\' 3
\--NGEN 700 \--POP_SIZE 300 \--n_digits 1 \--nr_refits 5
\--predict_individualized True \--model_type rf new command : srun
python \'scripts/run_experiments.py\' \'7var-covid\' 20000 200 0.75 2999
\'/home/scur1004/ICR_Threshold_Change/Threshold_Change/7var-covid/\' 3
\--NGEN 700 \--POP_SIZE 300 \--n_digits 1 \--nr_refits 5
\--predict_individualized True \--model_type rf \--thresh 0.8

For the same dataset we run the experiment for two different treshold
values : 0.2 & 0.8.

5\) The results would be available in the Threshold_Change folder .

6\) We have not used plots here as the experiment is run only for a
single confidence value.