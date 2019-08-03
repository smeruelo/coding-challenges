import irc.client
from base64 import b64decode


SERVER = 'irc.root-me.org'
PORT = 6667
CANDY = 'Candy'
ME = 'teQ'


class MyClient(irc.client.SimpleIRCClient):
    def run(self):
        self.connect(SERVER, PORT, ME)
        self.start()

    def on_welcome(self, conn, event):
        conn.privmsg(CANDY, '!ep2')

    def on_privmsg(self, conn, event):
        print(event.arguments[0])
        result = b64decode(event.arguments[0]).decode()
        conn.privmsg(CANDY, f'!ep2 -rep {result}')


if __name__ == '__main__':
    client = MyClient()
    client.run()
