import irc.client
import math


SERVER = 'irc.root-me.org'
PORT = 6667
CANDY = 'Candy'
ME = 'teQ'


class MyClient(irc.client.SimpleIRCClient):
    def run(self):
        self.connect(SERVER, PORT, ME)
        self.start()

    def on_welcome(self, conn, event):
        conn.privmsg(CANDY, '!ep1')

    def on_privmsg(self, conn, event):
        if '/' in event.arguments[0]:
            a, b = map(int, event.arguments[0].split(' / '))
            result = round(math.sqrt(a) * b, 2)
            conn.privmsg(CANDY, f'!ep1 -rep {result}')
        else:
            print(event.arguments[0])



if __name__ == '__main__':
    client = MyClient()
    client.run()
