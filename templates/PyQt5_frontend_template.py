# --------------------------------------------------------------
# 1. All IMPORTS
# -------------------------------------------------------------
"""
PyQt5 --> Framework: Haupt-Directory

QtCore --> Module: Sub-Directory von PyQt5 -> contains identifiers e.g. Alignment to structure our App
QtWidgets --> Module: Sub-Directory von PyQt5 -> provides a set of GUI elements and the main_window

PyQt 'Classes' im Module QtWidgets
--------------------------------------
QApplication -> Important Object: Allows us to create and execute our App
QWidget -> Important Object: Allows us to create a Main Window (Parent)

QLabel -> This is simple a Text(str)  object.
QPushButton -> This is a click/submit style Button object
QVBoxLayout -> This allows us to use VERTICAL ALIGNMENT

PyQt 'Methods' (functions in a class) :
--------------------------------------
.addWidget() -> Allows you to add an object to the layout to a column or a row
.setText() -> Change the Text of an existing object
.addLayout() -> Used to add Layouts together e.g. to add a column to a row
.setLayout() -> Used to set the final design to the Main Window
.show() / .hide() -> Allows you to show or hide an object

"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


# --------------------------------------------------------------
# 2. APP main SETTINGS: Create app and the main window
# --------------------------------------------------------------
app = QApplication([])
main_window = QWidget()

main_window.setWindowTitle("Random Word Maker")
main_window.resize(300, 200)

# ---------------------------------------------------------------
# 3. CREATE ALL WIDGETS needed in the App
# ----------------------------------------------------------------
title = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

# ----------------------------------------------------------------
# 4. APP DESIGN:
# a.) Create your Layout,
# b.) Add widgets (created above) to the Layout
# -----------------------------------------------------------------

# a.) Create Layout
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

# b.) Add Widgets to the layout
row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)


# -----------------------------------------------------------------
# 5. SET THE FINAL LAYOUT:
# a.) Add Design layouts from above to the master_layout
# b.) take master_layout and set it as final Layout to our main_window
# -----------------------------------------------------------------
# a.)
master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

# b.)
main_window.setLayout(master_layout)

# -----------------------------------------------------------------
# 6. Create Functions: for the EventHandling in step 7
# -----------------------------------------------------------------


def function():
    pass


# -----------------------------------------------------------------
# 7. EVENTS:
# -----------------------------------------------------------------


button1.clicked.connect(function)

# ------------------------------------------------------------------
# 8. SHOW and EXECUTE your App
# ------------------------------------------------------------------

main_window.show()
app.exec_()

