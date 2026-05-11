# sources_number_main.py
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

# --- Bar plot (original requirement) ---
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='question_number', y='sources_number', hue='AI')
plt.title('Analysis - sources_number per question_number')
plt.xticks(rotation=100)
plt.tight_layout()
barplot_path = os.path.join(script_dir, 'sources_number_plot.png')
plt.savefig(barplot_path)
plt.close()  # close to avoid overlapping with next plot

# --- Pie chart (new requirement) ---
plt.figure(figsize=(7, 7))
plt.pie(sources_number_main, labels=sources_number_main.index, autopct='%1.1f%%',
        startangle=90, colors=['lightcoral', 'lightskyblue'])
plt.title('Average Sources Number per AI')
pie_path = os.path.join(script_dir, 'sources_number_pie.png')
plt.savefig(pie_path)
plt.close()

print(f"\nBar plot saved as: {barplot_path}")
print(f"Pie chart saved as: {pie_path}")