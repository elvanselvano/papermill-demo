import papermill as pm
import os
import yaml

CONFIG_PATH = './'

def load_config(config_name):
     with open(os.path.join(CONFIG_PATH, config_name)) as file:
          config = yaml.safe_load(file)
     return config

def main():
     config = load_config('config.yaml')
     os.system("papermill --help-notebook ../template/paper-input.ipynb")
     
     result = pm.execute_notebook(config['dataset']['input_path'],
                                  config['notebook']['output_path'],
                                  kernel_name='python3',
                                  parameters=config['parameters'])
     
     print(result)

if __name__ == '__main__':
     main()

