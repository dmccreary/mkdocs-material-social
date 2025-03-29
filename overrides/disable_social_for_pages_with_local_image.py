from mkdocs.plugins import BasePlugin

class DisableSocialForPagesWithLocalImagePlugin(BasePlugin):
    def on_page_context(self, context, page, config, **kwargs):
        # Check if the page has a custom image in its metadata
        if page.meta and ('image' in page.meta or 'og:image' in page.meta):
            # Mark this page to skip social plugin processing
            page.meta['social'] = {'cards': False}
            
            # Add debug information
            print(f"DEBUG: Disabled social cards for page: {page.title}")
            print(f"DEBUG: Image metadata: {page.meta.get('image') or page.meta.get('og:image')}")
        return context

    def on_config(config):
        return config