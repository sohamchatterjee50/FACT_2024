1\) The code change for the mutation changes apply to the
Anomaly_Correction experiment.

2\) The original code had wrong casual variables for the SCM_PROGRAMMING
SCM, we corrected that and ran the code for a confidence of 0.75 .

3\) The main code change is in the following file :

..Extension_ICR\\Anomaly_Correction\\icr\\src\\mcr\\causality\\scms\\examples.py

The original dictionary storing the casual variables for the
SCM_PROGRAMMING SCM was :

fnc_dict={\'senior-level_skill\': fn_skilled, \'nr_commits\':
fn_nr_commits, \'nr_stars\': fn_nr_stars, \'fever\':
fn_fever,\'fatigue\': fn_fatigue}

we corrected it to :

fnc_dict={\'senior-level_skill\': fn_skilled, \'nr_commits\':
fn_nr_commits, \'nr_stars\': fn_nr_stars, \'nr_languages\':
fn_nr_languages}

4\) To run the experiment you use the same command :

sbatch 5_var_skill_corrected.job

5\) The results would be available in the Synthetic_Dataset_Results
folder.

6\) We have not used plots here as the experiment is run only for a
single confidence value.
