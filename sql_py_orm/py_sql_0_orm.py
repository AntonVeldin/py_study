import sqlalchemy as sq
import psycopg2
import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# доступ к паролю
with open("token.json", 'r') as f:
    js = json.loads(f.read())
db_name = js["database"]["name"]
db_name_2 = "mydb_2"
db_user = js["database"]["user"]
db_pass = js["database"]["pass"]

# формируем адрес для подключения
db = 'postgresql://' + db_user + ':' + db_pass + '@localhost:5432/' + db_name_2
# db = 'postgresql+psycorg2://' + db_user + ':' + db_pass + '@localhost:5432/' + db_name


# создаем обобщенный класс, который будет определять, что все наследуемые классы будут в одной схеме
Base = declarative_base()

engine = sq.create_engine(db)
Session = sessionmaker(blind=engine)


# Создаем модель ORM:
class Author(Base):
    __tablename__ = 'authors'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    albums = relationship('Albums', back_populates='authors')
    # для доступа к автору из альбомов, мы должны использовать команду ".authors",
    # при этом в альбомах уже есть authors. Ссылается на существущий атрибут в классе.


class Album(Base):
    __tablename__ = 'albums'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    tracks = relationship('Tracks', backref='albums')
    # обращаемся "tracks.albums", но в треках нет albums. Создаает атрибут.
    published = sq.Column(sq.Date)
    id_authors = sq.Column(sq.Integer, sq.ForeignKey('authors.id'))
    authors = relationship(Author)


class Genre(Base):
    __tablename__ = 'genre'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    tracks = relationship('Tracks', secondary='track_to_genre', back_populates='genres')


track_to_genre = sq.Table(
    'track_to_genre', Base.metadata,
    sq.Column('genre.id', sq.Integer, sq.ForeignKey('genre.id')),
    sq.Column('track.id', sq.Integer, sq.ForeignKey('tracks.id')),
)


class Track(Base):
    __tablename__ = 'tracks'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    duration = sq.Column(sq.Integer)
    genres = relationship(Genre, secondary=track_to_genre, back_populates='tracks')
    id_album = sq.Column(sq.Integer, sq.ForeignKey('albums.id'))


# Создание всех таблиц:
if __name__ == '__main__':
    Base.metadata.create_all(engine)









#
#
#
#
#
#
#
#
#
#
#
# class Album(Base):
#     __tablename__ = 'albums'
#     id = sq.Column(sq.Integer, primary_key=True)
#     title = sq.Column(sq.String)
#     tracks = relationship('Track', back_populates='albums')
#     published = sq.Column(sq.Date)
#
#     id_artists = sq.Column(sq.Integer, sq.ForeignKey('authors.id'))
#     # artist = relationship(Artist, back_populates='albums')
#
# class Track(Base):
#     __tablename__ = 'track'
#     id = sq.Column(sq.Integer, primary_key=True)
#     title = sq.Column(sq.String)
#     duration = sq.Column(sq.Integer)
#     # genres = relationship(Genre, secondary=track_to_genre,back_populates='tracks')
#     id_album = sq.Column(sq.Integer, sq.ForeignKey('album.id'))
#     album = relationship(Album, back_populates='tracks')
