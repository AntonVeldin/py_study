import datetime

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
Session = sessionmaker(bind=engine)


# Создаем модель ORM:
class Author(Base):
    __tablename__ = 'author'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String)
    albums = relationship('Album', back_populates='author')
    # для доступа к автору из альбомов, мы должны использовать команду ".author",
    # при этом в альбомах уже есть author. Ссылается на существущий атрибут в классе.


class Album(Base):
    __tablename__ = 'album'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    track = relationship('Track', backref='album')
    # обращаемся "tracks.album", но в треках нет album. Создаает атрибут.
    published = sq.Column(sq.Date)
    id_author = sq.Column(sq.Integer, sq.ForeignKey('author.id'))
    author = relationship(Author)

    def init_publish(self, pub_date=None):
        if pub_date is not None:
            self.published = pub_date
        else:
            self.published = datetime.date.today()
        session.commit()


class Genre(Base):
    __tablename__ = 'genre'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    track = relationship('Track', secondary='track_to_genre', back_populates='genre')


track_to_genre = sq.Table(
    'track_to_genre', Base.metadata,
    sq.Column('genre.id', sq.Integer, sq.ForeignKey('genre.id')),
    sq.Column('track.id', sq.Integer, sq.ForeignKey('track.id')),
)


class Track(Base):
    __tablename__ = 'track'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String)
    duration = sq.Column(sq.Integer)
    genre = relationship(Genre, secondary=track_to_genre, back_populates='track')
    id_album = sq.Column(sq.Integer, sq.ForeignKey('album.id'))


if __name__ == '__main__':
    # Создание всех таблиц:
    # Base.metadata.create_all(engine)
    session = Session()
#     art1 = Author(name='Best Bundle')
#     session.add(art1)
#     session.commit()
#     date_arl1 = {
#         'Album 1': [
#             {'name': 'Track 1_1', 'dur': 60},
#             {'name': 'Track 1_2', 'dur': 50},
#             {'name': 'Track 1_3', 'dur': 45}
#         ],
#         'Album 2': [
#             {'name': 'Track 2_1', 'dur': 60},
#             {'name': 'Track 2_2', 'dur': 50},
#             {'name': 'Track 2_3', 'dur': 45}
#         ]
#     }
#
#     for title, tracks in date_arl1.items():
#         alb = Album(title=title, author=art1)
#         session.add(alb)
#         for tr in tracks:
#             tr = Track(title=tr.get('name'), duration=tr.get('dur'), album=alb)
#             # tr.id_album = alb (либо так)
#             x = session.add(tr)
#     session.commit()
#
# # в дебаггере  смотрим переменные,
# # art1
# # art1.albums
# # art1.name
# # art1.id
# # alb.id
# # tr.album
# # tr.album.title

# Корректировка записей в БД:
    session.query(Album).filter(Album.title == 'Album 2').update({
        'published': datetime.date(year=2020, month=1, day=1)
    })
    session.commit()

# Заполнение промежуточной таблицы с жанрами:
#     genres = ['rock', 'classic', 'jazz']
#     inst_genres = []
#     for g in genres:
#         inst_genres.append(Genre(title=g))
#         print(inst_genres)
#     session.add_all(inst_genres)
#     for track in session.query(Track).filter(Track.id_album == 2).all():
#         track.genre.extend(inst_genres)
#     session.commit()

    q = session.query(Author).filter(Author.name == 'Best Bundle')
    artist = q.first()
    # artist.albums[1].track[0].genre[0].title  в дебаггере
    # [g.title for g in artist.albums[1].track[0].genre] в дебаггере
    # session.query(Genre).first().track в дебаггере

    # alb1 = artist.albums[0]
    # alb1.init_publish()
    # alb1.published
    # datetime.date(2021, 2, 23) в дебаггере

    session.commit()