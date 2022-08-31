try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="anggisiti")

    nama = "anggang"
    query = f"delete from siswa where nama="{nama}'"

    curs.execute(query)
    data = 