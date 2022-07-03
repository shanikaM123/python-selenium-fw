import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def get_app_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_login_username():
        user_name = config.get('common info', 'username')
        return user_name

    @staticmethod
    def get_login_password():
        password = config.get('common info', 'password')
        return password
