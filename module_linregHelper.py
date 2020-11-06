from module_scraper import *
from module_numericFinancialData import * 
from import_my_packages import * 
from module_featurizer import *

from sklearn.metrics import silhouette_samples
import matplotlib.cm as cm
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer
from pyclustering.utils import read_sample
from pyclustering.samples.definitions import FCPS_SAMPLES
from sklearn.metrics import silhouette_samples, silhouette_score
from scipy import spatial
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor 

##################### PLOT SETTINGS #####################
font_dict = {'size' : 40, 'family': 'serif'}
font_dict_legend = {'size' : 20, 'family': 'serif'}
tick_size = 30
###################################################################

def mape(target, fit):
    # target = target['TARGET'].tolist()
    target = target.tolist()

    fit = list(fit)
    x = statistics.mean([100 * (abs(target[i] - fit[i])/target[i]) for i in range(len(target))])
    x = round(x, 5)
    return(x) # returns MAPE as a PERCENT



def vif(df):
    vif_data = pd.DataFrame() 
    vif_data["feature"] = df.columns 
    vif_data["VIF"] = [variance_inflation_factor(df.values, i) for i in range(len(df.columns))] 
    return(vif_data)


def correlation_plot(X, text_extention, home_directory):
    corr = X.corr(method='pearson') 
    fig, ax = plt.subplots(figsize=(30,30))
    sns.heatmap(corr, annot=True, xticklabels=corr.columns, 
            yticklabels=corr.columns, ax=ax, linewidths=.5, 
            vmin = -1, vmax=1, center=0, square = False)
    plt.title('Correlation HeatMap for ALL DATA')
    fig.savefig(home_directory + "/LinReg_Results/Figures/Correlation_Test_" + text_extention + ".jpg", bbox_inches="tight")

def linreg_Plots(true_y, fitted_y, residuals, text_extension, home_directory):
    fig = plt.figure(figsize = (20,12))
    plt.scatter(fitted_y, residuals, s = 100)
    plt.title("Residuals vs. Fit - " + text_extension, fontdict = font_dict)
    plt.xlabel("Fitted Values", fontdict = font_dict)
    plt.ylabel("Residuals", fontdict = font_dict)
    plt.xticks(fontsize = tick_size, fontname = font_dict['family'])
    plt.yticks(fontsize = tick_size, fontname = font_dict['family'])
    plt.axhline(y=0,color='gray',linestyle='--', linewidth = 3)
    fig.savefig(home_directory + "/LinReg_Results/Figures/Linear_Regression_Numeric_" + text_extension + "_Residuals_vs_Fitted.jpg", bbox_inches="tight")



    fig = plt.figure(figsize = (20,12))
    plt.scatter(true_y, residuals, s = 100)
    plt.title("Residuals vs. Target - " + text_extension, fontdict = font_dict)
    plt.xlabel("Target Values", fontdict = font_dict)
    plt.ylabel("Residuals", fontdict = font_dict)
    plt.xticks(fontsize = tick_size, fontname = font_dict['family'])
    plt.yticks(fontsize = tick_size, fontname = font_dict['family'])
    plt.axhline(y=0,color='gray',linestyle='--', linewidth = 3)
    fig.savefig(home_directory + "/LinReg_Results/Figures/Linear_Regression_Numeric_" + text_extension + "_Residuals_vs_Target.jpg", bbox_inches="tight")


    fig = plt.figure(figsize = (20,20))
    plt.scatter(true_y, fitted_y, s = 100)
    plt.title("Fitted vs. Target - " + text_extension, fontdict = font_dict)
    plt.xlabel("Target Values", fontdict = font_dict)
    plt.ylabel("Fitted Values", fontdict = font_dict)
    plt.xticks(fontsize = tick_size, fontname = font_dict['family'])
    plt.yticks(fontsize = tick_size, fontname = font_dict['family'])
    ax = plt.gca()
    lims = [
        np.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
        np.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
    ]
    ax.plot(lims, lims, 'k-', alpha=0.75, zorder=0)
    ax.set_aspect('equal')
    ax.set_xlim(lims)
    ax.set_ylim(lims)
    fig.savefig(home_directory + "/LinReg_Results/Figures/Linear_Regression_Numeric_" + text_extension + "_Fitted_vs_Target.jpg", bbox_inches="tight")

