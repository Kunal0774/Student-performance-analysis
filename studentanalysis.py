# ============================================
# 📊 STUDENT PERFORMANCE DATA ANALYSIS PROJECT
# ============================================

# 🔷 1. IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('ggplot')

# ============================================
# 🔷 2. LOAD DATASET
# ============================================

file_path = r"E:\KUNAL!!!\PROJECTS!!!!\student analysis\Student_performance_data _.csv"
df = pd.read_csv(file_path)

print("\n✅ DATA LOADED SUCCESSFULLY\n")

# ============================================
# 🔷 3. BASIC DATA UNDERSTANDING
# ============================================

print("\n🔹 FIRST 5 ROWS:\n")
print(df.head())

print("\n🔹 DATA INFO:\n")
print(df.info())

print("\n🔹 STATISTICS:\n")
print(df.describe())

# ============================================
# 🔷 4. DATA CLEANING
# ============================================

print("\n🔹 CHECKING MISSING VALUES:\n")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert data types
df['Gender'] = df['Gender'].astype('category')
df['GradeClass'] = df['GradeClass'].astype('category')

print("\n✅ DATA CLEANING DONE\n")

# ============================================
# 🔷 5. EXPLORATORY DATA ANALYSIS (EDA)
# ============================================

# 📊 5.1 GPA Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['GPA'], kde=True)
plt.title("GPA Distribution")
plt.xlabel("GPA")
plt.ylabel("Count")
plt.show()

# 📊 5.2 Gender vs GPA
plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='GPA', data=df)
plt.title("Gender vs GPA")
plt.show()

# 📊 5.3 Study Time vs GPA
plt.figure(figsize=(6,4))
sns.scatterplot(x='StudyTimeWeekly', y='GPA', data=df)
plt.title("Study Time vs GPA")
plt.show()

# 📊 5.4 Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# 📊 5.5 Extracurricular Activities vs GPA
activities = ['Sports', 'Music', 'Volunteering']

for act in activities:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=act, y='GPA', data=df)
    plt.title(f"{act} vs GPA")
    plt.show()

# ============================================
# 🔷 6. INSIGHTS GENERATION
# ============================================

print("\n🔷 KEY INSIGHTS:\n")

avg_gpa = df['GPA'].mean()
print(f"✔ Average GPA: {avg_gpa:.2f}")

study_corr = df['StudyTimeWeekly'].corr(df['GPA'])
print(f"✔ Study Time vs GPA Correlation: {study_corr:.2f}")

sports_impact = df.groupby('Sports')['GPA'].mean()
print("\n✔ Sports Participation Impact on GPA:\n", sports_impact)

music_impact = df.groupby('Music')['GPA'].mean()
print("\n✔ Music Participation Impact on GPA:\n", music_impact)

volunteer_impact = df.groupby('Volunteering')['GPA'].mean()
print("\n✔ Volunteering Impact on GPA:\n", volunteer_impact)

# ============================================
# 🔷 7. SAVE CLEANED DATA FOR POWER BI
# ============================================

df.to_csv("cleaned_student_data.csv", index=False)

print("\n✅ Cleaned dataset saved as 'cleaned_student_data.csv'")
print("👉 Use this file in Power BI")

# ============================================
# 🔷 8. FINAL MESSAGE
# ============================================

print("\n🎯 PROJECT COMPLETED SUCCESSFULLY!")
print("👉 You can now create Power BI Dashboard using cleaned data.")