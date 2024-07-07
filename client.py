import yaml
# test comment frontend
#testing auto sync=
#testing auto sync 2
#testing auto sync 3
if __name__ == "__main__":
    with open("../conf.yaml", 'r') as file:
        config = yaml.safe_load(file)
        print(f"Server IP Address: {config.get('ServerIPAddress')}")
        
