import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_1_480840362897-4n84emjclhrshmthi4vdj2eu22q0uhfp.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    # credentials = flow.run_console()
    credentials = flow.run_local_server(port=8080)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.captions().list(
        part="snippet",
        videoId="M7FIvfx5J10"
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()
