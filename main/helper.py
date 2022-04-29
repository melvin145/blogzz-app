import django
from django.utils.text import slugify

import string
import random
def generate_string(N):
    return ''.join(random.choices(string.ascii_uppercase+string.digits,k=N))

def generate_slug(text):
    
    new_slug=slugify(text)
    from main.models import Post
    if Post.objects.filter(slug=new_slug).exists():
        generate_slug(text+generate_slug(5))
    return new_slug