def create_mu_ratio_dynamic(df):
    # Create a column for expenditure ratio
    df['non_food_forward'] = df['non_food'].shift(-1)
    df['PMt_cMt/PMt+1_cMt+1'] = df['non_food'] / df['non_food_forward']

    # Create a column for price ratio
    df['cpi_ind_forward'] = df['cpi_ind'].shift(-1)
    df['PMt+1/PMt'] = df['cpi_ind_forward'] / df['cpi_ind']

    # Multiply the expenditure ratio by the price ratio
    df['cMt/cMt+1'] = df['PMt_cMt/PMt+1_cMt+1'] * df['PMt+1/PMt']

    df['cMt'] = df['non_food'] / df['cpi_ind']

    return df


def create_mu_ratio_static(df, PA_gammaA, etaA, etaM):
    df['food-PA_gammaA'] = df.food - PA_gammaA
    df['PA_cA-gammaA/PM_cM'] = df['food-PA_gammaA'] / df.non_food

    # Multiply by the ratio of the Cobb-Douglas parameters
    df['muM/PM/muA/PA'] = etaM/etaA * df['PA_cA-gammaA/PM_cM']

    return df
