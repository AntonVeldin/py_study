import sqlalchemy as sq

# Связь One to Many:
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html


class Album(Base):
    __tablename__ = 'album'
    id = sq.Column(sq.Integer, primary_key=True)
    tracks = relationship('Track', backref='album')

class Track(Base):
    __tablename__ = 'track'
    id = sq.Column(sq.Integer, primary_key=True)
    id_album = sq.Column(sq.Integer, sq.ForeignKey('album.id'))
