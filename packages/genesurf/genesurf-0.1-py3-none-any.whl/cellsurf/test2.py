import pandas as pd
from utils.data_pp import spatial_pp
from utils.deconvolution import deconvolution_multi_ctn
from utils.get_data_from_h5 import get_data_from_h5
from utils.cell_type_visualization import visualize_lineplot, celltype_visualization_visium

data_dir = 'example_data/CRLM_visium/raw_data/'
save_dir = 'example_data/simulated_data/pp_data/'
expr_path = data_dir + '/filtered_feature_bc_matrix.h5'
pos_path = data_dir + '/tissue_positions_list.csv'

filtered_matrix_h5 = get_data_from_h5(expr_path)
df_expr = pd.DataFrame(filtered_matrix_h5.matrix.A, columns=filtered_matrix_h5.barcodes.astype(str), index=filtered_matrix_h5.feature_ref['name'].astype(str))
df_expr = df_expr.T
df_pos = pd.read_csv(pos_path, index_col=0, header=None)
df_pos = df_pos.loc[df_pos.iloc[:, 0] == 1].iloc[:, 1:3]
df_pos.rename(columns={df_pos.columns[0]: 'x'}, inplace=True)
df_pos.rename(columns={df_pos.columns[1]: 'y'}, inplace=True)
df_pos['x'] = df_pos['x'] - df_pos['x'].min()
df_pos['y'] = df_pos['y'] - df_pos['y'].min()
df_expr = df_expr.reindex(df_pos.index)

df_expr.reset_index(drop=True, inplace=True)
df_pos.reset_index(drop=True, inplace=True)
barcodes = df_pos.index.to_numpy()

df_pp_data = spatial_pp(df_expr, df_pos, barcodes, save_dir)
df_deconvolution_data = deconvolution_multi_ctn(df_pp_data, cell_type_num=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], spatial_mode='hexagon', save_dir_name='CRLM_visium', margin=0.05, device_id=0, num_epoch=2)

# Here we use the deconvolution results of epoch=500 for further exploration.
results_dir = 'results_save/CRLM_visium_example2'
df_deconvolution_data = pd.read_csv(results_dir + '/CRLM_visium.csv')

# Plot cell type number K versus perplexity and rare cell type number
cell_type_num = df_deconvolution_data.iloc[:, 0]
ppl = df_deconvolution_data.iloc[:, 2]
rare_cell_type_num = df_deconvolution_data.iloc[:, 1]
visualize_lineplot(cell_type_num, ppl, rare_cell_type_num)

# Choose a suitable cell_type_num for further visualization (The optimal cell type number K is determined at the point where reaches the lowest perplexity while minimizing the rare cell type number ideally. It is reconmmended to choose the cell type number with a low perplexity but not very high rare cell type number (less than 3). Moreover, the user can choose the optimal K with the help their biology knowledge.)
cell_type_num = 11
df_pred_ = pd.read_csv(results_dir + f'/prediction_save/cell_type_num_{cell_type_num}/pred.csv')
df_pos_ = df_pp_data.iloc[:, 1:3]
celltype_visualization_visium(df_pred_, df_pos_, col_num=6)

