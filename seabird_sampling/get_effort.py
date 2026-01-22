import numpy as np


def get_effort(track_times):
    effort = np.zeros(len(track_times))
    for i in range(len(track_times)):
        effort[i] = track_times[i][2]
    return effort
