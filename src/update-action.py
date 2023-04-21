import json
import os

def main():
    # load json into python object
    with open('./actions.json', "r") as file:
        
        data = json.load(file)
        actions = data['actions']
    
    # we pass valid versions that's going to come from dependanbot action.
    action_name = os.environ.get('ACTION_NAMES')
    new_version = os.environ.get('NEW_VERSION')
    previous_version = os.environ.get('PREVIOUS_VERSION')

    if not action_name or not new_version or not previous_version:
        raise OSError("PR action details not available. ")
    

    [print(os.environ.get(var)) for var in ['ACTION_NAMES', 'NEW_VERSION', 'PREVIOUS_VERSION']]
    
    # CHANGE_DETECTED = False
    # # update actions
    # for action in actions:
    #     if action_name == action["name"]:
    #         action['versions'].remove(previous_version)
    #         if new_version not in action['versions']:
    #             action['versions'].append(new_version)

    #         print(f"Dependency {action['name']} updated")
    #         print(f"{action['name']} new versions are:  {action['versions']}")
    #         CHANGE_DETECTED = True
    # if CHANGE_DETECTED:
    #     with open('./actions.json', 'w') as file:
    #         data["actions"] = actions
    #         json.dump(data, file)


if __name__ == '__main__':
    main()