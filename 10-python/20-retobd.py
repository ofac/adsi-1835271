import os
from twilio.rest import Client
import pymysql
from prettytable import PrettyTable
# Twilio 
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number   = 'whatsapp:+573103972370'
account_sid          = 'ACbe1b902dbf8f2918c80f6c9d931e2a98'
auth_token           = '32a1bf7bbbcad032f5c309b4ec7517a0'
client = Client(account_sid, auth_token)
# Base de Datos - - - - - - - - - - - - - - - - - - - - - - -
con = pymysql.connect(host='localhost', user='root', password='', db='universe')
# Menu - - - - - - - - - - - - - - - - - - - - - - -
def menu():
	t = PrettyTable(['MENU ( CRUD PYTHON & MYSQL )'])
	t.align['MENU ( CRUD PYTHON & MYSQL )'] = "l" 
	t.padding_width = 4
	t.add_row(['1) Insertar Planeta'])
	t.add_row(['2) Consultar todos los Planetas'])
	t.add_row(['3) Consultar Planeta'])
	t.add_row(['4) Modificar Planeta'])
	t.add_row(['5) Eliminar Planeta'])
	t.add_row(['6) Salir'])
	print(t)
	return input('> Ingrese una Opcion : ')
# Opcion 1 - - - - - - - - - - - - - - - - - - - - - - -
def opcion1():
	name    = input('> Nombre del Planeta : ')
	ordern  = int(input('> Orden del Planeta : '))
	moons   = int(input('> Numero de Lunas : '))
	with con.cursor() as cursor:
		sql = "INSERT INTO planets (id, name, ordern, moons) VALUES (DEFAULT, %s, %s, %s)"
		try:
			cursor.execute(sql, (name, ordern, moons))
			print('')
			print('Planeta Adicionado con Exito!')
			client.messages.create(body='Planeta '+ name +' Adicionado con Exito!', from_=from_whatsapp_number, to=to_whatsapp_number)
		except:
			print("Ops Error!")
	con.commit()
# Opcion 2 - - - - - - - - - - - - - - - - - - - - - - -
def opcion2():
	with con.cursor() as cursor:
		sql = 'SELECT * FROM planets'
		try:
			cursor.execute(sql)
			result = cursor.fetchall()
			print('')
			t = PrettyTable(['ID', 'NOMBRE', 'ORDEN', 'LUNAS'])
			for row in result:
				t.add_row([row[0], row[1], row[2], row[3]])
			print(t)
		except:
			print("Ops Error!")
	con.commit()
# Opcion 3 - - - - - - - - - - - - - - - - - - - - - - -
def opcion3():
	id = int(input('> ID del Planeta a Consultar : '))
	with con.cursor() as cursor:
		sql = 'SELECT * FROM planets WHERE id = %s'
		try:
			cursor.execute(sql, (id))
			result = cursor.fetchall()
			print('')
			t = PrettyTable(['ID', 'NOMBRE', 'ORDEN', 'LUNAS'])
			for row in result:
				t.add_row([row[0], row[1], row[2], row[3]])
			print(t)
		except:
			print("Ops Error!")
	con.commit()	
# Opcion 4 - - - - - - - - - - - - - - - - - - - - - - -
def opcion4():
	id = int(input('> ID del Planeta a Modificar : '))
	name   = input('> Nombre del Planeta : ')
	ordern = int(input('> Orden del Planeta : '))
	moons  = int(input('> Numero de Lunas : '))
	with con.cursor() as cursor:
		sql = "UPDATE planets SET name=%s, ordern=%s, moons=%s WHERE id = %s"
		try:
			cursor.execute(sql, (name, ordern, moons, id))
			client.messages.create(body='Planeta '+ name +' Modificado con Exito!', from_=from_whatsapp_number, to=to_whatsapp_number)
			print('Planeta Modificado con Exito!')
		except:
			print("Ops Error!")
	con.commit()		
# Opcion 5 - - - - - - - - - - - - - - - - - - - - - - -
def opcion5():
	id = int(input('> ID del Planeta a Eliminar : '))
	with con.cursor() as cursor:
		sql = "DELETE FROM planets WHERE id = %s"
		try:
			cursor.execute(sql, (id))
			print('Planeta Eliminado con Exito!')
		except:
			print("Ops Error!")
	con.commit()
# Opciones Menu - - - - - - - - - - - - - - - - - - - - - - -
preguntar = 1
opcion    = 0
while preguntar == 1:
	opcion = int(menu())
	os.system('clear')
	if opcion == 1:
		opcion1()
	elif opcion == 2:
		opcion2()
	elif opcion == 3:
		opcion3()
	elif opcion == 4:
		opcion4()
	elif opcion == 5:
		opcion5()			
	elif opcion == 6:
		preguntar = 0
		con.close()