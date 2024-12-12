# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:34:17 2024

@author: past
"""

#statistical analysis functions

from scipy.stats import ttest_ind, f_oneway, kstest, shapiro, norm, mannwhitneyu, levene
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def perform_normal_test(melted_data, alpha = 0.05):
    if len(melted_data) < 2:
        raise ValueError("Normaldistribution test needs at least two values!")

    if len(melted_data) <=200:
        test_nv, p = kstest(melted_data, 'norm', args = (norm.mean(melted_data), norm.std(melted_data)))
    else: 
        test_nv, p = shapiro(melted_data)
    
    return bool(p >= alpha)
    
def perform_ranktest(melted_data, treatment_to_compare): 
    if treatment_to_compare not in melted_data.columns:
        raise ValueError(f"Spalte '{treatment_to_compare}' fehlt im DataFrame.")
    if 'Value' not in melted_data.columns:
        raise ValueError("Spalte 'Value' fehlt im DataFrame.")
        
    treatments = melted_data[treatment_to_compare].unique()
    if len(treatments) == 2:
        group1 = melted_data[melted_data[treatment_to_compare] == treatments[0]]['Value']
        group2 = melted_data[melted_data[treatment_to_compare] == treatments[1]]['Value']
        if len(group1) == 0 or len(group2) == 0:
            raise ValueError("One group does not contain values. Please check data. ")
        
        # Mann-Whitney-U-Test (Wilcoxon für unabhängige Stichproben)
        w_stat, w_p_value = mannwhitneyu(group1, group2, alternative='two-sided')
        print(f"U-statistic: {w_stat}, p-value: {w_p_value}")
        return w_stat, w_p_value
    else:
        print("No statistic! Current statistical analysis requires exactly two or more treatments.")
        return None, None

def perform_t_test(melted_data, treatment_to_compare):
    # Conduct a t-test between two treatments if applicable
    treatments = melted_data[treatment_to_compare].unique()
    if len(treatments) == 2:
        group1 = melted_data[melted_data[treatment_to_compare] == treatments[0]]['Value']
        group2 = melted_data[melted_data[treatment_to_compare] == treatments[1]]['Value']
        #test of variance homogeneity
        l_stat, p_value_levene = levene(group1, group2)
        equal_var = p_value_levene > 0.05
        print(f"Equal Variance: {equal_var}")
        # Perform the t-test (independant)
        t_stat, p_value = ttest_ind(group1, group2, equal_var = equal_var)
        print(f"t-statistic: {t_stat}, p-value: {p_value}")
        return t_stat, p_value
        
    else:
        print("No statistic! Current statistical analysis requires exactly two or more treatments.")
        return None, None
    
def perform_anova(melted_data, treatment_to_compare):
    # Perform ANOVA between multiple treatments
    treatments = melted_data[treatment_to_compare].unique()
    if len(treatments) > 2:
        groups = [melted_data[melted_data[treatment_to_compare] == t]['Value'] for t in treatments]
        f_stat, p_value = f_oneway(*groups)
        
        print(f"ANOVA F-statistic: {f_stat}, p-value: {p_value}")
        if p_value < 0.05: 
            tukey_result = pairwise_tukeyhsd(melted_data['Value'], melted_data[treatment_to_compare], alpha=0.05)
            #print(tukey_result)
            return f_stat, p_value, tukey_result.summary()
        else:
            print("No significant difference, therefore no post-hoc test required.")
            return f_stat, p_value, None
        
    else:
        print("ANOVA requires more than two treatments.")
        return None, None, None