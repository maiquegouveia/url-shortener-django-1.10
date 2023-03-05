import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    Klass = instance.__class__
    if Klass.objects.filter(shortcode=new_code).exists():
        return create_shortcode()
    return new_code