from mkdocs.plugins import BasePlugin
import re
import os

class SocialOverridePlugin(BasePlugin):
    def on_page_context(self, context, page, config, **kwargs):
        """Save custom image path from page metadata if it exists"""
        if page.meta and 'image' in page.meta:
            page.custom_image = page.meta['image']
            print(f"DEBUG: Found custom image in {page.file.src_path}: {page.custom_image}")
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
        
        print(f"DEBUG: Processing page {page.file.src_path} with custom image: {full_image_url}")
        
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