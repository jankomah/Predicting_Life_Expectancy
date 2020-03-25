import pandas as pd
from sklearn.linear_model import LassoLarsIC
from itertools import combinations
from statsmodels.stats.outliers_influence import variance_inflation_factor


def get_cat(df):
    """get list of cat features from df"""
    cat = []
    for x in df.columns:
        if df[x].dtypes == 'object':
            cat.append(x)
    return cat


def get_nom(df):
    """get nom features"""
    nom = []
    for x in df.columns:
        if df[x].dtypes != 'object':
            nom.append(x)
    return nom[2:] # no need for feature id and age but customise according to df

"""Function for OneHotEncoding"""
def encode_features(data_set, feature_names):
    for feature_name in feature_names:
        le = LabelEncoder()
        le.fit(data_set[feature_name])
        encoded_column = le.transform(data_set[feature_name])
        data_set[feature_name] = encoded_column
    return data_set


def variance_inflation_factor(feature_list, DataFrame):
    """
    Passes the inputs into statsmodel's variance_inflation_factor function.
    Returns a DataFrame with each feature and its variance inflation factor.
    """
    feature_df = DataFrame[feature_list]
    vif = [variance_inflation_factor(feature_df.values, i)
           for i in range(feature_df.shape[1])]
    data = list(zip(feature_list, vif))
    data_df = pd.DataFrame(data, columns=['Feature','VIF'])
    return data_df


# Remove Multicollinear features
def remove_collinear(x , threshold):
    
    y = x['loan_status']
    x = x.drop(columns = ['loan_status'])
    
    #calc the correlation matrix
    corr_matrix = x.corr()
    elements = range(len(corr_matrix.columns) - 1)
    drop_cols = []
    
    # Iterate through cor matrix and compare correlations
    for s in elements:
        for j in range(i):
            item = corr_matrix.iloc[j:(j+1) , (s+1):(s+2)]
            col = item.columns
            row = item.index
            val = abs(item.values)
            
            # if corr exceeds threshold
            if val >= threshold:
                drop_cols.append(col.values[0])
                
    # Drop one of each pair of correlated columns
    drops = set(drop_cols)
    x = x.drop(columns = drops)
    
    # Add the score back into the data
    x['loan_status'] = y
    
    return x   








