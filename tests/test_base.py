import unittest


from app.manage import app
from app.shared.models import db
from app.models.user import User


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.db = db
        self.client = app.test_client()
        self.app.config.update({"TESTING": True})
        with app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()

    def run(self, result=None):
        with app.app_context():
            super().run(result=result)


class UserTestCase(BaseTestCase):
    def test_lookup(self):
        participant = User(name="Bayram", surname="Kaya", email="a@a.com")
        db.session.add(participant)
        db.session.commit()
        participants = User.query.all()
        assert participant in participants
        print("NUMBER OF ENTRIES:", len(participants))

if __name__ == "__main__":
    unittest.main()
