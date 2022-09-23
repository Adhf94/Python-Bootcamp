import smtplib

my_email = "email"
#Se creo una contraseña para APPS para poder acceder al servidor smtp de google.
password = "password"
#conexion al servidor de google
#Simplficando la conexion para con el context manager para no tener que cerrarlo manualmente
#connection = smtplib.SMTP("smtp.gmail.com", port=587)
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #start transport layer security
    connection.starttls()
    #login a el sls
    connection.login(user=my_email, password=password)
    #Send the email. Para el sujeto del mensaje se usa Sujeto: antes de todo, y luego para el mensaje, dos \n\n
    connection.sendmail(from_addr=my_email, to_addrs="dummie@yahoo.com",
                        msg="Subject:Hello\n\nThis is the context manager try")
    #close
    #connection.close()
