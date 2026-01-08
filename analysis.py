import pandas as pd

# Load CSV
df = pd.read_csv("data/student_marks.csv")
print("First 5 rows of the dataset:")
print(df.head())

import pandas as pd

df = pd.read_csv("data/student_marks.csv")

# Check column names
print("Columns in CSV:", df.columns)


# 1️⃣ Average marks per student (only exam columns)
exam_cols = ["exam1", "exam2", "exam3"]
df["Average"] = df[exam_cols].mean(axis=1)
print("\nAverage marks per student:")
print(df[["semester", "sex", "Average"]])

# 2️⃣ Average marks per exam
exam_averages = df[exam_cols].mean()
print("\nAverage marks per exam:")
print(exam_averages)

# 3️⃣ Weakest exam
weak_exam = exam_averages.idxmin()
print(f"\nWeakest exam: {weak_exam}")

# 4️⃣ Top 3 students
top_students = df.sort_values(by="Average", ascending=False).head(3)
print("\nTop 3 students:")
print(top_students[["semester", "sex", "Average"]])

import matplotlib.pyplot as plt

# Average marks per exam
exam_avg = df[['exam1', 'exam2', 'exam3']].mean()

# Bar chart
plt.figure(figsize=(8,5))
plt.bar(exam_avg.index, exam_avg.values, color='skyblue')
plt.title('Average Marks per Exam')
plt.ylabel('Average Marks')
plt.ylim(0, 100)
plt.show()

# Sort students by Average descending
top_students = df_avg.sort_values(by='Average', ascending=False).head(10)

# Bar chart for top 10
plt.figure(figsize=(10,5))
plt.bar(top_students.index.astype(str), top_students['Average'], color='lightgreen')
plt.title('Top 10 Students by Average Marks')
plt.xlabel('Student Index')
plt.ylabel('Average Marks')
plt.ylim(0, 100)
plt.show()
