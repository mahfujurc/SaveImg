import instaloader
import os

def download_images(username, target_folder):
    loader = instaloader.Instaloader()

    # Ensure the target folder exists, create it if not
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Fetch the profile by username (no need for login as it's public)
    profile = instaloader.Profile.from_username(loader.context, username)

    # Download each post and save it to the target folder
    for post in profile.get_posts():
        print(f"Downloading {post.url}")
        loader.download_post(post, target=target_folder)  # Save posts in the specified folder

if __name__ == "__main__":
    download_images('cutu_afrin', 'downloads/cutu_afrin')  # Save images in "downloads/cutu_afrin"
