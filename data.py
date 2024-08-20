import sqlite3 as sq


def dataconecter(query):
    with sq.connect('Animedata.db') as ani:
        cur = ani.cursor()
        cur.execute(query)
    return cur


def mexadatas():
    data = dataconecter("SELECT rusname,engname FROM about_anime")
    return (dict(data.fetchall()))


def anistudio(studioname):
    id = dataconecter(f"SELECT id_anime FROM about_anime WHERE rusname = '{studioname}'").fetchone()[0]
    studio = dataconecter(f"SELECT studio FROM studio WHERE id_anime={id}").fetchall()
    studios = [i[0] for i in studio]
    return studios


def aniinfo(studioname):
    info = dataconecter(
        f"SELECT director,ruslic, oppening, logo FROM about_anime WHERE rusname = '{studioname}'"
    ).fetchone()
    placeholders = ['rezh', 'lic', 'music', 'logo']
    return (dict(zip(placeholders, info)))


def infcharacters(studioname):
    id = dataconecter(f"SELECT id_anime FROM about_anime WHERE rusname = '{studioname}'").fetchone()[0]
    characters = dataconecter(f"SELECT name,information FROM character WHERE id_anime={id}").fetchall()
    return (dict(characters))


def photocharacters(studioname):
    id = dataconecter(f"SELECT id_anime FROM about_anime WHERE rusname = '{studioname}'").fetchone()[0]
    photocharacter = dataconecter(f"SELECT name,photo FROM character WHERE id_anime={id}").fetchall()
    return (dict(photocharacter))


def groopphoto(studioname):
    groop = dataconecter(f"SELECT engname FROM about_anime WHERE rusname = '{studioname}'").fetchone()[0]
    return(groop)

