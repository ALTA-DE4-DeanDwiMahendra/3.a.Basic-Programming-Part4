def mean_median(array_input):
    if len(array_input) == 0:
        return None, None  # Return None for both mean and median if array_input is empty
    
    # Menghitung mean
    mean = sum(array_input) / len(array_input)
    
    # Menghitung median
    array_input.sort()
    n = len(array_input)
    mid = n // 2
    if n % 2 == 0:
        median = (array_input[mid - 1] + array_input[mid]) / 2
    else:
        median = array_input[mid]
    
    return mean, median

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4]))        # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5]))     # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15]))   # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50]))# (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120]))# (49.0, 30)
    print(mean_median([]))                  # (None, None) for empty input
