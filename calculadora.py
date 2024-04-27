import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array_ = np.array(list).reshape(3, 3)

    mean = [np.mean(array_, axis=0).tolist(), np.mean(array_, axis=1).tolist(), np.mean(array_).tolist()]
    variance = [np.var(array_, axis=0).tolist(), np.var(array_, axis=1).tolist(), np.var(array_).tolist()]
    std_deviation = [np.std(array_, axis=0).tolist(), np.std(array_, axis=1).tolist(), np.std(array_).tolist()]
    maximum = [np.max(array_, axis=0).tolist(), np.max(array_, axis=1).tolist(), np.max(array_).tolist()]
    minimum = [np.min(array_, axis=0).tolist(), np.min(array_, axis=1).tolist(), np.min(array_).tolist()]
    sum_ = [np.sum(array_, axis=0).tolist(), np.sum(array_, axis=1).tolist(), np.sum(array_).tolist()]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_deviation,
        'max': maximum,
        'min': minimum,
        'sum': sum_
    }

    return calculations
