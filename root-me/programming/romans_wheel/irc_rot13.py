import irc.client
import codecs


SERVER = 'irc.root-me.org'
PORT = 6667
CANDY = 'Candy'
ME = 'teQ'


class MyClient(irc.client.SimpleIRCClient):
    def run(self):
        self.connect(SERVER, PORT, ME)
        self.start()

    def on_welcome(self, conn, event):
        conn.privmsg(CANDY, '!ep3')

    def on_privmsg(self, conn, event):
        print(event.arguments[0])
        result = codecs.encode(event.arguments[0], 'rot13')
        conn.privmsg(CANDY, f'!ep3 -rep {result}')


if __name__ == '__main__':
    client = MyClient()
    client.run()
