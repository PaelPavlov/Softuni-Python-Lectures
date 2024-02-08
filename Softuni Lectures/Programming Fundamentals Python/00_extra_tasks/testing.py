import requests

def get_user_info(username):
    url = f'https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client
    _id=407408718192.apps.googleusercontent.com&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.activity.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_glucose.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.blood_pressure.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.body_temperature.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.heart_rate.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.location.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.nutrition.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.oxygen_saturation.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.reproductive_health.write+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.read+
    https%3A%2F%2Fwww.googleapis.com%2Fauth%2Ffitness.sleep.write&access_type=offline'
    response = requests.get(url)

    if response.status_code == 200:
        data = data.json()
        return data
    else:
        print('Error 404')
        return None

username = input('Give us your email address or username? ')      
print(get_user_info(username))