
"""
DM ASSIGNMENT 2 
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import scipy.stats as stats
warnings.filterwarnings('ignore')


data= pd.read_csv('student_data.csv')
df = data.copy()
print(df.describe())
print(df.sample(5))
print(df.shape)
print(df.info())

print(df.sex.nunique())
print(df.age.max())

sns.set_context("talk")

sns.set_style("whitegrid")
colors = sns.color_palette('pastel')[0:5]
plt.figure(figsize=(10,8))
df.school.value_counts().plot(kind='pie', autopct='%.0f%%', colors = colors,)
plt.title('School proportion in %')
plt.legend()


plt.figure(figsize=(10,8))
df.sex.value_counts().plot(kind='pie', autopct='%.0f%%', colors = colors)
plt.title('Sex proportion in %')
plt.legend()


plt.figure(figsize=(10,8))
sns.countplot(data = df, x='famsize', palette = colors, order = df.famsize.value_counts().index)
plt.title('Size of family')




fig, axes = plt.subplots(1, 2, figsize=(15, 8),sharey=True)

# Medu
sns.countplot(ax=axes[0], data = df, x='Medu', palette = colors)
axes[0].set_title('Mother Education')

# Fedu
sns.countplot(ax=axes[1], data = df, x='Fedu', palette = colors)
axes[1].set_title('Father Education')


fig, axes = plt.subplots(1, 2, figsize=(15, 8), sharey=True)
order2 = ['at_home','teacher','health','services','other']

# Mjob
sns.countplot(ax=axes[0], data = df, x='Mjob', palette = colors, order=order2)
axes[0].set_title('Mother Job')

# Fjob
sns.countplot(ax=axes[1], data = df, x='Fjob', palette = colors, order=order2)
axes[1].set_title('Father Job')



plt.figure(figsize=(10,8))
df.guardian.value_counts().plot(kind='pie', autopct='%.0f%%', colors = colors,)
plt.title('Guardian proportion in %')
plt.legend()

fig, axes = plt.subplots(1, 2, figsize=(15, 8), sharey=True)
order2 = [1,2,3,4]

# Mjob
sns.countplot(ax=axes[0], data = df, x='traveltime', palette = colors, order=order2)
axes[0].set_title('Travel time')

# Fjob
sns.countplot(ax=axes[1], data = df, x='studytime', palette = colors, order=order2)
axes[1].set_title('Study time')

plt.figure(figsize=(10,8))
sns.countplot(data = df, x='health', palette = colors)
plt.title('Health')

plt.figure(figsize=(10,8))
sns.histplot(data = df, x='absences', bins=15, palette = colors)
plt.title('Absences Distributiion')
print(df.query('absences > 30'))

fig, axes = plt.subplots(1, 3, figsize=(15,5),sharey=True)

# G1
sns.histplot(ax=axes[0], data = df, x='G1', palette = colors, bins = 12)
axes[0].set_title('Grade 1 Distribution')

# G2
sns.histplot(ax=axes[1], data = df, x='G2', palette = colors, bins = 12)
axes[1].set_title('Grade 2 Distribution')

# G3
sns.histplot(ax=axes[2], data = df, x='G3', palette = colors, bins = 12)
axes[2].set_title('Grade 3 Distribution')




