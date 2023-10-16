from dao.user_dao import UserDao
class UserService:
    def find_by_name(self, name):
        return UserDao().find_by_name(name)