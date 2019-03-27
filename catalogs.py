'''python
import mysql.connector
cnx=mysql.connector.connect(user='root',password='unvisible777',host='127.0.0.1',database='shop')
cursor=cnx.cursor()

user_query = ('select * from users')

cursor.execute(user_query)

print('Sifarişlərə baxmaq üçün istifadəçi nömrəsini seçin:')


for u in cursor:
    print('%d - %s %s' % (u[0:3]))
    
user = int(input('No: '))

orders_query = ('select * from orders inner join users on orders.user = users.id where orders.user=%d'%user) 

cursor.execute(orders_query)

for o in cursor:
    print(o)
   
'''
