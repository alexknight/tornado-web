from tornado.web import RequestHandler
from methods import readdb


class IndexHandler(RequestHandler):
    def get(self):
        usernames = readdb.select_columns(table="users", column="username")
        one_user = usernames[0][0]
        self.render("index.html", user=one_user)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = readdb.select_table(table="users", column="*", condition="username", value=username)
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                self.set_secure_cookie(username, db_pwd, httponly=True, secure=True)
                self.write(username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no thi user.")
