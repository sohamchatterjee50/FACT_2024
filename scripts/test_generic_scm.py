import logging
import mcr.causality.examples as ex
import time
import pandas as pd

savepath = '~/data/mcr-experiments/test_generic/run1/'

population_size = 50

logging.getLogger().setLevel(logging.INFO)

scm = ex.SCM_3_VAR_NONCAUSAL
y_name = 'y'
scm.set_prediction_target(y_name)

context = scm.sample_context(population_size)
data = scm.compute()

temperature = 1
warmup_steps = 500
num_samples = 1000

obs = data.iloc[0, [0, 1, 3]]
gt = context.iloc[0]
print(obs)
print(gt)

scm_abd = scm.abduct(obs, infer_type='mcmc', warmup_steps=warmup_steps, num_samples=num_samples,
                     num_chains=1, temperature=temperature)

import torch
def compute_expected(obs):
    py = torch.sigmoid(torch.tensor(obs['x1'] + obs['x2']))
    dch1 = torch.distributions.Normal(torch.tensor(obs['x1'] + obs['x2'] + 1), torch.tensor(1))
    pch1 = dch1.log_prob(torch.tensor(obs['x3']))
    dch0 = torch.distributions.Normal(torch.tensor(obs['x1'] + obs['x2']), torch.tensor(1))
    pch0 = dch0.log_prob(torch.tensor(obs['x3']))

    c1 = torch.log(py) + pch1
    c2 = torch.log(1 - py) + pch0

    print(torch.exp(c1), torch.exp(c2))
    return torch.exp(c1) / (torch.exp(c1) + torch.exp(c2))

print(f"theory: {compute_expected(obs)}, practice: {scm_abd.model['y']['noise_distribution'].mixing_distribution.probs[1]}")

# data.to_csv(savepath + 'data.csv')
# context.to_csv(savepath + 'context.csv')

num_chains = 1

dfs_dist = []
for temperature in [0, 1]:
    print(f"temp: {temperature}")
    for warmup_steps in [10, 50, 100, 300]:
        print(f"warmup_steps: {warmup_steps}")
        for num_samples in [50, 100, 200, 500, 1000]:
            print(f"num_samples: {num_samples}")
            dists = []
            for ii in range(population_size):
                print(f"ii: {ii}/{population_size}")
                t0 = time.time()
                scm_abd = scm.abduct(data.iloc[ii, [0, 1, 3]], infer_type='mcmc',
                                     warmup_steps=warmup_steps, num_samples=num_samples, num_chains=num_chains,
                                     temperature=temperature)
                t1 = time.time()
                time_elapsed = t1 - t0

                cntxt = scm_abd.sample_context(10000)
                post_sample = scm_abd.compute()

                dist = data.iloc[ii, [0, 1, 3]] - (post_sample.describe().loc['mean', ['x1', 'x2', 'x3']])

                dist['y_est'] = post_sample.describe().loc['mean', 'y']
                dist['time'] = time_elapsed
                dist['num_samples'] = num_samples
                dist['num_chains'] = num_chains
                dist['warmup_steps'] = warmup_steps
                dist['temperature'] = temperature

                dists.append(dist)

            df_dists = pd.concat(dists, axis=1).T
            df_dists.to_csv(savepath + f"diff_{warmup_steps}_{num_samples}.csv")

            df_dists = df_dists.reset_index()
            dfs_dist.append(df_dists)

dff = pd.concat(dfs_dist, ignore_index=True)
dff.to_csv(savepath + 'dff.csv')