from functools import wraps


def authorization_required(func):
    @wraps(func)
    def wrapper(w, *args, **kwargs):
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        if username_input in w.PREMIUM_USERS and w.PREMIUM_USERS[username_input].password == password_input:
            return func(w, *args, **kwargs)
        else:
            return 'Wrong username or password'

    return wrapper


class User:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password


class Website:
    PREMIUM_USERS = {}

    def __init__(self):
        pass

    def activate_premium(self, full_name, username, password):
        user = User(full_name, username, password)
        self.PREMIUM_USERS.update({user.username: user})
        print('premium user activated for', user.username)

    @property
    def premium_content(self):
        content = ['premium_content1', 'premium_content2', 'premium_content3']
        return content


@authorization_required
def show_premium_content(web: Website):
    for i in web.premium_content:
        print(i)


if __name__ == '__main__':
    web = Website()
    web.activate_premium('Ali', 'Ali1234', 'Ali4321')
    show_premium_content(web)
