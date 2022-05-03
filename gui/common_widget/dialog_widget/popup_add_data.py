# Project: wsl_app_v4_0
# FileName: popup_add_data.py
# Main Python Code for GUI popups - Add Location, Add Tour

########################################################################################################################
import sys
from typing import Optional

import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QApplication, QDialogButtonBox, QPushButton

########################################################################################################################
from src.models import LocationLists, AddLocation


class AddLocationDialog(QDialog):
    def __init__(self,
                 title,
                 left=10,
                 top=10,
                 width=520,
                 height=400,
                 prev_selected_continent: Optional[str] = None,
                 prev_selected_country: Optional[str] = None,
                 prev_selected_region: Optional[str] = None,
                 parent=None):

        self.prev_selected_continent: Optional[str] = prev_selected_continent
        self.prev_selected_country: Optional[str] = prev_selected_country
        self.prev_selected_region: Optional[str] = prev_selected_region

        # Calls constructor for QDialog
        QDialog.__init__(self, parent=parent)

        # Call constructor to get previously selected location

        # Set Title of the QDialog.
        self.setWindowTitle(title)

        # Set Geometry of the QDialog.
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setGeometry(left, top, width, height)

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Set this custom widget's parent, if it was passed to the constructor function (not None).
        if not (parent is None):
            self.setParent(parent)

        # Create Vertical Layout Box.
        self.layout = QVBoxLayout()

        # Create Horizontal Layouts.
        self.hlayout_continent = QHBoxLayout()
        self.hlayout_country = QHBoxLayout()
        self.hlayout_region = QHBoxLayout()
        self.hlayout_city = QHBoxLayout()

        # Continent Label and Combobox
        self.hlayout_continent.addWidget(QLabel("Continent:"))
        self.cb_continent = PyQt5.QtWidgets.QComboBox()
        self.hlayout_continent.addWidget(self.cb_continent)
        self.cb_continent.setFixedWidth(200)
        self.hlayout_continent.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_continent)

        # Country Label and Line Edit
        self.hlayout_country.addWidget(QLabel("Country:"))
        self.cb_country = PyQt5.QtWidgets.QComboBox()
        self.hlayout_country.addWidget(self.cb_country)
        self.cb_country.setFixedWidth(200)
        self.line_country = PyQt5.QtWidgets.QLineEdit()
        self.hlayout_country.addWidget(self.line_country)
        self.line_country.setFixedWidth(200)

        self.layout.addLayout(self.hlayout_country)

        # Region Label and Line Edit
        self.hlayout_region.addWidget(QLabel("Region:"))

        self.cb_region = PyQt5.QtWidgets.QComboBox()
        self.hlayout_region.addWidget(self.cb_region)
        self.cb_region.clear()
        # self.cb_region.addItems()
        self.cb_region.setFixedWidth(200)

        self.line_region = PyQt5.QtWidgets.QLineEdit()
        self.hlayout_region.addWidget(self.line_region)
        self.line_region.setFixedWidth(200)

        self.layout.addLayout(self.hlayout_region)

        # City Label and Line Edit
        self.hlayout_city.addWidget(QLabel("City:"))
        self.line_city = PyQt5.QtWidgets.QLineEdit()
        self.hlayout_city.addWidget(self.line_city)
        self.line_city.setFixedWidth(200)
        self.hlayout_city.addWidget(QLabel(''))
        self.layout.addLayout(self.hlayout_city)

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(q_btn)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.ButtonBox)

        self.setLayout(self.layout)

        self.on_startup()

        self.connect_slots()

    # This defines the event handlers for everything.
    def connect_slots(self):
        self.cb_continent.currentIndexChanged.connect(self.slot_cb_continent_on_index_change)
        self.cb_country.currentIndexChanged.connect(self.slot_cb_country_on_index_change)

    # This setups up everything at the first startup.
    def on_startup(self):
        # If a Continent been selected from the previous tab add it on startup.
        if self.prev_selected_continent is None or self.prev_selected_continent == "":
            self.cb_continent.addItems([''] + LocationLists.return_continents())
        else:
            self.cb_continent.addItem(self.prev_selected_continent)

        # If a Country has been selected from the previous tab add it on startup
        if self.prev_selected_country is not None and self.prev_selected_country != "":
            self.cb_country.addItem(self.prev_selected_country)
        else:
            self.slot_cb_continent_on_index_change()

        # If a Country has been selected from the previous tab add it on startup
        if self.prev_selected_region is not None and self.prev_selected_region != "":
            self.cb_region.addItem(self.prev_selected_region)
        else:
            self.slot_cb_country_on_index_change()

    def slot_cb_continent_on_index_change(self):
        self.cb_country.clear()
        return_country_inst = LocationLists(entered_continent=self.cb_continent.currentText())
        self.cb_country.addItems([''] + return_country_inst.return_countries_from_continents())

    def slot_cb_country_on_index_change(self):
        self.cb_region.clear()
        return_region_inst = LocationLists(entered_continent=self.cb_continent.currentText(),
                                           entered_country=self.cb_country.currentText())
        self.cb_region.addItems([''] + return_region_inst.return_regions_from_countries())

########################################################################################################################

class AddTourType(QDialog):
    def __init__(self,
                 title,
                 left=10,
                 top=10,
                 width=520,
                 height=400,
                 parent=None):
        # Calls constructor for QDialog
        QDialog.__init__(self, parent=parent)

        # Set Title of the QDialog.
        self.setWindowTitle(title)

        # Set Geometry of the QDialog.
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.setGeometry(left, top, width, height)

        # Disable x button to force "yes" or "no" click
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # Disable help button
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        # Set this custom widget's parent, if it was passed to the constructor function (not None).
        if not(parent is None):
            self.setParent(parent)

        # Create Vertical Layout Box.
        self.layout = QVBoxLayout()

        # Create Horizontal Layouts.
        self.vlayout_tour = QVBoxLayout()

        # Tour Gender CheckBox
        self.chkbox_men = PyQt5.QtWidgets.QCheckBox()
        self.chkbox_men.setText("Men")
        self.chkbox_women = PyQt5.QtWidgets.QCheckBox()
        self.chkbox_women.setText("Women")
        self.vlayout_tour.addWidget(self.chkbox_men)
        self.vlayout_tour.addWidget(self.chkbox_women)

        # Tour Year Label and Combobox
        self.vlayout_tour.addWidget(QLabel("Tour Year:"))
        self.line_year = PyQt5.QtWidgets.QLineEdit()
        self.vlayout_tour.addWidget(self.line_year)
        self.line_year.setFixedWidth(200)
        self.vlayout_tour.addWidget(QLabel(''))

        # Continent Label and Combobox
        self.vlayout_tour.addWidget(QLabel("Tour Type:"))
        self.line_tourtype = PyQt5.QtWidgets.QLineEdit()
        self.vlayout_tour.addWidget(self.line_tourtype)
        self.line_tourtype.setFixedWidth(200)
        self.vlayout_tour.addWidget(QLabel(''))
        self.layout.addLayout(self.vlayout_tour)

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.ButtonBox = QDialogButtonBox(q_btn)
        self.ButtonBox.accepted.connect(self.accept)
        self.ButtonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.ButtonBox)

        self.setLayout(self.layout)

########################################################################################################################

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    win = AddLocationDialog(title='Add a New Location')
    win.show()
    sys.exit(win.exec_())

