import io
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaIoBaseDownload

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_1_480840362897-4n84emjclhrshmthi4vdj2eu22q0uhfp.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    # credentials = flow.run_console()
    credentials = flow.run_local_server(port=3000)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.captions().list(
        part="snippet",
        videoId="M7FIvfx5J10"
    )
    response = request.execute()

    # print(response)

    captionID = ""
    for caption in response.get("items", []):
        if caption["snippet"]["language"] == "en":
            captionID = caption["id"]
            print("\nCaption ID:", captionID)

            print("Language:", caption["snippet"]["language"])
            print("Last Updated:", caption["snippet"]["lastUpdated"])
            print()

    request = youtube.captions().download(
        id="AUieDabtbewAoYf8lCfnfuXcILjAGpv59b7UPZ_y8u4r"
    )

    fh = io.FileIO("output.txt", "wb")

    download = MediaIoBaseDownload(fh, request)
    complete = False
    while not complete:
        status, complete = download.next_chunk()


if __name__ == "__main__":
    main()
