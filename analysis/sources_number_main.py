import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'brazil_sedimentary_basins.csv')

df = pd.read_csv(csv_path)
sources_number_main = df.groupby('AI')['sources_number'].mean()
print(sources_number_main)

sns.barplot(data=df, x='question_number', y='sources_number', hue='AI')
plt.title('Analyse - sources_number por question_number')
plt.xticks(rotation=100)
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'sources_number_plot.png'))