import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Button, Stack, Textbox

page = pglet.page("index", no_window = True)

page.connection.clean()

#page.update(Page(title="Counter"))
page.title = "Counter"
page.update()


txtNum = Textbox(value = '0', align = 'right')

def on_click(e):
    try:
        count = int(page.connection.get_value(txtNum))

        #if we get here the number is int
        #page.send('set number errorMessage=""')

        if e.data == '+':
            page.connection.set_value(txtNum, count + 1)

        elif e.data =='-':
            page.connection.set_value(txtNum, count - 1)

    except ValueError:
        page.connection.send('set number errorMessage="Please enter a number"')

page.connection.add(
    Stack(horizontal = True, controls=[
        Button('-', onclick=on_click, data='-'),
        txtNum,
        Button('+', onclick=on_click, data='+'),
    ])
)

input("Press Enter to exit...")