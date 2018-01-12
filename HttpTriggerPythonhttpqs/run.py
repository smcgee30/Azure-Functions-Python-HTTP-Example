import sys, requests, os

# Initial setup

endpoint = 'https://dashboard.signalsciences.net/api/v0'
email = os.environ.get('SIGSCI_EMAIL')
password = os.environ.get('SIGSCI_PASSWORD')

# Authenticate

auth = requests.post(
    endpoint + '/auth',
    data = {"email": email, "password": password}
)

if auth.status_code == 401:
    print 'Invalid login.'
    sys.exit()
elif auth.status_code != 200:
    print 'Unexpected status: %s response: %s' % (auth.status_code, auth.text)
    sys.exit()

parsed_response = auth.json()
token = parsed_response['token']

# Fetch list of corps

headers = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer %s' % token
}
corps = requests.get(endpoint + '/corps', headers=headers)
print corps.text
