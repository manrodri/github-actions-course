import json

def main():
    # load json into python object
    with open('./actions.json', "r") as file:
        
        data = json.load(file)
        actions = data['actions']
    
    # we pass valid versions that's going to come from dependanbot action.
    dependecy_to_update = {
        "name": "checkout",
        "versions": ["v3"],
    }
    
    # update dependecy
    for action in actions:
        if dependecy_to_update["name"] == action["name"]:
            action['versions'] = dependecy_to_update['versions']
            print(f"Dependency {action['name']} updated")
    
    with open('./actions.json', 'w') as file:
        data["actions"] = actions
        json.dump(data, file)


if __name__ == '__main__':
    main()