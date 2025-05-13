# Social Overrides

This solution uses a custom Python plugin that:

Identifies pages with custom images in their metadata
Processes the HTML after it's generated
Finds and replaces the social plugin's meta tags with your custom image URLs

This approach is robust because:

It works with any version of mkdocs-material
It doesn't rely on JavaScript that might not be executed by social media crawlers
It directly modifies the final HTML output
It only affects pages where you've defined a custom image

To add custom images to any page, simply include the image property in the page's front matter:

## Installation

in the plugins folder create two files:

plugins/__init__.py
plugins/social_overview.py

## Setup

Place the following code into ```setup.py``` in the project root (not in docs)

```python
from setuptools import setup, find_packages

setup(
    name='social_override',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'social_override = plugins.social_override:SocialOverridePlugin',
        ]
    }
)
```

Run the setup:

```sh
pip install -e . 
```

Sample terminal log:

```
Obtaining file:///Users/danmccreary/Documents/ws/mkdocs-material-social
  Preparing metadata (setup.py) ... done
Installing collected packages: social-override
  Attempting uninstall: social-override
    Found existing installation: social-override 0.1
    Uninstalling social-override-0.1:
      Successfully uninstalled social-override-0.1
  Running setup.py develop for social-override
Successfully installed social-override-0.1
```

## Page Setup

Add the following to your markdown file that you DO NOT want the social card to be used.
This will use a file called `my-custom-image.png` in the img directory.

```yml
---
title: Page Title
description: Page description
image: img/my-custom-image.png
---
```

Note that the file should have a width to height ratio of 1.91 to 1. You can use the src/resize program
to resize the image to have a white background to get the correct ratio.

## Testing

After you run `mkdocs gh-deploy` you can test the social card previews with these tools:

[SocialSharePreview.com](https://socialsharepreview.com/?url=https://dmccreary.github.io/mkdocs-material-social/metadata-override-test/)

[Metatags.io](https://metatags.io/)

## Source Code for Social Override Plugin (no debug)

```python
from mkdocs.plugins import BasePlugin
import re

class SocialOverridePlugin(BasePlugin):
    def on_page_context(self, context, page, config, **kwargs):
        """Save custom image path from page metadata if it exists"""
        if page.meta and 'image' in page.meta:
            page.custom_image = page.meta['image']
        return context
    
    def on_post_page(self, html, page, config, **kwargs):
        """Replace social plugin meta tags with our custom image"""
        # Only process pages with custom image
        if not hasattr(page, 'custom_image'):
            return html
        
        # Build the full URL for the custom image
        site_url = config['site_url'].rstrip('/')
        image_path = '/' + page.custom_image.lstrip('/')
        full_image_url = site_url + image_path
        
        # Find and replace OpenGraph image tags
        og_tags = re.findall(r'<meta\s+property="og:image"[^>]*?>', html)
        for tag in og_tags:
            if '/assets/images/social/' in tag:
                new_tag = f'<meta property="og:image" content="{full_image_url}">'
                html = html.replace(tag, new_tag)
        
        # Find and replace Twitter image tags
        twitter_tags = re.findall(r'<meta\s+name="twitter:image"[^>]*?>', html)
        for tag in twitter_tags:
            if '/assets/images/social/' in tag:
                new_tag = f'<meta name="twitter:image" content="{full_image_url}">'
                html = html.replace(tag, new_tag)
        
        return html

# Make the plugin available to MkDocs
def get_plugin():
    return SocialOverridePlugin()
```

## Social Override With Debug

```python
from mkdocs.plugins import BasePlugin
import re
import os

class SocialOverridePlugin(BasePlugin):
    def on_page_context(self, context, page, config, **kwargs):
        """Save custom image path from page metadata if it exists"""
        if page.meta and 'image' in page.meta:
            page.custom_image = page.meta['image']
            # print(f"DEBUG: Found custom image in {page.file.src_path}: {page.custom_image}")
        return context
    
    def on_post_page(self, html, page, config, **kwargs):
        """Replace social plugin meta tags with our custom image"""
        # Only process pages with custom image
        if not hasattr(page, 'custom_image'):
            return html
        
        # Build the full URL for the custom image
        site_url = config['site_url'].rstrip('/')
        image_path = '/' + page.custom_image.lstrip('/')
        full_image_url = site_url + image_path
        
        # print(f"DEBUG: Processing page {page.file.src_path} with custom image: {full_image_url}")
        
        # Check if social plugin tags exist in the HTML
        if '/assets/images/social/' in html:
            print(f"DEBUG: Found social plugin tags in HTML for {page.file.src_path}")
        else:
            print(f"DEBUG: No social plugin tags found in HTML for {page.file.src_path}")
        
        # Direct approach with simpler tag finding
        og_tags = re.findall(r'<meta\s+property="og:image"[^>]*?>', html)
        twitter_tags = re.findall(r'<meta\s+name="twitter:image"[^>]*?>', html)
        
        print(f"DEBUG: Found {len(og_tags)} og:image tags and {len(twitter_tags)} twitter:image tags")
        
        # Replace og:image tags
        for tag in og_tags:
            if '/assets/images/social/' in tag:
                new_tag = f'<meta property="og:image" content="{full_image_url}">'
                html = html.replace(tag, new_tag)
                print(f"DEBUG: Replaced og:image tag")
        
        # Replace twitter:image tags
        for tag in twitter_tags:
            if '/assets/images/social/' in tag:
                new_tag = f'<meta name="twitter:image" content="{full_image_url}">'
                html = html.replace(tag, new_tag)
                print(f"DEBUG: Replaced twitter:image tag")
        
        return html

# Make the plugin available to MkDocs
def get_plugin():
    return SocialOverridePlugin()
```

## Claude Dialog

[Claud Override Trials and Final Plugin](https://claude.ai/share/c7a44a8b-3f78-4e6f-9b79-f43c1056bf17) - a log of the dozens of solutions we tried with Claude using overrides.