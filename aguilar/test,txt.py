import libreria
assert(libreria.validar_entero(12)==True)
assert(libreria.validar_entero("hola")==False)
assert(libreria.validar_entero(-12)==False)
assert(libreria.validar_entero(False)==False)
assert(libreria.validar_entero(13.5)==False)
print("validar_entero => ok")
assert(libreria.validar_rango(3,1,8)==True)
assert(libreria.validar_rango(3,8,1)==False)
assert(libreria.validar_rango(9,1,8)==False)
assert(libreria.validar_rango("HOLA",1,8)==False)
assert(libreria.validar_rango(-4,-11,8)==False)
print("validar_rango => ok")
assert(libreria.validar_nombre("MIGUEL")==True)
assert(libreria.validar_nombre(12)==False)
assert(libreria.validar_nombre(-15)==False)
assert(libreria.validar_nombre(True)==False)
assert(libreria.validar_nombre("12345")==False)
print("validar_nombre => ok")
assert(libreria.validar_tamano("PEQUEÑO")==True)
assert(libreria.validar_tamano(12.5)==False)
assert(libreria.validar_tamano("grande")==True)
assert(libreria.validar_tamano(True)==False)
assert(libreria.validar_tamano("AZUL")==False)
assert(libreria.validar_tamano(152)==False)
assert(libreria.validar_tamano("grandote")==False)
assert(libreria.validar_tamano("mediano")==True)
print("validar_tamano => ok")
assert(libreria.validar_real(13.5)==True)
assert(libreria.validar_real(-13.5)==False)
assert(libreria.validar_real("HOLA")==False)
assert(libreria.validar_real("11.4")==False)
assert(libreria.validar_real(13)==False)
assert(libreria.validar_real(True)==False)
print("validar_real => ok")
assert(libreria.validar_tipo("contratado")==True)
assert(libreria.validar_tipo("MIGUEL")==False)
assert(libreria.validar_tipo(13.5)==False)
assert(libreria.validar_tipo("contratado")==True)
assert(libreria.validar_tipo(12)==False)
assert(libreria.validar_tipo("empleado")==True)
assert(libreria.validar_tipo(True)==False)
print("validar_tipo => ok")
assert(libreria.validar_ruc(52325695741)==True)
assert(libreria.validar_ruc("12345643567")==False)
assert(libreria.validar_ruc("HOLA")==False)
assert(libreria.validar_ruc(523256941)==False)
assert(libreria.validar_ruc(5232569235741)==False)
assert(libreria.validar_ruc(12)==False)
assert(libreria.validar_ruc(-2313442342424)==False)
assert(libreria.validar_ruc(13.53545)==False)
assert(libreria.validar_ruc(52325)==False)
print("validar_ruc => ok")
assert(libreria.validar_juego("mario")==True)
assert(libreria.validar_juego(13)==False)
assert(libreria.validar_juego("VEINTE")==False)
assert(libreria.validar_juego(True)==False)
assert(libreria.validar_juego("donkey")==False)
assert(libreria.validar_juego("pes")==True)
assert(libreria.validar_juego(13.54)==False)
assert(libreria.validar_juego(-13)==False)
print("validar_juego => ok")
assert(libreria.validar_dni(75461630)==True)
assert(libreria.validar_dni(461630)==False)
assert(libreria.validar_dni(756461630)==False)
assert(libreria.validar_dni("HOLA")==False)
assert(libreria.validar_dni(4612.6330)==False)
assert(libreria.validar_dni(75431630)==True)
assert(libreria.validar_dni(True)==False)
assert(libreria.validar_dni("75461630")==False)
print("validar_dni => ok")
assert(libreria.validar_ciclo("PRIMERO")==True)
assert(libreria.validar_ciclo("MIGUEL")==False)
assert(libreria.validar_ciclo(123)==False)
assert(libreria.validar_ciclo("tercero")==True)
assert(libreria.validar_ciclo("FIEL")==False)
assert(libreria.validar_ciclo(True)==False)
assert(libreria.validar_ciclo("QUINTO")==True)
assert(libreria.validar_ciclo("decimoprimero")==False)
assert(libreria.validar_ciclo("octavo")==True)
assert(libreria.validar_ciclo(98765)==False)
assert(libreria.validar_ciclo(12.54)==False)
assert(libreria.validar_ciclo("DECIMO")==True)
assert(libreria.validar_ciclo(-23)==False)
print("validar_ciclo => ok")
assert(libreria.validar_tar("2345 4231 2334 3245")==True)
assert(libreria.validar_tar("2345 4231 2334")==False)
assert(libreria.validar_tar("2345/4231/2334/3245")==False)
assert(libreria.validar_tar("2345 4231 HOLA 3245")==False)
assert(libreria.validar_tar("2345 HOLA 2334 3245")==False)
assert(libreria.validar_tar("23442")==False)
assert(libreria.validar_tar(1234343)==False)
print("validar_tar => ok")
assert(libreria.validar_clave(2345)==True)
assert(libreria.validar_clave("hola")==False)
assert(libreria.validar_clave(132343)==False)
assert(libreria.validar_clave(123)==False)
assert(libreria.validar_clave(-322)==False)
print("validar_clave => ok")
assert(libreria.validar_tel("074 346578")==True)
assert(libreria.validar_tel("074 34657")==False)
assert(libreria.validar_tel("054 34657")==False)
assert(libreria.validar_tel("074/34657")==False)
assert(libreria.validar_tel(7434657)==False)
assert(libreria.validar_tel("074 3461257")==False)
assert(libreria.validar_tel("0074 34657")==False)
assert(libreria.validar_tel("074-34657")==False)
print("validar_tel => ok")
assert(libreria.validar_celular(935880051)==True)
assert(libreria.validar_celular("935880051")==False)
assert(libreria.validar_celular(835880051)==False)
assert(libreria.validar_celular(880051)==False)
assert(libreria.validar_celular(93588005231)==False)
assert(libreria.validar_celular("HOLA")==False)
print("validar_celular => ok")
assert(libreria.validar_mess("DICIEMBRE")==True)
assert(libreria.validar_mess(67)==False)
assert(libreria.validar_mess("enero")==True)
assert(libreria.validar_mess("ENE")==False)
assert(libreria.validar_mess(True)==False)
assert(libreria.validar_mess("MARZO")==True)
assert(libreria.validar_mess(989898)==False)
assert(libreria.validar_mess("34")==False)
assert(libreria.validar_mess("octubre")==True)
assert(libreria.validar_mess(-34)==False)
assert(libreria.validar_mess("hola")==False)
assert(libreria.validar_mess("JULIO")==True)
print("validar_mess => ok")
assert(libreria.validar_correo("miguel@gmail.com")==True)
assert(libreria.validar_correo("miguel@gmailcom")==False)
assert(libreria.validar_correo("miguelgmail.com")==False)
assert(libreria.validar_correo("miguel@hotmail.com")==False)
assert(libreria.validar_correo("hola")==False)
assert(libreria.validar_correo(12654)==False)
assert(libreria.validar_correo(True)==False)
print("validar_correo => ok")
assert(libreria.validar_hotmail("miguel@hotmail.com")==True)
assert(libreria.validar_hotmail("miguel@hotmailcom")==False)
assert(libreria.validar_hotmail("miguel@otmail.com")==False)
assert(libreria.validar_hotmail("miguel")==False)
assert(libreria.validar_hotmail(12234)==False)
assert(libreria.validar_hotmail(False)==False)
print("validar_hotmail => ok")
assert(libreria.validar_placa("h3j-243")==False)
assert(libreria.validar_placa("GTY-243")==False)
assert(libreria.validar_placa("H2J-243")==True)
assert(libreria.validar_placa("K3J/243")==False)
assert(libreria.validar_placa("JOSE")==False)
assert(libreria.validar_placa(-2343)==False)
assert(libreria.validar_placa(243)==False)
print("validar_placa => ok")
assert(libreria.validar_color("AZUL")==True)
assert(libreria.validar_color("POLO")==False)
assert(libreria.validar_color(165)==False)
assert(libreria.validar_color("verde")==True)
assert(libreria.validar_color(True)==False)
assert(libreria.validar_color("AZU")==False)
assert(libreria.validar_color("AMARILLO")==True)
assert(libreria.validar_color(-123)==False)
assert(libreria.validar_color(121)==False)
assert(libreria.validar_color("negro")==True)
assert(libreria.validar_color("HOLA")==False)
print("validar_color => ok")
assert(libreria.validar_estado("EBRIO")==True)
assert(libreria.validar_estado("JOSE")==False)
assert(libreria.validar_estado(5672)==False)
assert(libreria.validar_estado("54GF3")==False)
assert(libreria.validar_estado("sano")==True)
assert(libreria.validar_estado(987654321)==False)
print("validar_estado => ok")
assert(libreria.validar_codigo("324567b")==True)
assert(libreria.validar_codigo("3245673")==False)
assert(libreria.validar_codigo("ABCDEFG")==False)
assert(libreria.validar_codigo("324567AX")==False)
assert(libreria.validar_codigo(3245673)==False)
assert(libreria.validar_codigo(True)==False)
print("validar_codigo => ok")
assert(libreria.validar_tipo_de_pago("EFECTIVO")==True)
assert(libreria.validar_tipo_de_pago(123)==False)
assert(libreria.validar_tipo_de_pago("HOLA")==False)
assert(libreria.validar_tipo_de_pago("tarjeta")==True)
assert(libreria.validar_tipo_de_pago("treinta")==False)
assert(libreria.validar_tipo_de_pago(-123)==False)
assert(libreria.validar_tipo_de_pago(True)==False)
print("validar_tipo_de_pago => ok")
assert(libreria.validar_rang(2.3,0.0,20.0)==True)
assert(libreria.validar_rang(2.3,20.0,0.0)==False)
assert(libreria.validar_rang("HOLA",20.0,0.0)==False)
assert(libreria.validar_rang(2,20.0,0.0)==False)
assert(libreria.validar_rang(13.6,12.4,0.6)==False)
assert(libreria.validar_rang(-12.4,0.0,-12.0)==False)
print("validar_rang => ok")
assert(libreria.validar_fecha("2000-12-12")==True)
assert(libreria.validar_fecha("2020-13-12")==False)
assert(libreria.validar_fecha("2020/12/12")==False)
assert(libreria.validar_fecha("hola-13-12")==False)
assert(libreria.validar_fecha("miguel")==False)
assert(libreria.validar_fecha(3335)==False)
assert(libreria.validar_fecha(True)==False)
print("validar_fecha => ok")
