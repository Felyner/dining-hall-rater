def index():
    return dict()

@auth.requires_login()
def home():
    return dict()

def user():
    return dict(form = auth())
