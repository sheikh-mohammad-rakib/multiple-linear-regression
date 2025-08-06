# Multiple Linear Regression Lab

This project demonstrates how to implement multiple linear regression using Python and scikit-learn. The lab uses a real-world dataset of fuel consumption and CO2 emissions for vehicles sold in Canada.

## Objectives

- Use scikit-learn to implement multiple linear regression
- Create, train, and test a regression model on real data
- Visualize model outputs and evaluate performance

## Dataset

The dataset (`FuelConsumptionCo2.csv`) contains model-specific fuel consumption ratings and estimated carbon dioxide emissions for new light-duty vehicles. Key features include engine size, fuel consumption, and CO2 emissions.

## Requirements

- Python 3.8+
- NumPy
- Pandas
- Matplotlib
- scikit-learn

Install dependencies with:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Usage

1. Open the notebook `Mulitple-Linear-Regression.ipynb`.
2. Run the cells sequentially to:
   - Load and explore the data
   - Select and preprocess features
   - Train and evaluate multiple linear regression models
   - Visualize results

## Exercises

The notebook includes exercises to:
- Fit and visualize simple and multiple regression models
- Compare model performance on train and test data
- Explore feature selection and model improvement

## Cloning and Running the Project

Follow these steps to clone the repository and run both the notebook and `app.py` on any device:

### 1. Prerequisites

- Install Python 3.x from [python.org](https://www.python.org/downloads/).
- (Optional) Install Git from [git-scm.com](https://git-scm.com/downloads).

### 2. Clone the Repository

```bash
git clone https://github.com/sheikh-mohammad-rakib/multiple-linear-regression.git
cd multiple-linear-regression
```

### 3. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Running `app.py`

```bash
python app.py
```

### 6. Running the Notebook

- Install Jupyter if not already installed:
  ```bash
  pip install notebook
  ```
- Start Jupyter Notebook:
  ```bash
  jupyter notebook
  ```
- Open the notebook file (e.g., `multiple-linear-regression.ipynb`) in your browser and run the cells.

## License

This project is for educational purposes.
