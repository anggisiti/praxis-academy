try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="anggisiti")

    curs = conn.cursor()

    nama = "anggi"
    umur = "17"
    query = f"update siswa set nama="anggang", umur=24 where nama='angga'"

    curs.execute(query)
    conn.commit()
    print("data berhasil diupdate")
except Exception as e:
    print(e)