import pandas as pd



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
