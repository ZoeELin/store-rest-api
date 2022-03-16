from db import db


class TransformModel(db.Model):
    __tablename__ = 'my_url'

    long_url = db.Column(db.String())
    short_url = db.Column(db.String(), primary_key=True)
    visit_times = db.Column(db.Integer)

    @classmethod
    def find_by_long_url(cls, url):
        return cls.query.filter_by(long_url=url).first()

    @classmethod
    def find_by_short_url(cls, url):
        return cls.query.filter_by(short_url=url).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


# class VisitorModel(db.Model):
#     __tablename__ = 'visitor'