import json
import jsonschema
import yaml


def main():
    with open("docker_file.yaml", "r") as yaml_file:
        yaml_conf = yaml.safe_load(yaml_file.read())
    print(yaml_conf)


    with open
    jsonschema.validate(intance = yaml_conf)





if __name__ == '__main__':
    main()