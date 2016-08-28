# Author: Laurence Armstrong

import requests
import json

api_keys = {
    "Richard": 'fd276502-7625-4c92-834b-6ab7b4255ed7',
    "Josh": '8def074f-0399-45e8-a130-aef62c9e440f',
    "Laurence": '440446dc-c265-489b-b317-1af0c583b0b9'
}
APITemplate = "https://api.at.govt.nz/v1/gtfs/stops?api_key={}"

if __name__ == "__main__":
    r = requests.get(APITemplate.format(api_keys["Richard"]))
    print("Making API request")
    if r.status_code == 200:
        print("Request successful, writing to file")
        stop_data = r.json()

        with open("stopData", "w") as f:
            json.dump(stop_data['response'], f)
            # for s in stop_data['response']:
                # f.write("{},{},{},{}\n".format(s['stop_id'], s['stop_name'],
                                                    # s['stop_lat'], s['stop_lon']))
        print("Done.")
    else:
        print("Failed to get data")
