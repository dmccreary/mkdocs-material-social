from mkdocs.plugins import BasePlugin
import re

class SocialOverridePlugin(BasePlugin):
    def on_page_context(self, context, page, config, **kwargs):
        if page.meta and 'image' in page.meta:
            page.custom_image = page.meta['image']
        return context
    
    def on_post_page(self, html, page, config, **kwargs):
        if not hasattr(page, 'custom_image'):
            return html
        
        site_url = config['site_url'].rstrip('/')
        image_path = '/' + page.custom_image.lstrip('/')
        full_image_url = site_url + image_path
        
        # Use regex to find and replace og:image meta tags
        html = re.sub(
            r'<meta property="og:image" content="[^"]*?/assets/images/social/[^"]*?"[^>]*?>',
            f'<meta property="og:image" content="{full_image_url}">',
            html
        )
        
        # Replace twitter:image meta tags
        html = re.sub(
            r'<meta name="twitter:image" content="[^"]*?/assets/images/social/[^"]*?"[^>]*?>',
            f'<meta name="twitter:image" content="{full_image_url}">',
            html
        )
        
        return html