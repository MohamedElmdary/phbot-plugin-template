from typing import List

class Gui: pass
class GuiButton: pass
class GuiCheckBox: pass
class GuiLabel: pass
class GuiLineEdit: pass
class GuiList: pass
class GuiCombobox: pass

Widget = GuiButton | GuiCheckBox | GuiLabel | GuiLineEdit | GuiList | GuiCombobox

def init(ModuleName: str, TabName: str) -> Gui: pass

def createButton(gui: Gui, callback: str, text: str, x: float, y: float) -> GuiButton: pass
def createCheckBox(gui: Gui, callback: str, text: str, x: float, y: float) -> GuiCheckBox: pass
def createLabel(gui: Gui, text: str, x: float, y: float) -> GuiLabel: pass
def createLineEdit(gui: Gui, text: str, x: float, y: float, w: float, h: float) -> GuiLineEdit: pass
def createList(gui: Gui, x: float, y: float, w: float, h: float) -> GuiList: pass
def createCombobox(gui: Gui, x: float, y: float, w: float, h: float) -> GuiCombobox: pass

def setText(gui: Gui, widget: Widget, text: str) -> None: pass
def setChecked(gui: Gui, widget: Widget, checked: bool) -> None: pass
def text(gui: Gui, widget: Widget) -> str: pass
def destroy(gui: Gui, widget: Widget) -> None: pass
def move(gui: Gui, widget: Widget, x: float, y: float) -> None: pass
def isChecked(gui: Gui, widget: Widget) -> bool: pass
def clear(gui: Gui, widget: Widget) -> None: pass
def append(gui: Gui, widget: Widget, text: str) -> None: pass
def currentIndex(gui: Gui, widget: Widget) -> int: pass
def remove(gui: Gui, widget: Widget, text: str) -> None: pass
def removeAt(gui: Gui, widget: Widget, index: int) -> None: pass
def getItems(gui: Gui, widget: Widget) -> List[str]: pass
