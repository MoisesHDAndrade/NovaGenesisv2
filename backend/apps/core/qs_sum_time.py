import datetime
from datetime import timedelta, date

def calc_time(qs):
	entrada= []
	total = datetime.timedelta(0)

	for item in qs:
			#verifica se as entradas e saida sao diferente de none para evitar problemas 
			#com as entradas em branco do day off
			if item.time_in and item.time_out and item.time_in !=None and item.time_out !=None:
				datetimeFormat = '%H:%M:%S'
				diff = datetime.datetime.strptime(
				str(item.time_out), datetimeFormat) - datetime.datetime.strptime(str(item.time_in), datetimeFormat)
                
				# se tirou break subtrai 30 minutos e adiciona a lista
				# e se o tamanho da lista for maior que o query retira da lista enquanto for maior
				if item.break_time:
					parada = datetime.timedelta(minutes=30)
					break_time = diff - parada
					entrada.append(break_time)

					if len(entrada) > len(qs):
						entrada.pop()
					
				# se NAO tirou break adiciona a lista apenas a diferenca entre entrada e saida
				# e se o tamanho da lista for maior que o query retira da lista enquanto for maior		
				if not item.break_time:
					entrada.append(diff)
					if len(entrada) > len(qs):
						entrada.pop()

	contador = 0
	for index in qs:
		total += entrada[contador]
		contador +=1

	return total

def convert_time(duration):
	days, seconds = duration.days, duration.seconds
	hours = (days * 24) + (seconds // 3600)
	minutes = (seconds % 3600) // 60
	seconds = (seconds % 60)
	return hours, minutes,seconds

def total_time(time_text):
	time_converted = convert_time(time_text)
	horas = (f'{time_converted[0]}:{time_converted[1]:{time_converted[2]}}')
	return horas



def convert_time_sum(duration):
	days, seconds = duration.days, duration.seconds
	hours = (days * 24) + (seconds / 3600)
	seconds = (seconds % 60)
	return hours,seconds

#esta funcao nao retorna os numeros em minutos
def total_time_sum(time_text):
	time_converted = convert_time_sum(time_text)
	horas = (f'{time_converted[0]}:{time_converted[1]}')
	return horas



##################################################
#calcula horas do mjs
def sum_mjs(time_in, time_out, break_time):
	if time_in and time_out :
		datetimeFormat = '%H:%M:%S'
		diff = datetime.datetime.strptime(
		str(time_out), datetimeFormat) - datetime.datetime.strptime(str(time_in), datetimeFormat)
		if break_time:
			parada = datetime.timedelta(minutes=30)
			break_time = diff - parada
			return break_time

		if not break_time:
			return diff

def convert_seconds(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 





#################################################
#calcula horas do mjs vinda da api

def sum_mjs_api(time_in, time_out, break_time):
	if time_in and time_out :
		datetimeFormat = '%H:%M'
		diff = datetime.datetime.strptime(
		str(time_out), datetimeFormat) - datetime.datetime.strptime(str(time_in), datetimeFormat)
		if break_time:
			parada = datetime.timedelta(minutes=30)
			break_time = diff - parada
			return break_time

		if not break_time:
			return diff



def edit_sum_mjs_api(time_in, time_out, break_time): #PALEATIVO
	if time_in and time_out :
		datetimeFormat = '%H:%M:%S'
		diff = datetime.datetime.strptime(
		str(time_out), datetimeFormat) - datetime.datetime.strptime(str(time_in), datetimeFormat)
		if break_time:
			parada = datetime.timedelta(minutes=30)
			break_time = diff - parada
			return break_time

		if not break_time:
			return diff



def convert_or_create_last_second_digits(time_):
	try:
		if time_:
			return datetime.datetime.strptime(time_, '%H:%M:%S').time()
	except Exception as e:
		return datetime.datetime.strptime(time_, '%H:%M').time()
