import psycopg2

# 把 Heroku Postgres 的相關資訊寫到下列指令 (database, user, password, host, port)
conn = psycopg2.connect(
                database = "ddrqvb30kbrdsa",
                user = "lgectutbchtebn",
                password = "0dc73cbc693a2d36743e36248287bf4d90254a61205aa2f1647678ff5f4fdc75",
                host = "ec2-3-209-61-239.compute-1.amazonaws.com",
                port = "5432"
                )

print("Opened database successfully")
