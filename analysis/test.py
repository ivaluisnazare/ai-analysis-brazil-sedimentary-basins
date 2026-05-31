# sources_number_main.py
# Analysis of sources used by AI models per test date
# with bar and pie charts saved side by side in a single file

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load and prepare data
# -----------------------------
file_path = "brazil_sedimentary_basins.csv"
try:
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully from '{file_path}'")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    exit(1)

# Clean and convert
df['sources_number'] = pd.to_numeric(df['sources_number'], errors='coerce')
df['test_date'] = pd.to_datetime(df['test_date'], errors='coerce')
df_clean = df.dropna(subset=['AI', 'test_date', 'sources_number'])

# print(df_clean)

# Group by date and AI (sum of sources)
grouped = df_clean.groupby(['test_date', 'AI'])['sources_number'].sum().reset_index()
grouped = grouped.sort_values(['test_date', 'AI'])

print("grouped data: be here")
print(grouped)

# Pivot for bar chart (dates as rows, AI as columns)
pivot = grouped.pivot(index='test_date', columns='AI', values='sources_number')

# Overall totals per AI for pie chart
total_per_ai = df_clean.groupby('AI')['sources_number'].sum()

# -----------------------------
# 2. Create side‑by‑side plots (bar and pie)
# -----------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Bar chart (left) ---
# Prepare bar plot data: convert dates to string labels
bar_data = pivot.copy()
bar_data.index = bar_data.index.strftime('%Y-%m-%d')
bar_data.plot(kind='bar', ax=ax1, width=0.7, edgecolor='black')
ax1.set_title('Total Sources Number per AI and Test Date')
ax1.set_xlabel('Test Date')
ax1.set_ylabel('Sum of Sources Number')
ax1.legend(title='AI')
ax1.grid(axis='y', linestyle='--', alpha=0.7)
# Rotate x labels if needed
ax1.tick_params(axis='x', rotation=45)

# --- Pie chart (right) ---
# Show overall proportion of sources used by each AI
colors = ['#66b3ff', '#ff9999']
wedges, texts, autotexts = ax2.pie(
    total_per_ai.values,
    labels=total_per_ai.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    explode=(0.05, 0),
    shadow=True
)
ax2.set_title('Overall Sources Share per AI')

# Improve text size
for text in texts + autotexts:
    text.set_fontsize(10)

# Equal aspect ratio ensures pie is circular
ax2.axis('equal')

# -----------------------------
# 3. Save and show
# -----------------------------
plt.tight_layout()
output_file = 'bar_pie_side_by_side.png'
plt.savefig(output_file, dpi=150, bbox_inches='tight')
print(f"Chart saved as '{output_file}'")

# Optional: display if running interactively
# plt.show()

# -----------------------------
# 4. Print summary tables to console
# -----------------------------
print("\n=== Total sources per AI and test date ===")
print(grouped.to_string(index=False))

print("\n=== Overall total sources per AI ===")
print(total_per_ai)