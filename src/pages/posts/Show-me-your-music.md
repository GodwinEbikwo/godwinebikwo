---
layout: ../../layouts/MarkdownPostLayout.astro
slug: 'Show-me-your-music-and-I-can-tell-you-who-you-are.md'
title: 'My Spotify Music Analysis'
pubDate: 2022-07-01
description: 'Accessing my spotify Api data'
author: 'Godwin Ebikwo'
# image:
#     url: 'https://xgjzloifyvgpbmyonaya.supabase.co/storage/v1/object/public/files/eIrUURb9l7/Ti8FwivPeA'
#     alt: 'The full Astro logo.'
tags: ['API', 'Data Visualisation']
---

<img
  src="https://binsta.dev/api/v1/files/eIrUURb9l7/transform?format=webp&size=lg&quality=hi"
  srcset="
    https://binsta.dev/api/v1/files/eIrUURb9l7/transform?format=webp&size=2xs 100w,
    https://binsta.dev/api/v1/files/eIrUURb9l7/transform?format=webp&size=xs 300w,
    https://binsta.dev/api/v1/files/eIrUURb9l7/transform?format=webp&size=sm 500w,
    https://binsta.dev/api/v1/files/eIrUURb9l7/transform?format=webp&size=md 750w,
    https://binsta.dev/api/v1/files/eIrUURb9l7/transform?format=webp&size=lg 1000w,
    https://binsta.dev/api/v1/files/eIrUURb9l7/transform?format=webp&size=xl 1500w,
    https://binsta.dev/api/v1/files/eIrUURb9l7/transform?format=webp&size=2xl 2500w
  "
  sizes="(max-width: 1000px) 100vw, 1000px"
  alt="attribution-img.svg"
/>

# Analyzing Your Spotify Listening History: A Primer

Have you ever wondered about the patterns hidden within your music preferences? The songs that resonate with you during various moods and moments? Analyzing your Spotify listening history can provide fascinating insights into your musical journey. In this primer, we'll guide you through the process of gathering your listening history and exploring ways to analyze it.

## Prerequisites

Before you start working with the Spotify API, you'll need to have the following:

1. **Spotify Account**: If you don't have one already, sign up for a Spotify account.

2. **Developer Account**: Create a developer account on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

3. **Application**: After creating a developer account, create a new application to obtain your **Client ID** and **Client Secret**.

# Analyzing Your Spotify Listening History with Python

If you're eager to dive into your Spotify listening history and gain insights into your musical preferences, you're in the right place. In this guide, we'll show you how to use the Spotipy package in Python to access your listening history and perform basic analysis.

## Step 1: Installing Spotipy

First, you need to install the Spotipy package, which allows you to interact with the Spotify API.

```markdown
Installation: pip install spotipy
```

## Step 2: Setting Up Spotipy

To begin, import the necessary libraries and set up Spotipy with your Spotify Developer credentials.

```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    redirect_uri='YOUR_REDIRECT_URI',
    scope='user-read-recently-played'
))
```

## Step 3: Retrieving Your Listening History

Now, you can retrieve your recent listening history using the `current_user_recently_played` method.

```python
recent_tracks = sp.current_user_recently_played(limit=50)
for item in recent_tracks['items']:
    track = item['track']
    print(track['name'], 'by', track['artists'][0]['name'])
```

## Step 4: Basic Analysis

Let's perform some basic analysis on your listening history. In this example, we'll count the occurrence of each artist in your recent tracks.

```python
from collections import Counter

artists = [item['track']['artists'][0]['name'] for item in recent_tracks['items']]
artist_counts = Counter(artists)

print("Top 5 Artists in Your Recent Listening History:")
for artist, count in artist_counts.most_common(5):
    print(artist, '-', count, 'plays')
```

## Step 5: Visualization

To visualize your listening history, you can create a bar chart of the top artists.

```python
import matplotlib.pyplot as plt

top_artists = [artist for artist, _ in artist_counts.most_common(5)]
play_counts = [count for _, count in artist_counts.most_common(5)]

plt.barh(top_artists, play_counts)
plt.xlabel('Play Counts')
plt.ylabel('Artists')
plt.title('Top 5 Artists in Your Recent Listening History')
plt.show()
```

## Conclusion

By utilizing the Spotipy package in Python, you've unlocked the ability to access your Spotify listening history and gain insights into your musical preferences. From retrieving recent tracks to performing basic analysis and creating visualizations, you've taken the first steps towards understanding your music habits on a deeper level. This journey into your listening history can uncover trends, surprises, and connections you may not have been aware of. Enjoy exploring the melodies that shape your life!
