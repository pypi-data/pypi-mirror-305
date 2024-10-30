import pandas as pd
from utils.data_pp import spatial_pp
import numpy as np
from utils.deconvolution import deconvolution
from utils.calculate_cell_type_expression import calc_cell_type_expr
from utils.cell_type_matching import cell_type_matching
import seaborn as sns
import matplotlib.pyplot as plt
from utils.cell_type_visualization import celltype_visualization_ST

data_dir = 'example_data/simulated_data/raw_data/'
save_dir = 'example_data/simulated_data/pp_data/'
expr_path = data_dir + '/count.csv'
pos_path = data_dir + '/pos.csv'

df_expr = pd.read_csv(expr_path)
df_pos = pd.read_csv(pos_path)
df_pos['x'] = df_pos['x'] - df_pos['x'].min()
df_pos['y'] = df_pos['y'] - df_pos['y'].min()
barcodes = np.array(range(len(df_expr)))

df_pp_data = spatial_pp(df_expr, df_pos, barcodes, save_dir)

df_deconvolution_results, df_beta = deconvolution(df_pp_data, cell_type_num=4, spatial_mode='square', save_dir_name='simulated_data', margin=0.05, device_id=0, num_epoch=5)

# Here we use the deconvolution results of epoch=500 for further exploration.
results_dir = 'results_save/simulated_data_example1'
df_deconvolution_results = pd.read_csv(results_dir + '/prediction_save/pred.csv')
df_beta = pd.read_csv(results_dir + '/prediction_save/beta.csv')

sc_data_path = data_dir + 'sc_data.csv'
df_sc = pd.read_csv(sc_data_path)
df_gt_expr = calc_cell_type_expr(df_sc, save_dir)
df_matching_results, df_corr = cell_type_matching(df_gt_expr, df_beta)

plt.figure(figsize=(5, 4))
sns.heatmap(df_corr, annot=True, cmap='YlGnBu', linewidths=0.5)
plt.title('Cell type matching')
plt.show()

