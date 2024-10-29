
from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Placeholder, Input, Label, TextArea, Header,Footer
from textual.screen import Screen, ModalScreen
from textual.containers import Container, Horizontal, VerticalScroll, Grid
from .confmscn import Confirm_Screen
from textual import events, on, work
import pandas as pd
from .paxModule import *
from .DFTable import DataFrameTable
from .ti_labels_iccid import create_pdf
from .serialNoValidator import SerialNoValidator
from .paxStoreChecker import PaxStoreChecker

class Scan_serials(ModalScreen):

    """SERIAL NUMBER INPUT"""
    BINDINGS = [("escape", "app.pop_screen", "Pop screen"),("0000", "", "Del item"),("BKSPC", "", "Del item")]


    def __init__(self):
        self.order_of_input = [] # list of all input in order of input
        self.serialNoList = [] # list of serialnumbers in paxstore
        self.copySerialNoList = self.serialNoList
        self.detailsList = []
        self.serialValidator = SerialNoValidator()  # Create an instance of the validator
        self.not_inPaxStore = [] # list of all terminals not found in PaxStore
        self.ops = apiPaxFunctions()
        super().__init__()
    
    def compose(self) -> ComposeResult:
        
        yield Header(name='PaxTools')
        yield Static("SCAN OR TYPE SERIAL NUMBER:")
        yield Input(placeholder="S/N",validators=[self.serialValidator])
        yield Footer()
    
    @on(Input.Submitted)
    @work
    async def update_serial_list(self):
        user_input = self.query_one(Input)
        self.order_of_input.append(user_input.value) # add all input to order of input list
        serialNo = user_input.value
        self.mount(Static(str(user_input.value)))
        if user_input.value == "BKSPC":
            self.serialNoList.pop()
            self.serialNoList.pop()
        if ":" in user_input.value:
            self.serialNoList.pop()
            self.app.bell()
        if user_input.value == "0000":
            self.disabled = True
            self.app.bell()
            self.order_of_input.pop()
            check = PaxStoreChecker(self.order_of_input)
            check.check_for_terminal()
            if check.not_in_paxStore:
                if await self.app.push_screen_wait(Confirm_Screen(f"These Terminals are not registered: {check.not_in_paxStore}\nDo you want to register now? ")):
                    add = await self.ops.createTerminals(check.not_in_paxStore)
                    self.app.notify(str(add))
            self.app.notify("these terminals are in the paxstore"+str(self.detailsList))
            self.app.notify("these are not:"+str(self.not_inPaxStore))
            self.app.notify("original order:"+str(self.order_of_input))
            
        user_input.clear()



        
class scan_v2(App):

    def on_mount(self) -> None:
         self.push_screen(Scan_serials())
         

if __name__ == "__main__":
    app = scan_v2()
    app.run()


        

        
