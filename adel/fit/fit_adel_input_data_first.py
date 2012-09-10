'''
This module is a facade for the first step of Adel input data fitting .

Created on Feb 7, 2012

@author: cchambon
'''  

import adel.fit.axis_table_fitting as axis_table_fitting
import adel.fit.dim_table_fitting as dim_table_fitting
import adel.fit.leaf_dynamic_parameters_table_fitting as leaf_dynamic_parameters_table_fitting

def fit_adel_input_data_first(plant_number=100, 
                              cohort_probabilities={'3': 0.0, '4': 0.900, '5': 0.967, '6': 0.817, '7': 0.083}, 
                              main_stem_leaves_number_probability_distribution={'10': 0.145, '11': 0.818, '12': 0.036, '13': 0.0, '14': 0.0},
                              bolting_date=500, flowering_date=1440,
                              final_axes_number=250):
    '''
    Fit the axis table partially, initialize the parameters table and initialize the dim table.
    :Parameters:
        - `plant_number` : the number of plants.
        - `cohort_probabilities` : probability of emergence of a child axis when the parent axis is present. This probability is 
           related to the cohort of the child axis.  
        - `main_stem_leaves_number_probability_distribution` : the probability distribution of the main stem leaves number.
        - `bolting_date` : The bolting date. Must be positive or null, and lesser than flowering_date.
        - `flowering_date` : The flowering date. Must be positive or null, and greater than bolting_date.
        - `final_axes_number` : the final number of axes
    :Types:
        - `plant_number` : int.
        - `cohort_probabilities` : dict.
        - `main_stem_leaves_number_probability_distribution` : dict
        - `bolting_date` : int
        - `flowering_date` : int
        - `final_axes_number` : int

    :return: The partially fitted axis table, the initialized dim table and the initialized parameters table.
    :rtype: a tuple of pandas.DataFrame
    '''    
    # Create and fit AxisTable
    axis_table_dataframe = axis_table_fitting.generate_axes(plant_number, cohort_probabilities, main_stem_leaves_number_probability_distribution)
    # Initialize the parameters table
    first_leaf_dynamic_parameters_table_dataframe = leaf_dynamic_parameters_table_fitting.fit_user_parameters_first(axis_table_dataframe['id_phen'].tolist())
    # Initialize DimTable
    first_dim_table_dataframe = dim_table_fitting.fit_dim_table_first(first_leaf_dynamic_parameters_table_dataframe)
    # Create a table with tillering dynamic: TT,NbrAxes
    tillering_dynamic_dataframe =  axis_table_fitting.create_tillering_dynamic_dataframe(0, bolting_date, flowering_date, plant_number, axis_table_dataframe, final_axes_number)

    return axis_table_dataframe, first_dim_table_dataframe, first_leaf_dynamic_parameters_table_dataframe, tillering_dynamic_dataframe



