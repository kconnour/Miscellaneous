import numpy as np


if __name__ == '__main__':
    # These are for 2025
    boundaries = np.array([0, 11925, 48475, 103350, 197300, 250525, np.inf])
    diff = np.diff(boundaries)
    rate = np.array([0.10, 0.12, 0.22, 0.24, 0.32, 0.35])

    income = 85000 - 4000 - 23500
    bottom_boundary = np.argmin(income > boundaries) - 1

    taxes_to_pay = np.sum((diff * rate)[:bottom_boundary])
    taxes_to_pay += (income - boundaries[bottom_boundary]) * rate[bottom_boundary]

    print('2025 federal taxes')
    print(f'Total taxes: ${taxes_to_pay}')
    print(f'Average tax rate: {taxes_to_pay / income * 100}%')

    # Colorado specifically
    taxes_to_pay += income * 0.044

    print('2025 federal + state taxes')
    print(f'Total taxes: ${taxes_to_pay}')
    print(f'Average tax rate: {taxes_to_pay / income * 100}%')
