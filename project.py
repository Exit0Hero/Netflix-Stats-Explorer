# making a netflix data visualization, so we can understand the cotent that Netflix provides also, the trends of the shows !
# steps: 1st load the data with pandas
# clean the data : handle missing files, removing duplicate, fix columns if needed
# understand the data use head(), info(), desribe() to explore data
# identify questions to answer
# plot the data using matplotlib
# save the data using plt.savefig()


# Netflix Data Visualization Project - Professional Version

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_excel("mymoviedb.xlsx", nrows=889)

# Drop rows with important missing values
df.dropna(subset=["Release_Date", "Title", "Popularity", "Vote_Count", "Overview", 
                  "Vote_Average", "Original_Language", "Genre", "Poster_Url"], inplace=True)

# Convert Release_Date to datetime
df['Release_Year'] = pd.to_datetime(df['Release_Date'], errors='coerce').dt.year

# Cleaned dataset
print("Cleaned dataset shape:", df.shape)

# ------------------ 1. Popularity ------------------
top_popular = df.sort_values("Popularity", ascending=False).head(15)
fig = px.bar(top_popular, x='Title', y='Popularity', color='Genre', 
             title='Top 15 Most Popular Netflix Movies/TV Shows',
             labels={'Popularity': 'Popularity Score'})
fig.show()

# ------------------ 2. Vote Count Distribution ------------------
plt.figure(figsize=(10,6))
sns.histplot(df["Vote_Count"], bins=40, kde=True, color="crimson")
plt.title("Distribution of Vote Counts")
plt.xlabel("Vote Count")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# ------------------ 3. Genre Distribution ------------------
genre_counts = df['Genre'].value_counts().nlargest(10)
fig = px.pie(names=genre_counts.index, values=genre_counts.values, 
             title="Top 10 Movie/Show Genres", hole=0.4)
fig.show()

# ------------------ 4. Language Distribution ------------------
lang_counts = df['Original_Language'].value_counts().nlargest(15)
fig = px.bar(lang_counts, x=lang_counts.values, y=lang_counts.index, orientation='h',
             title="Top 15 Original Languages", labels={'x': 'Number of Titles', 'y': 'Language'})
fig.show()

# ------------------ 5. Movies Released Per Year ------------------
year_counts = df['Release_Year'].value_counts().sort_index()
plt.figure(figsize=(12,6))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker='o', color='blue')
plt.title("Netflix Titles Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# ------------------ 6. Popularity vs Vote Count ------------------
fig = px.scatter(df, x='Vote_Count', y='Popularity', color='Genre', size='Vote_Average',
                 title='Popularity vs. Vote Count (Size = Vote Avg)')
fig.show()


