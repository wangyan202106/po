import yaml
from config import BASE_DIR
def build_data_fun():
    with open(BASE_DIR + '/data/data.yaml', encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data

