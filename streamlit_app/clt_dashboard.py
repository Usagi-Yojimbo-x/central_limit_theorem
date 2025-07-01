
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Central Limit Theorem (CLT) Dashboard")

st.write("As sample size increases, the sampling distribution of the sample mean apporaches normality--even if the population distribution is skewed or non-normal.")

# sidebar
population_options = ["Right Skewed", "Left Skewed", "Uniform", "Normal"]
population_type = st.sidebar.selectbox("Choose Population Distribution", population_options)
sample_size = st.sidebar.slider("Sample Size (n)", min_value=1, max_value=100, value=10)
num_samples = st.sidebar.slider("Number of Samples", min_value=10, max_value=1000, value=100)

def generate_pop(size=10000):
    if population_type == "Right Skewed":
        return np.random.exponential(scale=1.0, size=size)
    if population_type == "Left Skewed":
        return -np.random.exponential(scale=1.0, size=size)
    if population_type == "Uniform":
        return np.random.uniform(low=0.0, high=10.0, size=size)
    if population_type == "Normal":
        return np.random.normal(loc=0, scale=1.0, size=size)
    
population = generate_pop()

sample_means = []
for _ in range(num_samples):
    sample_means.append(np.random.choice(population, size=sample_size).mean())

fig, axs = plt.subplots(1,2, figsize=(12, 5))
axs[0].hist(population, bins=30, color='#1db954', edgecolor='white', density=True)
axs[0].set_title("Population Distribution")
sns.kdeplot(population, ax=axs[0], color='#b91d7a')

axs[1].hist(sample_means, bins=30, color='#1db954', edgecolor='white', density=True)
axs[1].set_title("Sampling Distribution of the Mean")
sns.kdeplot(sample_means, ax=axs[1], color='#b91d7a')


for ax in axs:
    ax.grid(axis='y', alpha=0.3)
    ax.spines[['top', 'right', 'left']].set_visible(False)

st.pyplot(fig)

# summary stats
st.write("**Population Mean:**", np.round(np.mean(population), 2))
st.write("**Mean of Sample Means:**", np.round(np.mean(sample_means), 2))
st.write("**Standard Error:**", np.round(np.std(sample_means), 2))

