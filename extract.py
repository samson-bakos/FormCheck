import requests

# Read app ID and app secret from the credentials file
credentials_file_path = '/Users/samsonbakos/keys/formcheck_credentials.txt'

with open(credentials_file_path, 'r') as file:
    credentials = dict(line.strip().split('=') for line in file)

app_id = credentials.get('INSTAGRAM_APP_ID')
app_secret = credentials.get('INSTAGRAM_APP_SECRET')

if not app_id or not app_secret:
    raise ValueError("Please provide valid INSTAGRAM_APP_ID and INSTAGRAM_APP_SECRET in the credentials file.")

# Get an App Token
token_url = f'https://graph.instagram.com/v12.0/oauth/access_token?client_id={app_id}&client_secret={app_secret}&grant_type=client_credentials'

try:
    response = requests.get(token_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    app_token = response.json().get('access_token')

    # Replace 'Squat' with the hashtag you want to search for
    hashtag = 'Squat'

    # Get recent media with the specified hashtag using the App Token
    media_url = f'https://graph.instagram.com/v12.0/tags/{hashtag}/recent_media?access_token={app_token}'
    response = requests.get(media_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    media_data = response.json()

    # Process the media data as needed
    for media in media_data.get('data', []):
        video_url = media.get('permalink')
        print(f"Video URL: {video_url}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    print(f"Response content: {response.text}")
    raise
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
