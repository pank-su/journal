import websocket

ws = websocket.WebSocket()

ws.connect("ws://localhost:8080/")

# Подключение к черепашке
# WARN: Нельзя использовать перенос строк и '
ws.send("""{"op": "subscribe","topic": "/turtle1/cmd_vel" }""")

print(ws.recv())
