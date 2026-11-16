"""This module contains functions for design of experiments analysis for HW 4 in AE 498 Data-Driven Modeling and Optimization."""

import numpy as np
import matplotlib.pyplot as plt

def effects(responses, n_replicates):
    """Function to calculate main and interaction effects for a 2^2 factorial experiment.

    Parameters
    ----------
    responses : array_like
        Input response data (4 x n_replications dimensions), where each row is an observed response for a condition (ordered in the standard order) and each column is a replicate.
        For example, responses[0,1] = response from replicate 1 for condition (1), responses[1,1] = response from replicate 1 for condition a.
    n_replicates : int
        Number of replications in the experiment data.

    Returns
    -------
    effects : array_like
        Calculated effects (3 x 1 dimensions) for A, B, and AB.

    Notes
    -----
    Standard order of experiment conditions (order of rows in responses) = (1), a, b, ab
    """

    # YOUR CODE HERE
    responses = np.asarray(responses)

    mean_responses = responses.mean(1)

    effect_a = ((mean_responses[1] + mean_responses[3]) * 0.5
                - (mean_responses[0] + mean_responses[2]) * 0.5)

    effect_b = ((mean_responses[2] + mean_responses[3]) * 0.5
                - (mean_responses[0] + mean_responses[1]) * 0.5)

    effect_ab = (mean_responses[3] - mean_responses[1]
                 - mean_responses[2] + mean_responses[0]) * 0.5

    return np.array([effect_a, effect_b, effect_ab])


def plot_effects(responses, n_replicates):
    """Function to plot effects for a 2^2 factorial experiment.

    Parameters
    ----------
    responses : array_like
        Input response data (4 x n_replications dimensions), where each row is an observed response for a condition (ordered in the standard order) and each column is a replicate.
        For example, responses[0,1] = response from replicate 1 for condition (1), responses[1,1] = response from replicate 1 for condition a.
    n_replicates : int
        Number of replications in the experiment data.

    Returns
    -------
    out : list
        List of artists added.

    Notes
    -----
    This function structure is based on matplotlib's suggested signature function for returning a plot:
    https://matplotlib.org/3.5.0/tutorials/introductory/usage.html#the-object-oriented-interface-and-the-pyplot-interface
    """

    # YOUR CODE HERE
    responses = np.asarray(responses)

    mean_responses = responses.mean(1)

    fig, ax = plt.subplots()
    out = (ax.plot([1, 2], [mean_responses[2], mean_responses[3]], "o--", label="B+")
           + ax.plot([1, 2], [mean_responses[0], mean_responses[1]], "o--", label="B-"))

    ax.set_xticks([1, 2])
    ax.set_xticklabels(["Low, -", "High, +"])
    ax.set_xlabel("Factor A")
    ax.set_ylabel("Response")
    ax.legend()

    return out


def plot_tornado(responses, n_replicates):
    """Function to make a tornado plot for a 2^2 factorial experiment.

    Parameters
    ----------
    responses : array_like
        Input response data (4 x n_replications dimensions), where each row is an observed response for a condition (ordered in the standard order) and each column is a replicate.
        For example, responses[0,1] = response from replicate 1 for condition (1), responses[1,1] = response from replicate 1 for condition a.
    n_replicates : int
        Number of replications in the experiment data.

    Returns
    -------
    out : list
        List of artists added.

    Notes
    -----
    This function structure is based on matplotlib's suggested signature function for returning a plot:
    https://matplotlib.org/3.5.0/tutorials/introductory/usage.html#the-object-oriented-interface-and-the-pyplot-interface
    """

    # YOUR CODE HERE
    effect_values = effects(responses, n_replicates)

    fig, ax = plt.subplots()
    bars = ax.barh(["A", "B", "AB"], effect_values)
    ax.invert_yaxis()

    ax.axvline(0, color="k", linewidth=0.8)
    ax.set_xlabel("Average Effect")
    ax.set_ylabel("Factor or Interaction")

    return list(bars)