# task_02_requests.py

import requests
import csv

def fetch_and_print_posts():
    """Fetch posts and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post["title"])
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_and_save_posts():
    """Fetch posts and save them to posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            data_to_save = [
                {"id": post["id"], "title": post["title"], "body": post["body"]}
                for post in posts
            ]

            with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data_to_save)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
