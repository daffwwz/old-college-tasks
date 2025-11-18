import pandas as pd
import matplotlib.pyplot as plt

# Membuat list dataframe untuk 4 jenis garam carrier
dfs1 = []
dfs2 = []
dfs3 = []
dfs4 = []

# membuat list ketinggian maksimum dan waktu pada step
heights1 = []
time_values1 = []
heights2 = []
time_values2 = []
heights3 = []
time_values3 =[]
heights4 = []
time_values4 =[]

# Membuat loop untuk mengolah data .csv dari step 45 hingga 65 dengan jarak 5 step
for i in range(45, 66, 5):
    filename = f'salt1_{i}.csv' # untuk garam carrier 1
    df1 = pd.read_csv(filename)
    dfs1.append(df1)
    max_height1 = (0.923 + df1['y'].max()) * 1000
    heights1.append(max_height1)

    # Mengambil data waktu berdasarkan indeks dari ketinggian maksimal
    time_value1 = df1.loc[df1['y'].idxmax()]['time']  
    time_values1.append(time_value1)

for i in range(45, 66, 5):
    filename = f'salt2_{i}.csv' # untuk garam carrier 2
    df2 = pd.read_csv(filename)
    dfs2.append(df2)
    max_height2 = (0.923 + df2['y'].max()) * 1000
    heights2.append(max_height2)
    time_value2 = df2.loc[df2['y'].idxmax()]['time']  
    time_values2.append(time_value2)

for i in range(45, 66, 5):
    filename = f'salt3_{i}.csv'
    df3 = pd.read_csv(filename)
    dfs3.append(df3)
    max_height3 = (0.923 + df3['y'].max()) * 1000
    heights3.append(max_height3)
    time_value3 = df3.loc[df3['y'].idxmax()]['time']  
    time_values3.append(time_value3)

for i in range(45, 66, 5):
    filename = f'salt4_{i}.csv'
    df4 = pd.read_csv(filename)
    dfs4.append(df4)
    max_height4 = (0.923 + df4['y'].max()) * 1000
    heights4.append(max_height4)
    time_value4 = df4.loc[df4['y'].idxmax()]['time'] 
    time_values4.append(time_value4)

plt.plot(time_values1, heights1, label='LiF-NaF-KF')
plt.plot(time_values2, heights2, label='LiF-BeF')
plt.plot(time_values3, heights3, label='KCl-MgCl2', linestyle='none', marker='none')
plt.plot(time_values4, heights4, label='NaNO3-NaNO2-KNO3')
plt.legend()
plt.title('Ketinggian maksimal tiap step terhadap waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Ketinggian (mm)')
plt.grid(True)
plt.show()

