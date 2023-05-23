import json
import instaloader

def download_saved_posts(json_file, target_directory):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
        
    saved_posts = data['saved_saved_media']

    L = instaloader.Instaloader()
    L.download_videos = False
    L.save_metadata = False
    
    # Iterate over the saved posts and download them
    for post in saved_posts:
        shortcode = post['string_map_data']['Saved on']['href'].split("/")[-2]
        try:
            # Download the post using the shortcode
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            L.download_post(post, target_directory)
            print(f"Downloaded post with shortcode: {shortcode}")
        except Exception as e:
            print(f"Failed to download post with shortcode: {shortcode}")
            print(f"Error message: {str(e)}")

    print("Download complete!")

# Paths and stuff
json_file = '/mnt/c/Users/harsh/Desktop/saved_posts.json'
target_directory = '/Saved'
download_saved_posts(json_file, target_directory)
