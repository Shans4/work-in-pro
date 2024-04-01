class UserService:
    def _check_user_exists(self, db, **kwargs):
        sql = "SELECT id FROM users WHERE username = ?;"
        user_id = db.cursor.execute(sql, (kwargs['username'],))
        if user_id is None:
            return False
        return True

    def create(self, db, **kwargs):
        if not self._check_user_exists(db, username=kwargs['username']):
            print('Такой пользователь уже есть')
            return
        sql = "INSERT INTO users(username) VALUES (?)"
        db.cursor.execute(sql, (kwargs['username'],))
        db.connection.commit()
        print('Добавили пользователя', kwargs['username'])

    def read(self, db, **kwargs):
        # kwargs['all'] = True
        pass

    def update(self, db, **kwargs):
        pass

    def delete(self, db, **kwargs):
        pass
