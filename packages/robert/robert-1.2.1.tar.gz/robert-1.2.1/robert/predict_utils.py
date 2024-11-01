#####################################################.
#     This file stores functions from PREDICT       #
#####################################################.

import os
import sys
import ast
import shutil
from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sb
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
# for users with no intel architectures. This part has to be before the sklearn imports
try:
    from sklearnex import patch_sklearn
    patch_sklearn(verbose=False)
except (ModuleNotFoundError,ImportError):
    pass
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.inspection import permutation_importance
from sklearn.metrics import matthews_corrcoef, make_scorer
import shap
from robert.curate import curate
from robert.utils import (
    load_model,
    standardize,
    load_dfs,
    load_database,
    get_graph_style,
    pearson_map
    )


def load_test(self, Xy_data, params_df, Xy_test_df):
    ''''
    Loads Xy data of the test set
    '''

    descs_model = ast.literal_eval(params_df['X_descriptors'][0])
    Xy_test_csv, X_test_csv, y_test_csv = pd.DataFrame(),pd.DataFrame(),pd.DataFrame()

    # test points coming from the files specified in csv_test
    if self.args.csv_test != '':
        Xy_test_csv = load_database(self, self.args.csv_test, "predict")
        X_test_csv, y_test_csv = test_csv(self,Xy_test_csv,descs_model,params_df)
        Xy_data['X_csv_test'] = X_test_csv
        Xy_data['y_csv_test'] = y_test_csv
        _, Xy_data['X_csv_test_scaled'] = standardize(self,Xy_data['X_train'],Xy_data['X_csv_test'])
        Xy_test_df = Xy_test_csv

    # test points coming from the test_set option (from GENERATE)
    if len(Xy_data['X_test']) > 0:
        _, Xy_data['X_test_scaled'] = standardize(self,Xy_data['X_train'],Xy_data['X_test'])
        
    return Xy_data, Xy_test_df


def test_csv(self,Xy_test_df,descs_model,params_df):
    """
    Separates the test databases into X and y. This allows to merge test external databases that 
    contain different columns with internal test databases coming from GENERATE
    """

    y_test_df = pd.DataFrame()
    
    try:
        X_test_df = Xy_test_df[descs_model]
    except KeyError:
        # this might fail if the initial categorical variables have not been transformed
        try:
            self.args.log.write(f"\n   x  There are missing descriptors in the test set! Looking for categorical variables converted from CURATE")
            Xy_test_df = curate.categorical_transform(self,Xy_test_df,'predict')
            X_test_df = Xy_test_df[descs_model]
            self.args.log.write(f"   o  The missing descriptors were successfully created")
        except KeyError:
            self.args.log.write(f"   x  There are still missing descriptors in the test set! The following descriptors are needed: {descs_model}")
            self.args.log.finalize()
            sys.exit()

    if params_df['y'][0] in Xy_test_df:
        y_test_df = Xy_test_df[params_df['y'][0]]

    return X_test_df, y_test_df


def plot_predictions(self, params_dict, Xy_data, path_n_suffix):
    '''
    Plot graphs of predicted vs actual values for train, validation and test sets
    '''

    set_types = ['train','valid']
    if 'y_pred_test' in Xy_data and not Xy_data['y_test'].isnull().values.any() and len(Xy_data['y_test']) > 0:
        set_types.append('test')
    
    graph_style = get_graph_style()
    
    self.args.log.write(f"\n   o  Saving graphs and CSV databases in:")
    if params_dict['type'].lower() == 'reg':
        # Plot graph with all sets
        _ = graph_reg(self,Xy_data,params_dict,set_types,path_n_suffix,graph_style)
        # Plot CV average ± SD graph of validation or test set
        _ = graph_reg(self,Xy_data,params_dict,set_types,path_n_suffix,graph_style,cv_mapie_graph=True)
        if 'y_pred_csv_test' in Xy_data and not Xy_data['y_csv_test'].isnull().values.any() and len(Xy_data['y_csv_test']) > 0:
            # Plot CV average ± SD graph of validation or test set
            _ = graph_reg(self,Xy_data,params_dict,set_types,path_n_suffix,graph_style,csv_test=True,cv_mapie_graph=True)

    elif params_dict['type'].lower() == 'clas':
        for set_type in set_types:
            _ = graph_clas(self,Xy_data,params_dict,set_type,path_n_suffix)
        if 'y_pred_csv_test' in Xy_data and not Xy_data['y_csv_test'].isnull().values.any() and len(Xy_data['y_csv_test']) > 0:
            set_type = 'csv_test'
            _ = graph_clas(self,Xy_data,params_dict,set_type,path_n_suffix,csv_test=True)

    return graph_style


def graph_reg(self,Xy_data,params_dict,set_types,path_n_suffix,graph_style,csv_test=False,print_fun=True,cv_mapie_graph=False):
    '''
    Plot regression graphs of predicted vs actual values for train, validation and test sets
    '''

    # Create graph
    sb.set(style="ticks")

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    _, ax = plt.subplots(figsize=(7.45,6))

    # Set tick sizes
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Title and labels of the axis
    plt.ylabel(f'Predicted {params_dict["y"]}', fontsize=14)
    plt.xlabel(f'{params_dict["y"]}', fontsize=14)
    
    error_bars = "valid"
    if 'y_pred_test' in Xy_data and not Xy_data['y_test'].isnull().values.any() and len(Xy_data['y_test']) > 0:
        error_bars = "test"

    title_graph = graph_title(self,csv_test,set_types,cv_mapie_graph,error_bars,Xy_data)

    if print_fun:
        plt.text(0.5, 1.08, f'{title_graph} of {os.path.basename(path_n_suffix)}', horizontalalignment='center',
            fontsize=14, fontweight='bold', transform = ax.transAxes)

    # Plot the data
    # CV graphs from VERIFY
    if 'CV' in set_types[0]:
        _ = ax.scatter(Xy_data["y_cv_valid"], Xy_data["y_pred_cv_valid"],
                    c = graph_style['color_valid'], s = graph_style['dot_size'], edgecolor = 'k', linewidths = 0.8, alpha = graph_style['alpha'], zorder=2)

    # other graphs
    elif not csv_test:
        if not cv_mapie_graph:
            _ = ax.scatter(Xy_data["y_train"], Xy_data["y_pred_train"],
                        c = graph_style['color_train'], s = graph_style['dot_size'], edgecolor = 'k', linewidths = 0.8, alpha = graph_style['alpha'], zorder=2)   
                    
        if not cv_mapie_graph or error_bars == 'valid':
            _ = ax.scatter(Xy_data["y_valid"], Xy_data["y_pred_valid"],
                        c = graph_style['color_valid'], s = graph_style['dot_size'], edgecolor = 'k', linewidths = 0.8, alpha = graph_style['alpha'], zorder=2)

        if error_bars == 'test':
            _ = ax.scatter(Xy_data["y_test"], Xy_data["y_pred_test"],
                        c = graph_style['color_test'], s = graph_style['dot_size'], edgecolor = 'k', linewidths = 0.8, alpha = graph_style['alpha'], zorder=3)

    else:
        error_bars = "test"
        _ = ax.scatter(Xy_data["y_csv_test"], Xy_data["y_pred_csv_test"],
                        c = graph_style['color_test'], s = graph_style['dot_size'], edgecolor = 'k', linewidths = 0.8, alpha = graph_style['alpha'], zorder=2)

    # average CV (MAPIE) ± SD graphs 
    if cv_mapie_graph:
        if not csv_test:   
            # Plot the data with the error bars
            _ = ax.errorbar(Xy_data[f"y_{error_bars}"], Xy_data[f"y_pred_{error_bars}"], yerr=Xy_data[f"y_pred_{error_bars}_sd"].flatten(), fmt='none', ecolor="gray", capsize=3, zorder=1)
            # Adjust labels from legend
            set_types=[error_bars,f'± SD']

        else:
            _ = ax.errorbar(Xy_data[f"y_csv_{error_bars}"], Xy_data[f"y_pred_csv_{error_bars}"], yerr=Xy_data[f"y_pred_csv_{error_bars}_sd"].flatten(), fmt='none', ecolor="gray", capsize=3, zorder=1)
            set_types=['External test',f'± SD']

    # legend and regression line with 95% CI considering all possible lines (not CI of the points)
    if 'CV' in set_types[0]: # CV in VERIFY
        if 'LOOCV' in set_types[0]:
            legend_coords = (0.835, 0.15) # LOOCV
        else:
            if len(set_types[0].split('-')[0]) == 1: # 1- to 9-fold CV
                legend_coords = (0.82, 0.15)
            elif len(set_types[0].split('-')[0]) == 2: # => 10-fold CV
                legend_coords = (0.807, 0.15)
    elif len(set_types) == 3: # train + valid + test
        legend_coords = (0.63, 0.15)
    elif len(set_types) == 2: # train + valid (or sets with ± SD)
        if 'External test' in set_types:
            legend_coords = (0.66, 0.15)
        else:
            legend_coords = (0.735, 0.15)
    ax.legend(loc='upper center', bbox_to_anchor=legend_coords,
            fancybox=True, shadow=True, ncol=5, labels=set_types, fontsize=14)

    Xy_data_df = pd.DataFrame()
    if 'CV' in set_types[0]:
        line_suff = 'cv_valid'
    elif not csv_test:
        line_suff = 'train'
    else:
        line_suff = 'csv_test'

    Xy_data_df[f"y_{line_suff}"] = Xy_data[f"y_{line_suff}"]
    Xy_data_df[f"y_pred_{line_suff}"] = Xy_data[f"y_pred_{line_suff}"]
    if len(Xy_data_df[f"y_pred_{line_suff}"]) >= 10:
        _ = sb.regplot(x=f"y_{line_suff}", y=f"y_pred_{line_suff}", data=Xy_data_df, scatter=False, color=".1", 
                        truncate = True, ax=ax, seed=params_dict['seed'])

    # set axis limits and graph PATH
    min_value_graph,max_value_graph,reg_plot_file,path_reduced = graph_vars(Xy_data,set_types,csv_test,path_n_suffix,cv_mapie_graph)

    # track the range of predictions (used in ROBERT score)
    pred_min = min(min(Xy_data["y_train"]),min(Xy_data["y_valid"]))
    pred_max = max(max(Xy_data["y_train"]),max(Xy_data["y_valid"]))
    pred_range = np.abs(pred_max-pred_min)
    Xy_data['pred_min'] = pred_min
    Xy_data['pred_max'] = pred_max
    Xy_data['pred_range'] = pred_range

    # Add gridlines
    ax.grid(linestyle='--', linewidth=1)

    # set axis limits
    plt.xlim(min_value_graph, max_value_graph)
    plt.ylim(min_value_graph, max_value_graph)

    # save graph
    plt.savefig(f'{reg_plot_file}', dpi=300, bbox_inches='tight')
    if print_fun:
        self.args.log.write(f"      -  Graph in: {path_reduced}")

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()


def graph_title(self,csv_test,set_types,cv_mapie_graph,error_bars,Xy_data):
    '''
    Retrieves the corresponding graph title.
    '''

    # set title for regular graphs
    if not cv_mapie_graph:
        # title for k-fold CV graphs
        if 'CV' in set_types[0]:
            title_graph = f'{set_types[0]} for train+valid. sets'
        elif not csv_test:
            # regular graphs
            title_graph = f'Predictions_train_valid'
            if 'test' in set_types:
                title_graph += '_test'
        else:
            title_graph = f'{os.path.basename(self.args.csv_test)}'
            if len(title_graph) > 30:
                title_graph = f'{title_graph[:27]}...'

    # set title for averaged CV ± SD graphs
    else:
        if not csv_test:
            sets_title = error_bars
        else:
            sets_title = 'external test'
        if Xy_data['cv_type'] == 'loocv':
            title_graph = f'{sets_title} set ± SD (LOOCV)'
        else:
            kfold = Xy_data['cv_type'].split('_')[-3]
            title_graph = f'{sets_title} set ± SD ({kfold}-fold CV)'

    return title_graph


def graph_vars(Xy_data,set_types,csv_test,path_n_suffix,cv_mapie_graph):
    '''
    Set axis limits for regression plots and PATH to save the graphs
    '''

    # x and y axis limits for graphs with multiple sets
    if not csv_test and 'CV' not in set_types[0]:
        size_space = 0.1*abs(min(Xy_data["y_train"])-max(Xy_data["y_train"]))
        min_value_graph = min(min(Xy_data["y_train"]),min(Xy_data["y_pred_train"]),min(Xy_data["y_valid"]),min(Xy_data["y_pred_valid"]))
        if 'test' in set_types:
            min_value_graph = min(min_value_graph,min(Xy_data["y_test"]),min(Xy_data["y_pred_test"]))
        min_value_graph = min_value_graph-size_space
            
        max_value_graph = max(max(Xy_data["y_train"]),max(Xy_data["y_pred_train"]),max(Xy_data["y_valid"]),max(Xy_data["y_pred_valid"]))
        if 'test' in set_types:
            max_value_graph = max(max_value_graph,max(Xy_data["y_test"]),max(Xy_data["y_pred_test"]))
        max_value_graph = max_value_graph+size_space

    else: # limits for graphs with only one set
        if 'CV' in set_types[0]: # for CV graphs
            set_type = 'cv_valid'
        else: # for external test sets
            set_type = 'csv_test'
        size_space = 0.1*abs(min(Xy_data[f'y_{set_type}'])-max(Xy_data[f'y_{set_type}']))
        min_value_graph = min(min(Xy_data[f'y_{set_type}']),min(Xy_data[f'y_pred_{set_type}']))
        min_value_graph = min_value_graph-size_space
        max_value_graph = max(max(Xy_data[f'y_{set_type}']),max(Xy_data[f'y_pred_{set_type}']))
        max_value_graph = max_value_graph+size_space

    # PATH of the graph
    if not csv_test:
        if 'CV' in set_types[0]:
            reg_plot_file = f'{os.path.dirname(path_n_suffix)}/CV_train_valid_predict_{os.path.basename(path_n_suffix)}.png'
        elif not cv_mapie_graph:
            reg_plot_file = f'{os.path.dirname(path_n_suffix)}/Results_{os.path.basename(path_n_suffix)}.png'
        else:
            reg_plot_file = f'{os.path.dirname(path_n_suffix)}/CV_variability_{os.path.basename(path_n_suffix)}.png'
        path_reduced = '/'.join(f'{reg_plot_file}'.replace('\\','/').split('/')[-2:])

    else:
        folder_graph = f'{os.path.dirname(path_n_suffix)}/csv_test'
        if not cv_mapie_graph:
            reg_plot_file = f'{folder_graph}/Results_{os.path.basename(path_n_suffix)}.png'
        else:
            reg_plot_file = f'{folder_graph}/CV_variability_{os.path.basename(path_n_suffix)}.png'
        path_reduced = '/'.join(f'{reg_plot_file}'.replace('\\','/').split('/')[-3:])
    
    return min_value_graph,max_value_graph,reg_plot_file,path_reduced


def graph_clas(self,Xy_data,params_dict,set_type,path_n_suffix,csv_test=False,print_fun=True):
    '''
    Plot a confusion matrix with the prediction vs actual values
    '''
    
    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    # get confusion matrix
    if 'CV' in set_type: # CV graphs
        matrix = ConfusionMatrixDisplay.from_predictions(Xy_data[f'y_cv_valid'], Xy_data[f'y_pred_cv_valid'], normalize=None, cmap='Blues') 
    else: # other graphs
        matrix = ConfusionMatrixDisplay.from_predictions(Xy_data[f'y_{set_type}'], Xy_data[f'y_pred_{set_type}'], normalize=None, cmap='Blues') 

    # transfer it to the same format and size used in reg graphs
    _, ax = plt.subplots(figsize=(7.45,6))
    matrix.plot(ax=ax, cmap='Blues')

    if print_fun:
        if 'CV' not in set_type:
            title_set = f'{set_type} set'
        else:
            title_set = set_type
        plt.text(0.5, 1.08, f'{title_set} of {os.path.basename(path_n_suffix)}', horizontalalignment='center',
            fontsize=14, fontweight='bold', transform = ax.transAxes)

    plt.xlabel(f'Predicted {params_dict["y"]}', fontsize=14)
    plt.ylabel(f'{params_dict["y"]}', fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # save fig
    if 'CV' in set_type: # CV graphs
        clas_plot_file = f'{os.path.dirname(path_n_suffix)}/CV_train_valid_predict_{os.path.basename(path_n_suffix)}.png'
        path_reduced = '/'.join(f'{clas_plot_file}'.replace('\\','/').split('/')[-2:])

    elif not csv_test:
        clas_plot_file = f'{os.path.dirname(path_n_suffix)}/Results_{os.path.basename(path_n_suffix)}_{set_type}.png'
        path_reduced = '/'.join(f'{clas_plot_file}'.replace('\\','/').split('/')[-2:])

    else:
        folder_graph = f'{os.path.dirname(path_n_suffix)}/csv_test'
        clas_plot_file = f'{folder_graph}/Results_{os.path.basename(path_n_suffix)}_{set_type}.png'
        path_reduced = '/'.join(f'{clas_plot_file}'.replace('\\','/').split('/')[-3:])

    plt.savefig(f'{clas_plot_file}', dpi=300, bbox_inches='tight')

    if print_fun:
        self.args.log.write(f"      -  Graph in: {path_reduced}")

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()


def save_predictions(self,Xy_data,params_dir,Xy_test_df,params_dict):
    '''
    Saves CSV files with the different sets and their predicted results
    '''

    Xy_orig_df, Xy_path, params_df, _, _, suffix_title = load_dfs(self,params_dir,'no_print')
    base_csv_name = '_'.join(os.path.basename(Path(Xy_path)).replace('.csv','_').split('_')[0:2])
    base_csv_name = f'PREDICT/{base_csv_name}'
    base_csv_path = f"{Path(os.getcwd()).joinpath(base_csv_name)}"
    Xy_orig_train = Xy_orig_df[Xy_orig_df.Set == 'Training']
    Xy_orig_train[f'{params_df["y"][0]}_pred'] = Xy_data['y_pred_train']
    train_path = f'{base_csv_path}_train_{suffix_title}.csv'
    _ = Xy_orig_train.to_csv(train_path, index = None, header=True)
    print_preds = f'      -  Train set with predicted results: PREDICT/{os.path.basename(train_path)}'
    Xy_orig_valid = Xy_orig_df[Xy_orig_df.Set == 'Validation']
    Xy_orig_valid[f'{params_df["y"][0]}_pred'] = Xy_data['y_pred_valid']
    # Search in the csv file for model type to avoid problems when using only the predict module with a classification model (reg model is the default)
    if params_df['type'].values[0] == 'reg' and 'y_pred_valid_sd' in Xy_data:
        Xy_orig_valid[f'{params_df["y"][0]}_pred_sd'] = Xy_data['y_pred_valid_sd']
    valid_path = f'{base_csv_path}_valid_{suffix_title}.csv'
    _ = Xy_orig_valid.to_csv(valid_path, index = None, header=True)
    print_preds += f'\n      -  Validation set with predicted results: PREDICT/{os.path.basename(valid_path)}'
    Xy_data['csv_pred_name'] = os.path.basename(valid_path)
    # saves test predictions
    Xy_orig_test = None
    if 'X_test_scaled' in Xy_data:
        Xy_orig_test = Xy_orig_df[Xy_orig_df.Set == 'Test']
        Xy_orig_test[f'{params_df["y"][0]}_pred'] = Xy_data['y_pred_test']
        if params_df['type'].values[0] == 'reg' and 'y_pred_test_sd' in Xy_data:
            Xy_orig_test[f'{params_df["y"][0]}_pred_sd'] = Xy_data['y_pred_test_sd']
        test_path = f'{base_csv_path}_test_{suffix_title}.csv'
        _ = Xy_orig_test.to_csv(test_path, index = None, header=True)
        print_preds += f'\n      -  Test set with predicted results: PREDICT/{os.path.basename(test_path)}'
        Xy_data['csv_pred_name'] = os.path.basename(test_path)
        
    # saves prediction for external test in --csv_test
    if self.args.csv_test != '':
        Xy_test_df[f'{params_df["y"][0]}_pred'] = Xy_data['y_pred_csv_test']
        if params_df['type'].values[0] == 'reg':
            Xy_test_df[f'{params_df["y"][0]}_pred_sd'] = Xy_data['y_pred_csv_test_sd']
        folder_csv = f'{os.path.dirname(base_csv_path)}/csv_test'
        Path(folder_csv).mkdir(exist_ok=True, parents=True)
        csv_name = f'{os.path.basename(self.args.csv_test)}'.split(".csv")[0]
        csv_name += f'_predicted_{suffix_title}.csv'
        csv_test_path = f'{folder_csv}/{csv_name}'
        _ = Xy_test_df.to_csv(csv_test_path, index = None, header=True)
        print_preds += f'\n      -  External set with predicted results: PREDICT/csv_test/{os.path.basename(csv_test_path)}'
        Xy_data['csv_pred_name'] = f'csv_test/{os.path.basename(csv_test_path)}'

    self.args.log.write(print_preds)

    path_n_suffix = f'{base_csv_path}_{suffix_title}'

    # store the names of the datapoints
    name_points = {}
    if params_dict['names'] != '':
        if params_dict['names'].lower() in Xy_orig_train: # accounts for upper/lowercase mismatches
            params_dict['names'] = params_dict['names'].lower()
        if params_dict['names'].upper() in Xy_orig_train:
            params_dict['names'] = params_dict['names'].upper()
        if params_dict['names'] in Xy_orig_train:
            name_points['train'] = Xy_orig_train[params_dict['names']]
            name_points['valid'] = Xy_orig_valid[params_dict['names']]
        if Xy_orig_test is not None:
            name_points['test'] = Xy_orig_test[params_dict['names']]

    return path_n_suffix, name_points, Xy_data


def print_predict(self,Xy_data,params_dict,path_n_suffix,loaded_model):
    '''
    Prints results of the predictions for all the sets
    '''
    
    dat_file = f'{os.path.dirname(path_n_suffix)}/Results_{os.path.basename(path_n_suffix)}.dat'
    path_reduced = '/'.join(f'{dat_file}'.replace('\\','/').split('/')[-2:])
    print_results = f"\n   o  Results saved in {path_reduced}:"
    set_print = 'Train:Validation'

    # get number of points and proportions
    n_train = len(Xy_data['X_train'])
    n_valid = len(Xy_data['X_valid'])
    n_test = 0
    n_points = f'{n_train}:{n_valid}'
    if 'X_test' in Xy_data and len(Xy_data['X_test']) > 0:
        set_print += ':Test'
        n_test = len(Xy_data['X_test'])
        n_points += f':{n_test}'
    total_points = n_train + n_valid + n_test
    print_results += f"\n      -  Points {set_print} = {n_points}"

    prop_train = round(n_train*100/total_points)
    prop_valid = round(n_valid*100/total_points)
    prop_test = round(n_test*100/total_points)
    prop_print = f'{prop_train}:{prop_valid}'
    if 'X_test' in Xy_data and len(Xy_data['X_test']) > 0:
        prop_print += f':{prop_test}'
    print_results += f"\n      -  Proportion {set_print} = {prop_print}"
    
    n_descps = len(Xy_data['X_train'].keys())
    print_results += f"\n      -  Number of descriptors = {n_descps}"
    print_results += f"\n      -  Proportion (train+valid.) points:descriptors = {n_train+n_valid}:{n_descps}"

    # print results and save dat file
    if params_dict['type'].lower() == 'reg':
        print_results += f"\n      -  Train : R2 = {Xy_data['r2_train']:.2}, MAE = {Xy_data['mae_train']:.2}, RMSE = {Xy_data['rmse_train']:.2}"
        print_results += f"\n      -  Valid. : R2 = {Xy_data['r2_valid']:.2}, MAE = {Xy_data['mae_valid']:.2}, RMSE = {Xy_data['rmse_valid']:.2}"
        if 'y_pred_test' in Xy_data and not Xy_data['y_test'].isnull().values.any() and len(Xy_data['y_test']) > 0:
            print_results += f"\n      -  Test : R2 = {Xy_data['r2_test']:.2}, MAE = {Xy_data['mae_test']:.2}, RMSE = {Xy_data['rmse_test']:.2}"
        if 'y_pred_csv_test' in Xy_data and not Xy_data['y_csv_test'].isnull().values.any() and len(Xy_data['y_csv_test']) > 0:
            print_results += f"\n      -  csv_test : R2 = {Xy_data['r2_csv_test']:.2}, MAE = {Xy_data['mae_csv_test']:.2}, RMSE = {Xy_data['rmse_csv_test']:.2}"
        # add equation for linear models
        if params_dict['model'].upper() == 'MVL' or self.args.evaluate == 'True':
            desc_mvl = ast.literal_eval(params_dict['X_descriptors'])
            print_results += f"\n\n   o  Linear model equation, with coefficients obtained using standardized data (coefficient values/importances can be compared):"
            print_results += f"\n      - {params_dict['y']} = {loaded_model.intercept_:.2} "
            for i, coeff in enumerate(loaded_model.coef_):
                if float(coeff) >= 0:
                    print_results += f"+ ({coeff:.2} * {desc_mvl[i]}) "
                else:
                    print_results += f"- ({np.abs(coeff):.2} * {desc_mvl[i]}) "

    elif params_dict['type'].lower() == 'clas':
        print_results += f"\n      -  Train : Accuracy = {Xy_data['acc_train']:.2}, F1 score = {Xy_data['f1_train']:.2}, MCC = {Xy_data['mcc_train']:.2}"
        print_results += f"\n      -  Valid. : Accuracy = {Xy_data['acc_valid']:.2}, F1 score = {Xy_data['f1_valid']:.2}, MCC = {Xy_data['mcc_valid']:.2}"
        if 'y_pred_test' in Xy_data and not Xy_data['y_test'].isnull().values.any() and len(Xy_data['y_test']) > 0:
            print_results += f"\n      -  Test : Accuracy = {Xy_data['acc_test']:.2}, F1 score = {Xy_data['f1_test']:.2}, MCC = {Xy_data['mcc_test']:.2}"
        if 'y_pred_csv_test' in Xy_data and not Xy_data['y_csv_test'].isnull().values.any() and len(Xy_data['y_csv_test']) > 0:
            print_results += f"\n      -  csv_test : Accur. = {Xy_data['acc_csv_test']:.2}, F1 score = {Xy_data['f1_csv_test']:.2}, MCC = {Xy_data['mcc_csv_test']:.2}"

    self.args.log.write(print_results)


def print_cv_var(self,Xy_data,params_dict,path_n_suffix):
    '''
    Prints results of the predictions for all the sets
    '''

    shap_plot_file = f'{os.path.dirname(path_n_suffix)}/CV_variability_{os.path.basename(path_n_suffix)}.png'
    path_reduced = '/'.join(f'{shap_plot_file}'.replace('\\','/').split('/')[-2:])
    if Xy_data['cv_type'] == 'loocv':
        cv_type = f'LOOCV'
    else:
        kfold = Xy_data['cv_type'].split('_')[-3]
        cv_type = f'{kfold}-fold CV'

    print_cv_var = f"\n   o  Cross-validation variation (with {cv_type}) graph saved in {path_reduced}:"
    print_cv_var += f"\n      -  Standard deviations saved in PREDICT/{Xy_data['csv_pred_name']} in the {params_dict['y']}_pred_sd column"
    print_cv_var += f"\n      -  Average SD = {round(Xy_data['avg_sd'],2)}"
    print_cv_var += f"\n      -  y range of dataset (train+valid.) = {round(Xy_data['pred_min'],2)} to {round(Xy_data['pred_max'],2)}, total {round(Xy_data['pred_range'],2)}"

    self.args.log.write(print_cv_var)


def shap_analysis(self,Xy_data,params_dict,path_n_suffix):
    '''
    Plots and prints the results of the SHAP analysis
    '''

    shap_plot_file = f'{os.path.dirname(path_n_suffix)}/SHAP_{os.path.basename(path_n_suffix)}.png'

    # load and fit the ML model
    loaded_model = load_model(params_dict)
    loaded_model.fit(Xy_data['X_train_scaled'], Xy_data['y_train']) 

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    # run the SHAP analysis and save the plot
    explainer = shap.Explainer(loaded_model.predict, Xy_data['X_valid_scaled'], seed=params_dict['seed'])
    try:
        shap_values = explainer(Xy_data['X_valid_scaled'])
    except ValueError:
        shap_values = explainer(Xy_data['X_valid_scaled'],max_evals=(2*len(Xy_data['X_valid_scaled'].columns))+1)

    shap_show = [self.args.shap_show,len(Xy_data['X_valid_scaled'].columns)]
    aspect_shap = 25+((min(shap_show)-2)*5)
    height_shap = 1.2+min(shap_show)/4

    # explainer = shap.TreeExplainer(loaded_model) # in case the standard version doesn't work
    _ = shap.summary_plot(shap_values, Xy_data['X_valid_scaled'], max_display=self.args.shap_show,show=False, plot_size=[7.45,height_shap])

    # set title
    plt.title(f'SHAP analysis of {os.path.basename(path_n_suffix)}', fontsize = 14, fontweight="bold")

    # adjust width of the colorbar
    plt.gcf().axes[-1].set_aspect(aspect_shap)
    plt.gcf().axes[-1].set_box_aspect(aspect_shap)
    
    plt.savefig(f'{shap_plot_file}', dpi=300, bbox_inches='tight')

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    path_reduced = '/'.join(f'{shap_plot_file}'.replace('\\','/').split('/')[-2:])
    print_shap = f"\n   o  SHAP plot saved in {path_reduced}"

    # collect SHAP values and print
    desc_list, min_list, max_list = [],[],[]
    for i,desc in enumerate(Xy_data['X_train_scaled']):
        desc_list.append(desc)
        val_list_indiv= []
        for _,val in enumerate(shap_values.values):
            val_list_indiv.append(val[i])
        min_indiv = min(val_list_indiv)
        max_indiv = max(val_list_indiv)
        min_list.append(min_indiv)
        max_list.append(max_indiv)
    
    if max(max_list, key=abs) > max(min_list, key=abs):
        max_list, min_list, desc_list = (list(t) for t in zip(*sorted(zip(max_list, min_list, desc_list), reverse=True)))
    else:
        min_list, max_list, desc_list = (list(t) for t in zip(*sorted(zip(min_list, max_list, desc_list), reverse=False)))

    for i,desc in enumerate(desc_list):
        print_shap += f"\n      -  {desc} = min: {min_list[i]:.2}, max: {max_list[i]:.2}"

    self.args.log.write(print_shap)


def PFI_plot(self,Xy_data,params_dict,path_n_suffix):
    '''
    Plots and prints the results of the PFI analysis
    '''

    pfi_plot_file = f'{os.path.dirname(path_n_suffix)}/PFI_{os.path.basename(path_n_suffix)}.png'

    # load and fit the ML model
    loaded_model = load_model(params_dict)
    loaded_model.fit(Xy_data['X_train_scaled'], Xy_data['y_train']) 

    score_model = loaded_model.score(Xy_data['X_valid_scaled'], Xy_data['y_valid'])
    error_type = params_dict['error_type'].lower()
    
    # select scoring function for PFI analysis based on the error type
    if params_dict['type'].lower() == 'reg':
        scoring = {
            'rmse': 'neg_root_mean_squared_error',
            'mae': 'neg_median_absolute_error',
            'r2': 'r2'
        }.get(error_type)
    else:
        scoring = {
            'mcc': make_scorer(matthews_corrcoef),
            'f1': 'f1',
            'acc': 'accuracy'
        }.get(error_type)

    perm_importance = permutation_importance(loaded_model, Xy_data['X_valid_scaled'], Xy_data['y_valid'], scoring=scoring, n_repeats=self.args.pfi_epochs, random_state=params_dict['seed'])

    # sort descriptors and results from PFI
    desc_list, PFI_values, PFI_sd = [],[],[]
    for i,desc in enumerate(Xy_data['X_train_scaled']):
        desc_list.append(desc)
        PFI_values.append(perm_importance.importances_mean[i])
        PFI_sd.append(perm_importance.importances_std[i])

    # sort from higher to lower values and keep only the top self.args.pfi_show descriptors
    PFI_values, PFI_sd, desc_list = (list(t) for t in zip(*sorted(zip(PFI_values, PFI_sd, desc_list), reverse=True)))
    PFI_values_plot = PFI_values[:self.args.pfi_show][::-1]
    desc_list_plot = desc_list[:self.args.pfi_show][::-1]

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    # plot and print results
    _, ax = plt.subplots(figsize=(7.45,6))
    y_ticks = np.arange(0, len(desc_list_plot))
    ax.barh(desc_list_plot, PFI_values_plot)
    ax.set_yticks(y_ticks,labels=desc_list_plot,fontsize=14)
    plt.text(0.5, 1.08, f'Permutation feature importances (PFIs) of {os.path.basename(path_n_suffix)}', horizontalalignment='center',
        fontsize=14, fontweight='bold', transform = ax.transAxes)
    ax.set(ylabel=None, xlabel='PFI')

    plt.savefig(f'{pfi_plot_file}', dpi=300, bbox_inches='tight')

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    path_reduced = '/'.join(f'{pfi_plot_file}'.replace('\\','/').split('/')[-2:])
    print_PFI = f"\n   o  PFI plot saved in {path_reduced}"

    if params_dict['type'].lower() == 'reg':
        print_PFI += f'\n      Original score (from model.score, R2) = {score_model:.2}'
    elif params_dict['type'].lower() == 'clas':
        print_PFI += f'\n      Original score (from model.score, MCC) = {score_model:.2}'

    for i,desc in enumerate(desc_list):
        print_PFI += f"\n      -  {desc} = {PFI_values[i]:.2} ± {PFI_sd[i]:.2}"
    
    self.args.log.write(print_PFI)


def outlier_plot(self,Xy_data,path_n_suffix,name_points,graph_style):
    '''
    Plots and prints the results of the outlier analysis
    '''

    # detect outliers
    outliers_data, print_outliers = outlier_filter(self, Xy_data, name_points)

    # plot data in SD units
    sb.set(style="ticks")
    
    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    _, ax = plt.subplots(figsize=(7.45,6))
    plt.text(0.5, 1.08, f'Outlier analysis of {os.path.basename(path_n_suffix)}', horizontalalignment='center',
    fontsize=14, fontweight='bold', transform = ax.transAxes)

    plt.grid(linestyle='--', linewidth=1)
    _ = ax.scatter(outliers_data['train_scaled'], outliers_data['train_scaled'],
            c = graph_style['color_train'], s = graph_style['dot_size'], edgecolor = 'k', linewidths = 0.8, alpha = graph_style['alpha'], zorder=2)
    _ = ax.scatter(outliers_data['valid_scaled'], outliers_data['valid_scaled'],
            c = graph_style['color_valid'], s = graph_style['dot_size'], edgecolor = 'k', linewidths = 0.8, alpha = graph_style['alpha'], zorder=2)
    if 'test_scaled' in outliers_data:
        _ = ax.scatter(outliers_data['test_scaled'], outliers_data['test_scaled'],
            c = graph_style['color_test'], s = graph_style['dot_size'], edgecolor = 'k', linewidths = 0.8, alpha = graph_style['alpha'], zorder=2)
    
    # Set styling preferences and graph limits
    plt.xlabel('SD of the errors',fontsize=14)
    plt.xticks(fontsize=14)
    plt.ylabel('SD of the errors',fontsize=14)
    plt.yticks(fontsize=14)
    
    axis_limit = max(outliers_data['train_scaled'], key=abs)
    if max(outliers_data['valid_scaled'], key=abs) > axis_limit:
        axis_limit = max(outliers_data['valid_scaled'], key=abs)
    if 'test_scaled' in outliers_data:
        if max(outliers_data['test_scaled'], key=abs) > axis_limit:
            axis_limit = max(outliers_data['test_scaled'], key=abs)
    axis_limit = axis_limit+0.5
    if axis_limit < 2.5: # this fixes a problem when representing rectangles in graphs with low SDs
        axis_limit = 2.5
    plt.ylim(-axis_limit, axis_limit)
    plt.xlim(-axis_limit, axis_limit)

    # plot rectangles in corners
    diff_tvalue = axis_limit - self.args.t_value
    Rectangle_top = mpatches.Rectangle(xy=(axis_limit, axis_limit), width=-diff_tvalue, height=-diff_tvalue, facecolor='grey', alpha=0.3)
    Rectangle_bottom = mpatches.Rectangle(xy=(-(axis_limit), -(axis_limit)), width=diff_tvalue, height=diff_tvalue, facecolor='grey', alpha=0.3)
    ax.add_patch(Rectangle_top)
    ax.add_patch(Rectangle_bottom)

    # save plot and print results
    outliers_plot_file = f'{os.path.dirname(path_n_suffix)}/Outliers_{os.path.basename(path_n_suffix)}.png'
    plt.savefig(f'{outliers_plot_file}', dpi=300, bbox_inches='tight')

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()
    
    path_reduced = '/'.join(f'{outliers_plot_file}'.replace('\\','/').split('/')[-2:])
    print_outliers += f"\n   o  Outliers plot saved in {path_reduced}"

    if 'train' not in name_points:
        print_outliers += f'\n      x  No names option (or var missing in CSV file)! Outlier names will not be shown'
    else:
        if 'test_scaled' in outliers_data and 'test' not in name_points:
            print_outliers += f'\n      x  No names option (or var missing in CSV file in the test file)! Outlier names will not be shown'

    print_outliers = outlier_analysis(print_outliers,outliers_data,'train')
    print_outliers = outlier_analysis(print_outliers,outliers_data,'valid')
    if 'test_scaled' in outliers_data:
        print_outliers = outlier_analysis(print_outliers,outliers_data,'test')
    
    self.args.log.write(print_outliers)


def outlier_analysis(print_outliers,outliers_data,outliers_set):
    '''
    Analyzes the outlier results
    '''
    
    if outliers_set == 'train':
        label_set = 'Train'
        outliers_label = 'outliers_train'
        n_points_label = 'train_scaled'
        outliers_name = 'names_train'
    elif outliers_set == 'valid':
        label_set = 'Validation'
        outliers_label = 'outliers_valid'
        n_points_label = 'valid_scaled'
        outliers_name = 'names_valid'
    elif outliers_set == 'test':
        label_set = 'Test'
        outliers_label = 'outliers_test'
        n_points_label = 'test_scaled'
        outliers_name = 'names_test'

    per_cent = (len(outliers_data[outliers_label])/len(outliers_data[n_points_label]))*100
    print_outliers += f"\n      {label_set}: {len(outliers_data[outliers_label])} outliers out of {len(outliers_data[n_points_label])} datapoints ({per_cent:.1f}%)"
    for val,name in zip(outliers_data[outliers_label], outliers_data[outliers_name]):
        print_outliers += f"\n      -  {name} ({val:.2} SDs)"
    return print_outliers

def outlier_filter(self, Xy_data, name_points):
    '''
    Calculates and stores absolute errors in SD units for all the sets
    '''
    
    # calculate absolute errors between predicted y and actual values
    outliers_train = [abs(x-y) for x,y in zip(Xy_data['y_train'],Xy_data['y_pred_train'])]
    outliers_valid = [abs(x-y) for x,y in zip(Xy_data['y_valid'],Xy_data['y_pred_valid'])]
    if 'y_pred_test' in Xy_data and not Xy_data['y_test'].isnull().values.any() and len(Xy_data['y_test']) > 0:
        outliers_test = [abs(x-y) for x,y in zip(Xy_data['y_test'],Xy_data['y_pred_test'])]

    # the errors are scaled using standard deviation units. When the absolute
    # error is larger than the t-value, the point is considered an outlier. All the sets
    # use the mean and SD of the train set
    outliers_mean = np.mean(outliers_train)
    outliers_sd = np.std(outliers_train)

    outliers_data = {}
    outliers_data['train_scaled'] = (outliers_train-outliers_mean)/outliers_sd
    outliers_data['valid_scaled'] = (outliers_valid-outliers_mean)/outliers_sd
    if 'y_pred_test' in Xy_data and not Xy_data['y_test'].isnull().values.any() and len(Xy_data['y_test']) > 0:
        outliers_data['test_scaled'] = (outliers_test-outliers_mean)/outliers_sd

    print_outliers, naming, naming_test = '', False, False
    if 'train' in name_points:
        naming = True
        if 'test' in name_points:
            naming_test = True

    outliers_data['outliers_train'], outliers_data['names_train'] = detect_outliers(self, outliers_data['train_scaled'], name_points, naming, 'train')
    outliers_data['outliers_valid'], outliers_data['names_valid'] = detect_outliers(self, outliers_data['valid_scaled'], name_points, naming, 'valid')
    if 'y_pred_test' in Xy_data and not Xy_data['y_test'].isnull().values.any() and len(Xy_data['y_test']) > 0:
        outliers_data['outliers_test'], outliers_data['names_test'] = detect_outliers(self, outliers_data['test_scaled'], name_points, naming_test, 'test')
    
    return outliers_data, print_outliers


def detect_outliers(self, outliers_scaled, name_points, naming_detect, set_type):
    '''
    Detects and store outliers with their corresponding datapoint names
    '''

    val_outliers = []
    name_outliers = []
    if naming_detect:
        name_points_list = name_points[set_type].to_list()
    for i,val in enumerate(outliers_scaled):
        if val > self.args.t_value or val < -self.args.t_value:
            val_outliers.append(val)
            if naming_detect:
                name_outliers.append(name_points_list[i])

    return val_outliers, name_outliers


def distribution_plot(self,Xy_data,path_n_suffix,params_dict):
    '''
    Plots histogram (reg) or bin plot (clas).
    '''

    # make graph
    sb.set(style="ticks")

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    _, ax = plt.subplots(figsize=(7.45,6))
    plt.text(0.5, 1.08, f'y-values distribution (train+valid.) of {os.path.basename(path_n_suffix)}', horizontalalignment='center',
    fontsize=14, fontweight='bold', transform = ax.transAxes)

    plt.grid(linestyle='--', linewidth=1)

    # combine train and validation sets
    y_combined = pd.concat([Xy_data['y_train'],Xy_data['y_valid']], axis=0).reset_index(drop=True)

    # plot histogram, quartile lines and the points in each quartile
    if params_dict['type'].lower() == 'reg':
        y_dist_dict,ax = plot_quartiles(y_combined,ax)
    
    # plot a bar plot with the count of each y type
    elif params_dict['type'].lower() == 'clas':
        y_dist_dict,ax = plot_y_count(y_combined,ax)

    # set styling preferences and graph limits
    plt.xlabel(f'{params_dict["y"]} values',fontsize=14)
    plt.xticks(fontsize=14)
    plt.ylabel('Frequency',fontsize=14)
    plt.yticks(fontsize=14)

    # set limits
    if params_dict['type'].lower() == 'reg':
        border_y_range = 0.1*np.abs(max(y_combined)-min(y_combined))
        plt.xlim(min(y_combined)-border_y_range, max(y_combined)+border_y_range)

    # save plot and print results
    orig_distrib_file = f'y_distribution_{os.path.basename(path_n_suffix)}.png'
    plt.savefig(f'{orig_distrib_file}', dpi=300, bbox_inches='tight')
    # for a VERY weird reason, I need to save the figure in the working directory and then move it into PREDICT
    final_distrib_file = f'{os.path.dirname(path_n_suffix)}/y_distribution_{os.path.basename(path_n_suffix)}.png'
    shutil.move(orig_distrib_file, final_distrib_file)

    # clean all the information and style from previous plots
    plt.gcf()
    plt.cla()
    plt.close()

    path_reduced = '/'.join(f'{final_distrib_file}'.replace('\\','/').split('/')[-2:])
    print_distrib = f"\n   o  y-values distribution plot saved in {path_reduced}"

    # print the quartile results
    if params_dict['type'].lower() == 'reg':
        print_distrib += f"\n      Ideally, the number of datapoints in the four quartiles of the y-range should be uniform (25% population in each quartile) to have similar confidence intervals in the predictions across the y-range"
        quartile_pops = [len(y_dist_dict['q1_points']),len(y_dist_dict['q2_points']),len(y_dist_dict['q3_points']),len(y_dist_dict['q4_points'])]
        print_distrib += f"\n      -  The number of points in each quartile is Q1: {quartile_pops[0]}, Q2: {quartile_pops[1]}, Q3: {quartile_pops[2]}, Q4: {quartile_pops[3]}"
        quartile_min_idx = quartile_pops.index(min(quartile_pops))
        quartile_max_idx = quartile_pops.index(max(quartile_pops))
        if 4*min(quartile_pops) < max(quartile_pops):
            print_distrib += f"\n      x  WARNING! Your data is not uniform (Q{quartile_min_idx+1} has {min(quartile_pops)} points while Q{quartile_max_idx+1} has {max(quartile_pops)})"
        elif 2*min(quartile_pops) < max(quartile_pops):
            print_distrib += f"\n      x  WARNING! Your data is slightly not uniform (Q{quartile_min_idx+1} has {min(quartile_pops)} points while Q{quartile_max_idx+1} has {max(quartile_pops)})"
        else:
            print_distrib += f"\n      o  Your data seems quite uniform"

    elif params_dict['type'].lower() == 'clas':
        if len(y_dist_dict['count_labels']) > 2:
            self.args.log.write(f"\n      ADAPT THIS PART for 3+ prediction classes!!")
            sys.exit()
        print_distrib += f"\n      Ideally, the number of datapoints in each prediction class should be uniform (50% population per class) to have similar reliability in the predictions across classes"
        distrib_counts = [y_dist_dict['count_labels'][0],y_dist_dict['count_labels'][1]]
        print_distrib += f"\n      - The number of points in each class is {y_dist_dict['type_labels'][0]}: {y_dist_dict['count_labels'][0]}, {y_dist_dict['type_labels'][1]}: {y_dist_dict['count_labels'][1]}"
        class_min_idx = distrib_counts.index(min(distrib_counts))
        class_max_idx = distrib_counts.index(max(distrib_counts))
        if 3*min(distrib_counts) < max(distrib_counts):
            print_distrib += f"\n      x  WARNING! Your data is not uniform (class {y_dist_dict['type_labels'][class_min_idx]} has {min(distrib_counts)} points while class {y_dist_dict['type_labels'][class_max_idx]} has {max(distrib_counts)})"
        elif 1.5*min(distrib_counts) < max(distrib_counts):
            print_distrib += f"\n      x  WARNING! Your data is slightly not uniform (class {y_dist_dict['type_labels'][class_min_idx]} has {min(distrib_counts)} points while class {y_dist_dict['type_labels'][class_max_idx]} has {max(distrib_counts)})"
        else:
            print_distrib += f"\n      o  Your data seems quite uniform"

    self.args.log.write(print_distrib)


def plot_quartiles(y_combined,ax):
    '''
    Plot histogram, quartile lines and the points in each quartile.
    '''

    bins = max([round(len(y_combined)/5),5]) # at least 5 bins until 25 points
    # histogram
    y_hist, _, _ = ax.hist(y_combined, bins=bins,
                color='#1f77b4', edgecolor='k', linewidth=1, alpha=1)

    # uniformity lines to plot
    separation_range = np.abs(max(y_combined)-min(y_combined))/4
    quart_dict = {'line_1': min(y_combined),
                    'line_2': min(y_combined) + separation_range,
                    'line_3': min(y_combined) + (2*separation_range),
                    'line_4': min(y_combined) + (3*separation_range),
                    'line_5': max(y_combined)}

    lines_plot = [quart_dict[line] for line in quart_dict]
    ax.vlines([lines_plot], ymin=max(y_hist)*1.05, ymax=max(y_hist)*1.3, colors='crimson', linestyles='--')

    # points in each quartile
    quart_dict['q1_points'] = []
    quart_dict['q2_points'] = []
    quart_dict['q3_points'] = []
    quart_dict['q4_points'] = []

    for val in y_combined:
        if val < quart_dict['line_2']:
            quart_dict['q1_points'].append(val)
        elif quart_dict['line_2'] < val < quart_dict['line_3']:
            quart_dict['q2_points'].append(val)
        elif quart_dict['line_3'] < val < quart_dict['line_4']:
            quart_dict['q3_points'].append(val)
        elif val >= quart_dict['line_4']:
            quart_dict['q4_points'].append(val)

    x_quart = 0.185
    for quart in quart_dict:
        if 'points' in quart:
            plt.text(x_quart, 0.845, f'Q{quart[1]}\n{len(quart_dict[quart])} points', horizontalalignment='center',
                    fontsize=12, transform = ax.transAxes, backgroundcolor='w')
            x_quart += 0.209

    return quart_dict,ax


def plot_y_count(y_combined,ax):
    '''
    Plot a bar plot with the count of each y type.
    '''

    # get the number of times that each y type is included
    labels_used = set(y_combined)
    type_labels,count_labels = [],[]
    for label in labels_used:
        type_labels.append(label)
        count_labels.append(len(y_combined[y_combined == label]))

    _ = ax.bar(type_labels, count_labels, tick_label=type_labels,
                color='#1f77b4', edgecolor='k', linewidth=1, alpha=1,
                width=0.4)

    y_dist_dict = {'type_labels': type_labels,
                   'count_labels': count_labels}

    return y_dist_dict,ax


def pearson_map_predict(self,Xy_data,params_dir):
    '''
    Plots the Pearson map and analyzes correlation of descriptors.
    '''

    X_combined = pd.concat([Xy_data['X_train'],Xy_data['X_valid']], axis=0).reset_index(drop=True)
    corr_matrix = pearson_map(self,X_combined,'predict',params_dir=params_dir)

    corr_dict = {'descp_1': [],
                 'descp_2': [],
                 'r': []
    }
    for i,descp in enumerate(corr_matrix.columns):
        for j,val in enumerate(corr_matrix[descp]):
            if i < j and np.abs(val) > 0.8:
                corr_dict['descp_1'].append(corr_matrix.columns[i])
                corr_dict['descp_2'].append(corr_matrix.columns[j])
                corr_dict['r'].append(val)

    print_corr = f'      Ideally, variables should show low correlations.' # no initial \n, it's a new log.write
    if len(corr_dict['descp_1']) == 0:
        print_corr += f"\n      o  Correlations between variables are acceptable"
    else:
        abs_r_list = list(np.abs(corr_dict['r']))
        abs_max_r = max(abs_r_list)
        max_r = corr_dict['r'][abs_r_list.index(abs_max_r)]
        max_descp_1 = corr_dict['descp_1'][abs_r_list.index(abs_max_r)]
        max_descp_2 = corr_dict['descp_2'][abs_r_list.index(abs_max_r)]
        if abs_max_r > 0.84:
            print_corr += f"\n      x  WARNING! High correlations observed (up to r = {round(max_r,2)} or R2 = {round(max_r*max_r,2)}, for {max_descp_1} and {max_descp_2})"
        elif abs_max_r > 0.71:
            print_corr += f"\n      x  WARNING! Noticeable correlations observed (up to r = {round(max_r,2)} or R2 = {round(max_r*max_r,2)}, for {max_descp_1} and {max_descp_2})"

    self.args.log.write(print_corr)
