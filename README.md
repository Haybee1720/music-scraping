Spotify Billboard Playlist Creator
This is a Python script that creates a private playlist on Spotify based on the Billboard Hot 100 chart from a specified date.

Requirements
To run this script, you will need:

A Spotify account
A registered Spotify application
The spotipy library installed
The requests library installed
The beautifulsoup4 library installed
Setup
Clone this repository to your local machine.
In the Spotify Developer Dashboard, create a new application and note the Client ID and Client Secret values.
In the settings for your new application, add http://localhost:8888/callback/ as a Redirect URI.
Create a virtual environment and activate it.
Install the required libraries using pip install -r requirements.txt.
In the root of the project, create a .env file with the following contents:
rust
Copy code
SPOTIPY_CLIENT_ID='your-client-id'
SPOTIPY_CLIENT_SECRET='your-client-secret'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
Replace your-client-id and your-client-secret with the values you noted in step 2.
Run the script using python main.py.
Follow the instructions in the console to create your playlist.
License
This project is licensed under the MIT License.
