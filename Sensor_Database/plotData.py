from matplotlib import pyplot as plt
from scipy import stats

sensor_data = pd.read_table('Data.csv', index_col=['timestamp'])
sensor_data = sensor_data[['X axes', 'Y axes', 'Z axes']]
print(sensor_data)