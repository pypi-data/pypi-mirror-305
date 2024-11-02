#! /usr/bin/env python3


import imapdedup

options = [
    "-s", "imap.fastmail.com",
    "-u", "quentinsf@fastmail.com",
    "-w", 'bxmgjjdb86ld4p9s',  # App password
    "-x",
    # "-v",
    # "-l",
    # "-n",
]

mboxes = [
    # 'INBOX',
    'Archives/2005',
    'Archives/2006',
]

imapdedup.process(*imapdedup.get_arguments(options + mboxes))

