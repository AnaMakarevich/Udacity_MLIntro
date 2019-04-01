#!/usr/bin/python


def outlier_cleaner(predictions: list, ages: list, net_worths: list):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    for i in range(len(predictions)):
        error = net_worths[i] - predictions[i]
        cleaned_data.append((ages[i], net_worths[i], error))
    # sort in ascending order
    cleaned_data.sort(key=lambda t: abs(t[2]))
    # calculate how many obs we need to retain
    num_obs = int(0.9*len(predictions))

    return cleaned_data[:num_obs]


