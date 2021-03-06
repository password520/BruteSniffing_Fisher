import Includes.menu as menu

commands = { 'create':
                {'posix' : 'touch', 'nt' : 'echo '' > '},
            'clear':
                {'posix' : 'clear', 'nt' : 'clr'},
            'copy':
                {'posix' : 'cp', 'nt' : 'copy'},
            'move':
                {'posix' : 'mv', 'nt' : 'rename'},
            'remove':
                {'posix' : 'rm', 'nt' : 'del'},
            'open':
                {'posix' : 'open', 'nt' : 'type'},
             'slash':
                {'posix' : '/', 'nt' : '\\'}
            }

directories, links = menu.construct_menus()
intro = directories[0]

#intro = {1: 'Web Attack', 2: 'Zip-file Bruteforce', 3 : 'Sniffing',  99 : 'Exit'}
#web_attack = {1 : 'Information Gathering', 2 : 'Bruteforce', 3 : 'Cloning', 4 : 'Fishing', 98 : 'Back', 99 : 'Exit'}
#links = [('Web Attack',1)]
#directories = [ intro, web_attack ]

proxychains = "Off"
tor = "Off" # activate only if proxychains is on
