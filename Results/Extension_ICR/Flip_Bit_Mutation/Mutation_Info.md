1\) The code change for the mutation changes apply to the
Shuffle_Index_Mutation & Flip_Bit_Mutation experiment.

2\) We run the experiment for the 3 variable non causal dataset with a
confidence of 0.75 .

3\) The code change is in the following file :

..Extension_ICR\\Shuffle_Index_Mutation\\icr\\src\\mcr\\recourse\\recourse.py

where we have replaced Gaussian Mutation with Shuffle_Index_Mutation and
Flip_Bit_Mutation function respectively. Ex: Original : proposal =
tools.mutGaussian(\[individual\[jj\]\], mu, sigma, indpb)\[0\]\[0\]
Change : proposal = tools.mutShuffleIndexes(\[individual\[jj\]\],
indpb)\[0\]\[0\]

4\) To run the experiment you use the same command :

Ex : sbatch Shuffle_Index.job

5\) The results would be available in the Shuffle_Index_Mutation_Results
& Flip_Bit_Mutation_Results folder respectively.

6\) We have not used plots here as the experiment is run only for a
single confidence value.
