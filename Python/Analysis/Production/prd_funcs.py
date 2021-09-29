def create_labor_prd_ratio(df, alphaLA, alphaLM):
    df['F_LA'] = alphaLA * df['prm_GDP']/df['prm_emp']
    df['F_LM'] = alphaLM * df['non_prm_GDP']/df['non_prm_emp']
    df['F_LM/F_LA'] = df['F_LM']/df['F_LA']

    return df


def create_cap_prd_ratio(df, alphaKA, alphaKM):
    df['F_KA'] = alphaKA * df['prm_GDP']/df['prm_cap']
    df['F_KM'] = alphaKM * df['non_prm_GDP']/df['non_prm_cap']
    df['F_KM/F_KA'] = df['F_KM']/df['F_KA']

    return df


def create_cap_ratio(df):
    df['KM/KA'] = df['non_prm_cap']/df['prm_cap']

    return df


def create_labor_ratio(df):
    df['LM/LA'] = df['non_prm_emp']/df['prm_emp']

    return df


def create_output_ratio(df):
    df['YM/YA'] = df['non_prm_GDP']/df['prm_GDP']

    return df
