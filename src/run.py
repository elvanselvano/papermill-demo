import papermill as pm
from config import *

# pm.inspect_notebook('paper-demo.ipynb')
# papermill --help-notebook ../notebooks/paper-input.ipynb

if __name__ == '__main__':
     result = pm.execute_notebook(INPUT_PATH, OUTPUT_PATH, PARAMETERS)

