class User:
    def __init__(self, name):
        self.name = name
        self.is_logged = False

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged == True:
            function(args0)
    return wrapper
@is_authenticated_decorator
def create_blog_post(user):
    print(f"this is {user.name}'s new blog post.")

new_user = User("adrian")
new_user.is_logged = True
create_blog_post(new_user)
