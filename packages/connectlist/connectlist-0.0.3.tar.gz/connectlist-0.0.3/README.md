# connectlist
## Table of Contents

- [Installation]
- [Features]
- [Publisher]
-[Usage]

## Installation

You can install the package using pip:

```bash
pip install connectlist

## Features
This module is used to  create contact book and then to add data,view data,search for data
##  Publisher
This module is produced by 'APS TECH INFO'
OWNER: APS TECH INFO
AUTHOR: SANTIN FABRIZIO AP
GMAIL: apstechinfo20@gmail.com
##usage 
from connectlist import *
'''the below contents can be replaced
book_name: by name of your contact book
name: name of the person
designation: by how you know them
phone-no: by the phone no
search : by thing to search '''
'''to create a new contact book'''
create('book_name')
''' to write in content in contact book'''
write('book_name','name','designation','phone-no')
'''to view content of contact book'''
view('book_name')
'''to search content of contact book'''
search('book_name','search')



