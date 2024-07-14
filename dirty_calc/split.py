import pandas as pd

data = pd.read_csv('datasets/gdb11_10ha_cnos_dienophiles.csv')

d1 = data.iloc[:100000,:]
d2 = data.iloc[100001:200000,:]
d3 = data.iloc[200001:300000,:]
d4 = data.iloc[300001:400000,:]
d5 = data.iloc[400001:500000,:]
d6 = data.iloc[500001:600000,:]
d7 = data.iloc[600001:700000,:]
d8 = data.iloc[700001:800000,:]
d9 = data.iloc[800001:900000,:]
d10 = data.iloc[900000:,:]

d1.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_1.csv', index=False)
d2.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_2.csv', index=False)
d3.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_3.csv', index=False)
d4.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_4.csv', index=False)
d5.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_5.csv', index=False)
d6.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_6.csv', index=False)
d7.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_7.csv', index=False)
d8.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_8.csv', index=False)
d9.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_9.csv', index=False)
d10.to_csv('dirty_calc/gdb11_10ha_cnos_dienophiles_10.csv', index=False)