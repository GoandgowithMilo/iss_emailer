def iss_pass_function(lat, lon):
    import requests
    from datetime import datetime

    # parameters takes up to 4 inputs. Latitude and longitude of the location, n as how many orbits over this location to predict and alt as altitude over the location.
    parameters = {"lat": lat, "lon":lon, "n":1}
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    data = response.json()['response'][0]['risetime']

    return "The next pass will occur at " + str(datetime.utcfromtimestamp(data))
