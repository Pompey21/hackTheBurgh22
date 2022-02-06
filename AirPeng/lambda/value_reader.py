def get_aqi(json_data):
    return json_data['data']['aqi']

def get_measurement(json_data, measurement):
    return json_data['data']['iaqi'][measurement]['v']