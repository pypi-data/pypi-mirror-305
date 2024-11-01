# End of Distribution

`end_of_distribution` is a Python library designed for statistical outlier detection, focusing on identifying values at the "end of the distribution" in datasets. It provides methods for detecting outliers using both **Z-score** and **Interquartile Range (IQR)**, commonly used techniques in data preprocessing and analysis.

## Features

- **Z-Score Outliers**: Identify outliers based on their distance from the mean.
- **IQR Outliers**: Detects outliers based on the interquartile range, robust against extreme values.

## Installation

After cloning the repository:

```bash
git clone https://github.com/adityayadav0111/end_of_distribution.git
cd end_of_distribution
```

To install directly if available on PyPI:

```bash
pip install end_of_distribution
```

## Usage

Import the functions from `end_of_distribution` to detect outliers in your data.

```python
from lib.end_of_distribution import z_score_outliers, iqr_outliers

# Example data
data = [1, 2, 3, 4, 100, 5]

# Detect outliers with Z-score
z_outliers = z_score_outliers(data, threshold=3)
print("Z-score Outliers:", z_outliers)

# Detect outliers with IQR
iqr_outliers = iqr_outliers(data)
print("IQR Outliers:", iqr_outliers)
```

### API Reference

- **`z_score_outliers(data, threshold=3)`**
  - Parameters:
    - `data` (list): List of numerical values to check for outliers.
    - `threshold` (float): Z-score threshold for identifying outliers. Default is 3.
  - Returns: A list with True/False for outliers in the dataset.

- **`iqr_outliers(data)`**
  - Parameters:
    - `data` (list): List of numerical values to check for outliers.
  - Returns: A list with True/False indicating outliers.

## Contributing

We welcome contributions! Here’s how to get started:

1. **Fork** the repository and **clone** it locally.
2. Create a new **branch** for your contribution.
3. Make your changes and **commit**.
4. **Push** your changes and open a **pull request**.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.