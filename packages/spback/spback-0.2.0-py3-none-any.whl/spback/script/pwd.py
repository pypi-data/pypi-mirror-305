"""reset the password,

python manage.py script_file <username> <email> <password>
"""


def main():
    from .use_django import use_django

    use_django()

    import argparse

    from django.contrib.auth import get_user_model

    User = get_user_model()

    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="username")
    parser.add_argument("email", help="email")
    parser.add_argument("password", help="password")

    args = parser.parse_args()

    u = User.objects.get(username=args.username, email=args.email)
    u.set_password(args.password)
    u.save()

    print(
        "user: {username} reset, password: {pwd}".format(
            pwd=args.password, username=args.username
        )
    )


if __name__ == "__main__":
    main()
