# myapp/context_processors.py
from .models import SiteSetting

def site_info(request):
    settings = SiteSetting.objects.all()
    
    # Create a dictionary for quick lookup by key
    settings_dict = {setting.key: setting.value for setting in settings}
    
    # Define variables using dictionary values with fallbacks
    site_name = settings_dict.get(SiteSetting.SITE_NAME, 'Default Site')
    logo_image = settings_dict.get(SiteSetting.LOGO_IMAGE)
    instagram_link = settings_dict.get(SiteSetting.INSTAGRAM_LINK)
    
    # Prepare the site data dictionary
    site_data = {
        'site_name': site_name,
        'logo_image': logo_image,
        'instagram_link': instagram_link,
    }
   
    return site_data



def site_icon(request):
    try:
        setting = SiteSetting.objects.get(key=SiteSetting.LOGO_IMAGE)
        logo_image_url = setting.image.url if setting.image else None
    except SiteSetting.DoesNotExist:
        logo_image_url = None
    
    return {
        'site_icon': logo_image_url
    }

