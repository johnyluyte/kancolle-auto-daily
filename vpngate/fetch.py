# -*- coding: utf-8 -*-
import urllib2
import datetime
import subprocess
import traceback

TUNNELBLICK     = '/Applications/Tunnelblick.app/Contents/MacOS/Tunnelblick'
URL             = 'http://www.vpngate.net/api/iphone/'
COUNTRY         = 'Japan'
COUNT           = 0
SERVER_IP       = 0
BASE64          = ''
OUTPUT_FILE     = ''
FOUND_SERVER    = 'Found available Server, download it? (y/n) '
NO_MORE_SERVER  = 'There are no more results, leaving.'

COLOR = {
    'default' : '\033[m',
    'green'   : '\033[1;32m',
    'red'     : '\033[1;31m',
    'yellow'  : '\033[1;33m',
    'cyan'    : '\033[1;36m'
}


def check_field(field):
    """
    [0]HostName,        # vpn837620535
    [1]IP,              # 180.145.12.69
    [2]Score,           # 601344
    [3]Ping,            # 4
    [4]Speed,           # 66434823
    [5]CountryLong,     # Japan
    [6]CountryShort,    # JP
    [7]NumVpnSessions,  # 20
    [8]Uptime,          # 132061213
    [9]TotalUsers,      # 57322
    [10]TotalTraffic,   # 4049248061471
    [11]LogType,        # 2weeks
    [12]Operator,       # yu-ki-PC's owner
    [13]Message,        # (empty)
    [14]OpenVPN_ConfigData_Base64  # IyMjIyMjIyMjIyMjIyMjIy ...
    """
    global SERVER_IP
    SERVER_IP   = field[1]
    Score       = field[2]
    CountryLong = field[5]

    if CountryLong != COUNTRY:
        return False
    print( 'parsed ' + append_color(COUNT, 'cyan') + ' VPN server')
    print( "Score: {}, IP: {}".format(append_color(Score, 'yellow'), append_color(SERVER_IP, 'yellow')) )
    global BASE64
    BASE64 = field[14]
    return True


def parse_csv():
    print( "Parsing {}".format(URL) )
    print( "Searching for Country: " + append_color(COUNTRY, 'cyan') )
    global COUNT
    COUNT = 0
    try:
        myData = urllib2.urlopen(URL)
        for line in myData:
            if line.startswith('*') or line.startswith('#'):
                continue
            COUNT += 1
            if check_field(line.split(',')) is True:
                input_ = raw_input(FOUND_SERVER)
                if input_ == 'y':
                    return True
                elif input_ == 'n':
                    continue
                else:
                    input_ = raw_input(FOUND_SERVER)
    except:
        print( append_color( 'An exception occurred.', 'red' ) )
        traceback.print_exc()
        return False
    print(NO_MORE_SERVER)
    return False

def save_configure_file():
    configuration = BASE64.decode('base64')

    global OUTPUT_FILE
    OUTPUT_FILE = datetime.datetime.now().strftime('%m%d_%H%M@') + SERVER_IP + '.ovpn'

    with open(OUTPUT_FILE, 'w') as out_file:
        out_file.write(configuration)
    print( 'Configuration file created: \n' + append_color(OUTPUT_FILE, 'green') )


def append_color(msg, color='default'):
    return '{}{}{}'.format(COLOR[color], msg, COLOR['default'])

def exec_tunnelblink():
    print( 'Starting Tunnelblick...')
    subprocess.call([TUNNELBLICK, OUTPUT_FILE.strip()])

def main():
    if parse_csv() is False:
        return False
    save_configure_file()
    exec_tunnelblink()

if __name__ == '__main__':
    main()
