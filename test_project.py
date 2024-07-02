# users nomli tabelga Pythonda User classi yozasiz va ushbu classda save(),get_users, 
# get_user,delete_user(),update_user() metodlari bo'lsin va bu metod ishlaganda bazadayam o'zgarishlar hosil bo'lsin
import psycopg2

def user():
    with psycopg2.connect(database='school', user='postgres', password='1111') as conn:
            curr=conn.cursor()
    
    def create_table():
        nonlocal conn
        nonlocal curr

        our_query="""create table if not exists users (id serial primary key, first_name varchar(100) not null, last_name  varchar(100) not null, username  varchar(100) not null, email  varchar(100) not null, age int not null, is_active boolean not null)"""
        curr.execute(our_query)
        conn.commit()
        print('Table created succesfully')
    
    def insert_data():
        nonlocal conn
        nonlocal curr
        insert_query="""INSERT INTO users(first_name, last_name, username, email, age, is_active) VALUES ('Colene', 'Sorrel', 'csorrel0', 'csorrel0@dyndns.org', 12, true),
        ('Angelique', 'Thackwray', 'athackwray1', 'athackwray1@1und1.de', 17, false),
        ('Andi', 'Bootman', 'abootman2', 'abootman2@bing.com', 45, false),
        ('Mikel', 'Pulster', 'mpulster3', 'mpulster3@Brinetvibes.com', 34, true);
          """

        curr.execute(insert_query)
        conn.commit()
        print(' Inserted succesfully')

    def get_users():
         nonlocal conn
         nonlocal curr

         select_query="""Select * from users where is_active=false"""
         curr.execute(select_query)
         rows=curr.fetchall()
         print(list(rows))
    
    def get_user():
        nonlocal conn
        nonlocal curr

        select_a_query="""Select * from  users where id=2"""
        curr.execute(select_a_query)
        row=curr.fetchone()
        print(row)

    def update_user():
        nonlocal conn
        nonlocal curr
        update_query="""update users set email='andi_bootma78@gmail.com' WHERE id=3"""
        curr.execute(update_query)
        conn.commit()
        print(' Updated succesfully')

    
    def delete_user():
        nonlocal conn
        nonlocal curr
        delete_query="""delete from users  WHERE id=4"""
        curr.execute(delete_query)
        conn.commit()
        print(' Deleted succesfully')

    return create_table, insert_data,get_users, get_user,update_user, delete_user

create_table, insert_data,get_users, get_user,update_user, delete_user=user()
print(create_table())
print(insert_data())
print(get_users())
print(get_user())
print(update_user())
print(delete_user())




         
