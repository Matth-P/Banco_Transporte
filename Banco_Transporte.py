import sqlite3

nome = input("Local:")
Hr = str(input("hora:"))
Mn = str(input("minuto:"))
transporte = input("transporte:")

hora = Hr + "h" + Mn

banco = sqlite3.connect('banco_Transporte.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pontos_rota3(nome text, hora not null, transporte text)")

cursor.execute("INSERT INTO pontos_rota3 VALUES('"+nome+"','"+hora+"','"+transporte+"')")

banco.commit()
