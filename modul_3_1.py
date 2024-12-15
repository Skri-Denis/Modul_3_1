calls = 0
def count_calls():
    global calls # вызов глобальной переменной
    calls += 1 # счетчик

def string_info (string):
    count_calls() # вызов счетчика вызовов
    string = (len(string), string.upper (), string.lower()) # кортеж по условиям
    return string
def is_contains (string, list_to_search):
    count_calls() # вызов счетчика вызовов
    for i in range (len(list_to_search)):
        str_comp = False
        if string.lower() == list_to_search [i].lower():
            str_comp = True
    return str_comp

print(string_info('University'))
print(string_info('Montana'))
print(is_contains('Python', ['hON', 'PYTon', 'pytHoN']))  # Urban ~ urBAN
print(is_contains('Motorbyke', ['Byke', 'ankle', 'moto', 'BOOM']))  # No matches
print(calls)

