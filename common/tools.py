import random
import os
import yaml


def get_num(n):
    return "".join(random.sample("0123456789",n))

def read_yml(filepath):

    baseDir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ymlPath = os.path.join(baseDir,filepath)
    ymlFile = open(ymlPath, "r", encoding="utf-8")
    cfg = ymlFile.read()
    f = yaml.safe_load(cfg)
    #print(f)
    return f





if __name__ == '__main__':
    #print(get_num(3))
    read_yml(r"case/test_data.yml")