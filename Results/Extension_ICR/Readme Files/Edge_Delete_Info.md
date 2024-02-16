1\) The experiment is highlighted in the Edge_Deletion folder.

2\) We run the experiment for the 5 variable skill & 7 variable covid
datasaet with a confidence of 0.75.

3\) The code change is in the following file :

\...Extension_ICR\\Edge_Deletion\\icr\\src\\mcr\\causality\\scms\\examples.py

Here, for both datasets, we have modified the adjacency matrices for the
SCMS (SCM_PROGRAMMING & SCM_COVID) to eliminate one edge and the
corresponding transitive dependencies. Ex:

For the 5 variable dataset, the SCM_Programming Original Matrix was :

\[ \[0, 0, 1, 1, 0, 0\], \[0, 0, 1, 0, 0, 0\],sc \[0, 0, 0, 1, 1, 1\],
\[0, 0, 0, 0, 0, 0\], \[0, 0, 0, 0, 0, 0\], \[0, 0, 0, 0, 0, 0\] \]

which was changed to :

\[ \[0, 0, 1, 0, 0, 0\], \[0, 0, 1, 0, 0, 0\], \[0, 0, 0, 1, 1, 1\],
\[0, 0, 0, 0, 0, 0\], \[0, 0, 0, 0, 0, 0\], \[0, 0, 0, 0, 0, 0\] \]

4\) To run the experiment you use the same command :

Ex : sbatch Edge_Delete_5\_Var.job

5\) The results would be available in the Edge_Delete_Results folder.

6\) We have not used plots here as the experiment is run only for a
single confidence value.