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


# One to One
class Album(Base):
    __tablename__ = 'album'
    id = sq.Column(sq.Integer, primary_key=True)
    track = relationship('Track', uselist=False)

# Many to Many
class Genre(Base):
    __tablename__ = 'genre'
    id = sq.Column(sq.Integer, primary_key=True)
    tracks = relationship('Tracks', secondary='track_to_genre')

track_to_genre = sq.Table(
    'track_to_genre', Base.metadata,
    sq.Column('genre.id', sq.Integer, sq.ForeignKey('genre.id')),
    sq.Column('track.id', sq.Integer, sq.ForeignKey('tracks.id')),
)

class Track(Base):
    __tablename__ = 'tracks'
    id = sq.Column(sq.Integer, primary_key=True)
    genres = relationship(Genre, secondary=track_to_genre)
