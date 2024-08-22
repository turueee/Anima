import sqlite3 as sq


def dataconecter(query):
    with sq.connect('Animedata.db') as ani:
        cur = ani.cursor()
        cur.execute(query)
    return cur


def mexadatas(genr):
    id_gen = dataconecter(f"SELECT id_genre FROM id_genre WHERE genre='{genr}'").fetchone()[0]
    data = dataconecter(f"SELECT rusname,engname FROM about_anime WHERE id_genre={id_gen}")
    return (dict(data.fetchall()))

def all_genres():
    genres = dataconecter("SELECT genre FROM id_genre").fetchall()
    gen=[i[0] for i in genres]
    return(gen)

def anistudio(studioname):
    id = dataconecter(f"SELECT id_anime FROM about_anime WHERE engname = '{studioname}'").fetchone()[0]
    studio = dataconecter(f"SELECT studio FROM studio WHERE id_anime={id}").fetchall()
    studios = [i[0] for i in studio]
    return studios


def aniinfo(studioname):
    info = dataconecter(
        f"SELECT director,ruslic, oppening, logo FROM about_anime WHERE engname = '{studioname}'"
    ).fetchone()
    placeholders = ['rezh', 'lic', 'music', 'logo']
    return (dict(zip(placeholders, info)))


def infcharacters(studioname):
    id = dataconecter(f"SELECT id_anime FROM about_anime WHERE engname = '{studioname}'").fetchone()[0]
    characters = dataconecter(f"SELECT name,information FROM character WHERE id_anime={id}").fetchall()
    return (dict(characters))


def photocharacters(studioname):
    id = dataconecter(f"SELECT id_anime FROM about_anime WHERE engname = '{studioname}'").fetchone()[0]
    photocharacter = dataconecter(f"SELECT name,photo FROM character WHERE id_anime={id}").fetchall()
    return (dict(photocharacter))


def groopphoto(studioname):
    groop = dataconecter(f"SELECT rusname FROM about_anime WHERE engname = '{studioname}'").fetchone()[0]
    return (groop)


def add_information_to_about_anime_database(rusnam, engnam, direct, russlic, id_genr):
    dataconecter(
        f"INSERT INTO about_anime ('rusname','engname','director','ruslic','id_genre') VALUES ('{rusnam}','{engnam}','{direct}','{russlic}',{id_genr})")


def add_information_to_id_genre_database(id_genr, genr):
    dataconecter(f"INSERT INTO id_genre VALUES ({id_genr},'{genr}')")


def add_information_to_character_database(nam, inform, id_anim):
    dataconecter(f"INSERT INTO id_genre ('name','information','id_anime') VALUES ('{nam}','{inform}',{id_anim})")


def add_information_to_studio_database(studi, id_anim):
    dataconecter(f"INSERT INTO studio VALUES ('{studi}',{id_anim})")
