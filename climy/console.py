import shutil


CINIT = '\033[{}m'
CEND = '\033[0m'
CBLOCK = '\033[{}m{}\033[0m'

CBOLD = '1'
CDIM = '2'
CITALIC = '3'
CURL = '4'
CSBLINK = '5'
CFBLINK = '6'
CSELECTED = '7'

CBLACK = '30'
CRED = '31'
CGREEN = '32'
CYELLOW = '33'
CBLUE = '34'
CVIOLET = '35'
Ccyan = '36'
CWHITE = '37'

CBLACKBG = '40'
CREDBG = '41'
CGREENBG = '42'
CYELLOWBG = '43'
CBLUEBG = '44'
CVIOLETBG = '45'
CcyanBG = '46'
CWHITEBG = '47'

CGREY = '90'
CRED2 = '91'
CGREEN2 = '92'
CYELLOW2 = '93'
CBLUE2 = '94'
CVIOLET2 = '95'
Ccyan2 = '96'
CWHITE2 = '97'

CGREYBG = '100'
CREDBG2 = '101'
CGREENBG2 = '102'
CYELLOWBG2 = '103'
CBLUEBG2 = '104'
CVIOLETBG2 = '105'
CcyanBG2 = '106'
CWHITEBG2 = '107'


cstyles = {
    'bold': '1',
    'dim': '2',
    'italic': '3',
    'underline': '4',
    'black': '30',
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'violet': '35',
    'cyan': '36',
    'white': '37',
    'bgblack': '40',
    'bgred': '41',
    'bggreen': '42',
    'bgyellow': '43',
    'bgblue': '44',
    'bgviolet': '45',
    'bgcyan': '46',
    'bgwhite': '47',
    'hblack': '90',
    'hred': '91',
    'hgreen': '92',
    'hyellow': '93',
    'hblue': '94',
    'hviolet': '95',
    'hcyan': '96',
    'hwhite': '97',
    'hbgblack': '100',
    'hbgred': '101',
    'hbggreen': '102',
    'hbgyellow': '103',
    'hbgblue': '104',
    'hbgviolet': '105',
    'hbgcyan': '106',
    'hbgwhite': '107',
}


def styled_text(text: str, style: str):
    splt = style.split(' ')
    ccode = ';'.join([cstyles.get(item, '39') for item in splt])
    return CBLOCK.format(ccode, text)


def sprint(text: str, style: str, align='<', end='\n'):
    stext = styled_text(text, style=style)
    if align == '>':
        tml_columns = shutil.get_terminal_size().columns
        size = len(text)
        stext = ' ' * (tml_columns - size) + stext
    elif align == '^':
        tml_columns = shutil.get_terminal_size().columns
        stext = stext.center(tml_columns)
    print(stext, end=end)
