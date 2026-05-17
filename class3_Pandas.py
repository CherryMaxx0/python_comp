import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Excel\student.csv")

# df.info()

math_score = df['Math']


# high_maths = df[df['Math']>80]
# print(high_maths)


# high_physics = df[df['Physics']>80]
# print(high_physics)


df['Average'] = df[['Math','Physics','Chemistry']].mean(axis=1)
print(df)

# df_sorted = df.sort_values(by='Average',ascending=False)
# print(df_sorted)
# df_sorted_Chemistry = df.sort_values(by='Chemistry',ascending=False)
# print(df_sorted_Chemistry)


df['Average'].hist(bins=5)
plt.title('Distribution of Average Score')
plt.xlabel('Score')
plt.ylabel('Number of students')
plt.show()



