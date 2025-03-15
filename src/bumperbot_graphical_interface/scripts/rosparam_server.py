#!/usr/bin/env python3

import rospy
import yaml
from std_srvs.srv import Trigger, TriggerResponse
from bumperbot_graphical_interface.srv import GetParam, GetParamResponse

config = {}

def handle_get_config(_):
    import json
    return TriggerResponse(success=True, message=json.dumps(config))

def handle_get_param(req):
    keys = req.param_name.split('/')
    value = config
    try:
        for key in keys:
            value = value[key]
        return GetParamResponse(value)
    except KeyError:
        return GetParamResponse("")

if __name__ == '__main__':
    rospy.init_node('config_provider_node')

    # Load config file specified by parameter
    config_path = rospy.get_param('~config_path', '/path/to/parameters.yaml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Provide a service to return YAML as JSON
    rospy.Service('/get_config', Trigger, handle_get_config)
    rospy.Service('/get_param', GetParam, handle_get_param)
    rospy.spin()