from bottle import route, run, template, error

# в случае проблем - узнайте свой IP-адрес. 
# Для меня на Ubuntu 20.04 сработало это:
# ifconfig -a
# ip addr
# hostname -I | awk '{print $1}'
HOST = '10.40.63.209'


# чтение файла .json
with open('data.json', 'r') as file:
    data = file.read()


# собственно основная страница
@route('/')
def serve_homepage():
    return template('disp_table', rows = data)


# обработка не существующих страниц
@error(404)
def error404(error):
    return 'There is nothing... :('

# запускаем микроприложение!
run(host=HOST, port=8080)
