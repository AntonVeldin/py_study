import sqlalchemy as sq

# Связь One to Many:

class Album(Base):
    __tablename__ = 'album'
    id = sq.Column(sq.Integer, primary_key=True)
    tracks = relationship('Track', backref='album')

class Track(Base):
    __tablename__ = 'track'
    id = sq.Column(sq.Integer, primary_key=True)
    id_album = sq.Column(sq.Integer, sq.ForeignKey('album.id'))
