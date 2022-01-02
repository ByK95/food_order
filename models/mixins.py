from app.shared.models import db


class ModelMixin(object):
    @classmethod
    def get(cls, *args, **kwargs):
        return cls.query.filter_by(*args, **kwargs).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
