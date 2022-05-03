########################################################################################################################
# Project: wsl_app_v4_0
# FileName: main_widget.py
# Main Python Code for GUI
########################################################################################################################
import sys
import re

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog

# from gui.common_widget.dialog_widget.popup_add_data import AddLocationDialog, AddTourType, AddEventType, SurferToHeat
from gui.common_widget.dialog_widget.popup_add_data import AddLocationDialog, AddTourType
from gui.main.ui_to_py.wsl_analytics_ui_v2_0 import Ui_Form
from src.models import AddTour, AddLocation, AddSurfer, LocationLists, TourLists


########################################################################################################################


class MainWidget(QMainWindow, Ui_Form):
    def __init__(self):
        # Call the constructor for the inherited QWidget class.
        QMainWindow.__init__(self)

        # Instances for AddLocationDialog
        add_loc_inst = AddLocation()

        # This function is inherited from the Ui_Form class.
        self.setupUi(self)

        # Call the connect_slots function to connect all the event-handlers to functions in this class.
        self.connect_slots()

        # Call to setup everything on the gui.
        self.on_startup()

    div_dict = {'input_error': ['Input Error', '=', 60],
                'wipe_out_wav': ['Wipe Out', '~', 60]}

    # Check for float
    def check_for_float(self,
                        check_string_for_float: str) -> float:

        okay_characters = "0123456789."
        if all([char in okay_characters for char in check_string_for_float]):
            return float(check_string_for_float)
        else:
            float_not_entered = (f"\n"
                                 f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                                 f"\nYou're confused. This should be a number (decimals are okay)."
                                 f"\nEntered Value: {check_string_for_float}")
            print(float_not_entered)
            raise ValueError()

    # Check for float
    def check_for_int(self,
                      check_string_for_int: str) -> float:

        okay_characters = "0123456789."
        if all([char in okay_characters for char in check_string_for_int]):
            return int(check_string_for_int)
        else:
            int_not_entered = (f"\n"
                               f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                               f"\nYou're confused. This should be an integer."
                               f"\nEntered Value: {check_string_for_int}")
            print(int_not_entered)
            raise ValueError()

    # This defines the event handlers for everything on the Main Widget
    def connect_slots(self):
        # Slots for Add Event Tab
        self.cb_addevent_year.currentIndexChanged.connect(self.slot_cb_addevent_year_on_index_change)
        self.cb_addevent_continent.currentIndexChanged.connect(self.slot_cb_addevent_continent_on_index_change)
        self.cb_addevent_country.currentIndexChanged.connect(self.slot_cb_addevent_country_on_index_change)
        self.cb_addevent_region.currentIndexChanged.connect(self.slot_cb_addevent_region_on_index_change)

        self.pb_addevent_newtour.clicked.connect(self.slot_pb_addevent_newtour_clicked)
        self.pb_addevent_clear.clicked.connect(self.slot_pb_addevent_clear_clicked)
        self.pb_addevent_submit.clicked.connect(self.slot_pb_addevent_submit_clicked)

        # # Slots for Add Heat Tab
        # self.cb_addheat_year.currentIndexChanged.connect(self.slot_cb_addheat_year_on_index_change)
        # self.cb_addheat_tour.currentIndexChanged.connect(self.slot_cb_addheat_tour_on_index_change)
        #
        # self.pb_addheat_newround.clicked.connect(self.slot_pb_addheat_newround_clicked)
        # self.pb_addheat_clear.clicked.connect(self.slot_pb_addheat_clear_clicked)
        # self.pb_addheat_submit.clicked.connect(self.slot_pb_addheat_submit_clicked)
        # self.pb_addheat_surfers.clicked.connect(self.slot_pb_addheat_surfers_clicked)
        #
        # # Slots for Add Round Results Tab
        # self.cb_addresults_year.currentIndexChanged.connect(self.slot_cb_addresults_year_on_index_change)
        # self.cb_addresults_tour.currentIndexChanged.connect(self.slot_cb_addresults_tour_on_index_change)
        # self.cb_addresults_event.currentIndexChanged.connect(self.slot_cb_addresults_round_on_index_change)
        # self.cb_addresults_round.currentIndexChanged.connect(self.slot_cb_addresults_heat_on_index_change)
        # self.cb_addresults_heat.currentIndexChanged.connect(self.slot_cb_addresults_surfer_on_index_change)
        #
        # self.pb_addresults_clear.clicked.connect(self.slot_pb_addresults_clear_clicked)
        # self.pb_addresults_submit.clicked.connect(self.slot_pb_addresults_submit_clicked)
        #
        # Slots for Add Break Tab
        self.cb_addbreak_continent.currentIndexChanged.connect(self.slot_cb_addbreak_continent_on_index_change)
        self.cb_addbreak_country.currentIndexChanged.connect(self.slot_cb_addbreak_country_on_index_change)

        self.pb_addbreak_clear.clicked.connect(self.slot_pb_addbreak_clear_clicked)
        self.pb_addbreak_newloc.clicked.connect(self.slot_pb_addbreak_newloc_clicked)
        self.pb_addbreak_submit.clicked.connect(self.slot_pb_addbreak_submit_clicked)

        # Slots for Add Surfer Tab
        self.cb_addsurfer_continent.currentIndexChanged.connect(self.slot_cb_addsurfer_continent_on_index_change)
        self.cb_addsurfer_hcontinent.currentIndexChanged.connect(self.slot_cb_addsurfer_hcontinent_on_index_change)
        self.cb_addsurfer_hcountry.currentIndexChanged.connect(self.slot_cb_addsurfer_hcountry_on_index_change)
        self.cb_addsurfer_hregion.currentIndexChanged.connect(self.slot_cb_addsurfer_hregion_on_index_change)

        self.pb_addsurfer_clear.clicked.connect(self.slot_pb_addsurfer_clear_clicked)
        self.pb_addsurfer_newloc.clicked.connect(self.slot_pb_addsurfer_newloc_clicked)
        self.pb_addsurfer_submit.clicked.connect(self.slot_pb_addsurfer_submit_clicked)

    # Everything that should happen when the app has started up
    def on_startup(self):
        # Add Event Tab
        self.cb_addevent_continent.addItems([''] + LocationLists.return_continents())
        self.cb_addevent_year.addItems([''] + TourLists.return_tour_years())

        # Add Heat Tab

        # Add Round Results Tab
        # Add Tour Years

        # Add Break Tab
        self.cb_addbreak_continent.addItems([''] + LocationLists.return_continents())

        # Add Surfer Tab
        self.cb_addsurfer_continent.addItems([''] + LocationLists.return_continents())
        self.cb_addsurfer_hcontinent.addItems([''] + LocationLists.return_continents())

    ####################################################################################################################
    # Add Event Tab

    def slot_cb_addevent_year_on_index_change(self):
        self.cb_addevent_tourtype.clear()
        return_tour_name_inst = TourLists(entered_year=self.cb_addevent_year.currentText())
        self.cb_addevent_tourtype.addItems([''] + return_tour_name_inst.return_tour_name_from_year())

    def slot_cb_addevent_continent_on_index_change(self):
        self.cb_addevent_country.clear()
        return_country_inst = LocationLists(entered_continent=self.cb_addevent_continent.currentText())
        self.cb_addevent_country.addItems([''] + return_country_inst.return_countries_from_continents())

    def slot_cb_addevent_country_on_index_change(self):
        self.cb_addevent_region.clear()
        return_region_inst = LocationLists(entered_continent=self.cb_addevent_continent.currentText(),
                                           entered_country=self.cb_addevent_country.currentText())
        self.cb_addevent_region.addItems([''] + return_region_inst.return_regions_from_countries())

    def slot_cb_addevent_region_on_index_change(self):
        self.cb_addevent_break.clear()
        return_break_name_inst = LocationLists(entered_continent=self.cb_addevent_continent.currentText(),
                                               entered_country=self.cb_addevent_country.currentText(),
                                               entered_region=self.cb_addevent_region.currentText())
        self.cb_addevent_break.addItems(([''] + return_break_name_inst.return_breaks_from_regions()))

    def slot_pb_addevent_newtour_clicked(self):
        dialog = AddTourType(title="Add a Tour Type to database.")

        if dialog.exec() == QDialog.Accepted:

            entered_tour_type = dialog.line_tourtype.text()

            entered_year = dialog.line_year.text() if not \
                dialog.line_year.text() == "" else None
            if entered_year is not None:
                entered_year = self.check_for_int(check_string_for_int=entered_year)

            # Grab Male or Female
            if dialog.chkbox_men.isChecked():
                if dialog.chkbox_women.isChecked():
                    print('Dude, we have to separate by gender because of stuff like muscle density to keep it fair.')
                    raise ValueError
                entered_gender = 'Men'
            elif dialog.chkbox_women.isChecked():
                entered_gender = 'Women'
            else:
                print("Bruh, you have to choose a gender for this to work.")
                raise ValueError

            # Enter a New Tour
            inst = AddTour(entered_year=entered_year,
                           entered_gender=entered_gender,
                           entered_tour_type=entered_tour_type)
            inst.add_new_tour()

    def slot_pb_addevent_clear_clicked(self):
        self.cb_addevent_year.clear()
        self.cb_addevent_year.addItems([''] + TourLists.return_tour_years())
        self.cb_addevent_tourtype.clear()
        self.line_addevent_name.clear()
        self.line_addevent_stop.clear()
        self.line_addevent_open.clear()
        self.line_addevent_close.clear()
        self.cb_addevent_continent.clear()
        self.cb_addevent_continent.addItems([''] + LocationLists.return_continents())
        self.cb_addevent_country.clear()
        self.cb_addevent_region.clear()
        self.cb_addevent_break.clear()

    def slot_pb_addevent_submit_clicked(self):

        entered_tour_name = self.cb_addevent_tourtype.currentText()
        entered_event_name = self.line_addevent_name.text()

        entered_stop_nbr = self.line_addevent_stop.text() if not \
            self.line_addevent_stop.text() == "" else None
        if entered_stop_nbr is not None:
            entered_stop_nbr = self.check_for_int(check_string_for_int=entered_stop_nbr)

        entered_continent = self.cb_addevent_continent.currentText()
        entered_country = self.cb_addevent_country.currentText()
        entered_region = self.cb_addevent_region.currentText()
        entered_break_name = self.cb_addevent_break.currentText()
        entered_open_date = self.line_addevent_open.text()
        entered_close_date = self.line_addevent_close.text()

        # Enter a New Event
        inst = AddTour(entered_tour_name=entered_tour_name,
                       entered_event_name=entered_event_name,
                       entered_stop_nbr=entered_stop_nbr,
                       entered_continent=entered_continent,
                       entered_country=entered_country,
                       entered_region=entered_region,
                       entered_break_name=entered_break_name,
                       entered_open_date=entered_open_date,
                       entered_close_date=entered_close_date)
        inst.add_new_event()

        self.slot_pb_addevent_clear_clicked()

    ####################################################################################################################
    # Add Heat Tab

    ####################################################################################################################
    # Add Results Tab

    ####################################################################################################################
    #  Add Break Tab

    # Change Country List when a Continent is selected
    def slot_cb_addbreak_continent_on_index_change(self):
        self.cb_addbreak_country.clear()
        return_country_inst = LocationLists(entered_continent=self.cb_addbreak_continent.currentText())
        self.cb_addbreak_country.addItems([''] + return_country_inst.return_countries_from_continents())

    # Change Region List when a Country is selected
    def slot_cb_addbreak_country_on_index_change(self):
        self.cb_addbreak_region.clear()
        return_region_inst = LocationLists(entered_continent=self.cb_addbreak_continent.currentText(),
                                           entered_country=self.cb_addbreak_country.currentText())
        self.cb_addbreak_region.addItems([''] + return_region_inst.return_regions_from_countries())

    # Open a PopUp to enter new location when The Add Location Button is selected
    # noinspection PyMethodMayBeStatic
    def slot_pb_addbreak_newloc_clicked(self):
        dialog = AddLocationDialog(title="Add a location to the database.",
                                   prev_selected_continent=self.cb_addbreak_continent.currentText(),
                                   prev_selected_country=self.cb_addbreak_country.currentText(),
                                   prev_selected_region=self.cb_addbreak_region.currentText(),
                                   )

        if dialog.exec() == QDialog.Rejected:
            dialog.close()

        if dialog.exec() == QDialog.Accepted:
            continent = dialog.cb_continent.currentText()

            entered_continent = dialog.cb_continent.currentText()

            # If country was entered into line edit use that value. Else use combobox.
            entered_country = None
            country_in_line_edit = dialog.line_country.text() is None or dialog.line_country.text() == ''
            country_in_combobox = dialog.cb_country.currentText() is None or dialog.cb_country.currentText() == ''
            if not country_in_line_edit:
                entered_country = dialog.line_country.text()
                add_country_inst = AddLocation(entered_continent=entered_continent,
                                               entered_country=entered_country)
                add_country_inst.add_new_country()
            elif country_in_combobox:
                print(f"\nSelect or enter a country.\n")
            else:
                entered_country = dialog.cb_country.currentText()

            # If region was entered into line edit use that value. Else use combobox.
            entered_region = None
            region_in_line_edit = dialog.line_region.text() is None or dialog.line_region.text() == ''
            region_in_combobox = dialog.cb_region.currentText() is None or dialog.cb_region.currentText() == ''
            if not region_in_line_edit:
                entered_region = dialog.line_region.text()
                add_region_inst = AddLocation(entered_continent=entered_continent,
                                              entered_country=entered_country,
                                              entered_region=entered_region)
                add_region_inst.add_new_region()
            elif region_in_combobox:
                print(f"\nSelect or enter a region.\n")
            else:
                entered_region = dialog.cb_region.currentText()

            # Grab City from line edit
            if dialog.line_city.text() is None or dialog.line_city == '':
                print(f"\nEnter a city.\n")
            else:
                entered_city = dialog.line_city.text()
                add_city_inst = AddLocation(entered_continent=entered_continent,
                                            entered_country=entered_country,
                                            entered_region=entered_region,
                                            entered_city=entered_city)
                add_city_inst.add_new_city()
            dialog.close()

    # Clear the form when the Clear button is checked
    def slot_pb_addbreak_clear_clicked(self):
        self.cb_addbreak_continent.clear()
        self.cb_addbreak_continent.addItems([''] + LocationLists.return_continents())
        self.cb_addbreak_country.clear()
        self.cb_addbreak_region.clear()
        self.line_addbreak_break.clear()
        self.check_addbreak_ability_green.setChecked(0)
        self.check_addbreak_ability_yellow.setChecked(0)
        self.check_addbreak_ability_red.setChecked(0)
        self.check_addbreak_burn_green.setChecked(0)
        self.check_addbreak_burn_yellow.setChecked(0)
        self.check_addbreak_burn_red.setChecked(0)
        self.check_addbreak_beach.setChecked(0)
        self.check_addbreak_point.setChecked(0)
        self.check_addbreak_reef.setChecked(0)
        self.check_addbreak_river.setChecked(0)
        self.check_addbreak_sandbar.setChecked(0)
        self.check_addbreak_jetty.setChecked(0)
        self.check_addbreak_eng.setChecked(0)
        self.line_addbreak_clean.clear()
        self.line_addbreak_blown.clear()
        self.line_addbreak_small.clear()

    # When the Submit button is clicked all data should be assigned a variable, prepared, and inserted into mysal db
    def slot_pb_addbreak_submit_clicked(self):

        # Assign Location Infor
        entered_continent = self.cb_addbreak_continent.currentText()
        entered_country = self.cb_addbreak_country.currentText()
        entered_region = self.cb_addbreak_region.currentText()
        entered_break_name = self.line_addbreak_break.text()

        # Grab Break Type based on which types are checked
        break_type_list = []
        if self.check_addbreak_beach.isChecked():
            break_type_list.append('Beach')
        if self.check_addbreak_point.isChecked():
            break_type_list.append('Point')
        if self.check_addbreak_reef.isChecked():
            break_type_list.append('Reef')
        if self.check_addbreak_river.isChecked():
            break_type_list.append('River')
        if self.check_addbreak_sandbar.isChecked():
            break_type_list.append('Sandbar')
        if self.check_addbreak_jetty.isChecked():
            break_type_list.append('Jetty')
        if self.check_addbreak_eng.isChecked():
            break_type_list.append('Engineered')

        # Turn List of break types into a string for mysql table
        # If break type is unknown assign None
        entered_break_type = ", ".join(break_type_list) if not ", ".join(break_type_list) == "" else None

        # Assign Reliability and if unknown assign None
        entered_reliability = self.cb_addbreak_reliability.currentText() if not \
            self.cb_addbreak_reliability.currentText() == "" else None

        # Assign ability level
        ability_list = []
        if self.check_addbreak_ability_green.isChecked():
            ability_list.append('Beginner')
        if self.check_addbreak_ability_yellow.isChecked():
            ability_list.append('Intermediate')
        if self.check_addbreak_ability_red.isChecked():
            ability_list.append('Advanced')

        # Turn List of abilities into a string for mysql table
        # If ability is unknown assign None
        entered_ability = ", ".join(ability_list) if not ", ".join(ability_list) == "" else None

        # Assign shoulder burn
        shoulder_burn_list = []
        if self.check_addbreak_burn_green.isChecked():
            shoulder_burn_list.append('Light')
        if self.check_addbreak_burn_yellow.isChecked():
            shoulder_burn_list.append('Medium')
        if self.check_addbreak_burn_red.isChecked():
            shoulder_burn_list.append('Exhausting')

        # Turn List of shoulder burn into a string for mysql table
        # If shoulder burn is unknown assign None
        entered_shoulder_burn = ", ".join(shoulder_burn_list) if not ", ".join(shoulder_burn_list) == "" else None

        # Assign Surfability Values
        entered_clean = self.line_addbreak_clean.text() if not \
            self.line_addbreak_clean.text() == "" else None
        entered_blown = self.line_addbreak_blown.text() if not \
            self.line_addbreak_blown.text() == '' else None
        entered_too_small = self.line_addbreak_small.text() if not \
            self.line_addbreak_small.text() == '' else None

        if entered_clean is not None:
            entered_clean = self.check_for_float(check_string_for_float=entered_clean)
        if entered_blown is not None:
            entered_blown = self.check_for_float(check_string_for_float=entered_blown)
        if entered_too_small is not None:
            entered_too_small = self.check_for_float(check_string_for_float=entered_too_small)

        # Enter a New Break
        add_new_break = AddLocation(entered_continent=entered_continent,
                                    entered_country=entered_country,
                                    entered_region=entered_region,
                                    entered_break_name=entered_break_name,
                                    entered_break_type=entered_break_type,
                                    entered_reliability=entered_reliability,
                                    entered_ability=entered_ability,
                                    entered_shoulder_burn=entered_shoulder_burn,
                                    entered_clean=entered_clean,
                                    entered_blown_out=entered_blown,
                                    entered_too_small=entered_too_small)

        add_new_break.add_new_break()

        # Clear Form on Submit
        self.slot_pb_addbreak_clear_clicked()

    ####################################################################################################################
    # Add Surfer Tab

    # Change Rep Country List when a Rep Continent is Selected
    def slot_cb_addsurfer_continent_on_index_change(self):
        self.cb_addsurfer_country.clear()
        return_country_inst = LocationLists(entered_continent=self.cb_addsurfer_continent.currentText())
        self.cb_addsurfer_country.addItems([''] + return_country_inst.return_countries_from_continents())

    # Change Home Country List when a Home Continent is Selected
    def slot_cb_addsurfer_hcontinent_on_index_change(self):
        self.cb_addsurfer_hcountry.clear()
        return_country_inst = LocationLists(entered_continent=self.cb_addsurfer_hcontinent.currentText())
        self.cb_addsurfer_hcountry.addItems([''] + return_country_inst.return_countries_from_continents())

    # Change Home Region List when a Home Country is selected
    def slot_cb_addsurfer_hcountry_on_index_change(self):
        self.cb_addsurfer_hregion.clear()
        return_region_inst = LocationLists(entered_continent=self.cb_addsurfer_hcontinent.currentText(),
                                           entered_country=self.cb_addsurfer_hcountry.currentText())
        self.cb_addsurfer_hregion.addItems([''] + return_region_inst.return_regions_from_countries())

    # Change Home City List When a Home Region is Selected
    def slot_cb_addsurfer_hregion_on_index_change(self):
        self.cb_addsurfer_hcity.clear()
        return_city_inst = LocationLists(entered_continent=self.cb_addsurfer_hcontinent.currentText(),
                                         entered_country=self.cb_addsurfer_hcountry.currentText(),
                                         entered_region=self.cb_addsurfer_hregion.currentText())
        self.cb_addsurfer_hcity.addItems([''] + return_city_inst.return_cities_from_regions())

    # Clear the form when the Clear button is checked
    def slot_pb_addsurfer_clear_clicked(self):
        self.line_addsurfer_firstname.clear()
        self.line_addsurfer_lastname.clear()
        self.check_addsurfer_goofy.setChecked(0)
        self.check_addsurfer_regular.setChecked(0)
        self.cb_addsurfer_continent.clear()
        self.cb_addsurfer_continent.addItems([''] + LocationLists.return_continents())
        self.cb_addsurfer_country.clear()
        self.line_addsurfer_bday.clear()
        self.line_addsurfer_ht.clear()
        self.line_addsurfer_wt.clear()
        self.line_addsurfer_firstseason.clear()
        self.line_addsurfer_firsttour.clear()
        self.cb_addsurfer_hcontinent.clear()
        self.cb_addsurfer_hcontinent.addItems([''] + LocationLists.return_continents())
        self.cb_addsurfer_hcountry.clear()
        self.cb_addsurfer_hregion.clear()
        self.cb_addsurfer_hcity.clear()
        self.check_addsurfer_male.setChecked(0)
        self.check_addsurfer_female.setChecked(0)

    # New Location Button Clicked
    def slot_pb_addsurfer_newloc_clicked(self):
        self.slot_pb_addbreak_newloc_clicked()
    
    # Submit Button Clicked
    def slot_pb_addsurfer_submit_clicked(self):

        # Grab Male or Female
        if self.check_addsurfer_male.isChecked():
            if self.check_addsurfer_female.isChecked():
                print('Dude, we have to separate by gender because of stuff like muscle density to keep it fair.')
                raise ValueError
            entered_gender = 'Men'
        elif self.check_addsurfer_female.isChecked():
            entered_gender = 'Women'
        else:
            print("Bruh, you have to choose a gender for this to work.")
            raise ValueError

        entered_first_name = self.line_addsurfer_firstname.text()
        entered_last_name = self.line_addsurfer_lastname.text()

        # Determine Stance
        if self.check_addsurfer_regular.isChecked():
            entered_stance = 'Regular'
        elif self.check_addsurfer_goofy.isChecked():
            entered_stance = 'Goofy'
        else:
            entered_stance = None

        entered_rep_continent = self.cb_addsurfer_continent.currentText()
        entered_rep_country = self.cb_addsurfer_country.currentText()

        entered_birthday = self.line_addsurfer_bday.text()
        if self.line_addsurfer_bday.text() == '' or self.line_addsurfer_bday.text() is None:
            entered_birthday = '1900-01-01'

        entered_height = self.line_addsurfer_ht.text() if not \
            self.line_addsurfer_ht.text() == "" else None
        if entered_height is not None:
            entered_height = self.check_for_int(check_string_for_int=entered_height)

        entered_weight = self.line_addsurfer_wt.text() if not \
            self.line_addsurfer_wt.text() == "" else None
        if entered_weight is not None:
            entered_weight = self.check_for_int(check_string_for_int=entered_weight)

        entered_first_season = self.line_addsurfer_firstseason.text() if not \
            self.line_addsurfer_firstseason.text() == "" else None
        if entered_first_season is not None:
            entered_first_season = self.check_for_int(check_string_for_int=entered_first_season)

        entered_first_tour = self.line_addsurfer_firsttour.text()

        entered_home_continent = self.cb_addsurfer_hcontinent.currentText()
        entered_home_country = self.cb_addsurfer_hcountry.currentText()
        entered_home_region = self.cb_addsurfer_hregion.currentText()
        entered_home_city = self.cb_addsurfer_hcity.currentText()

        new_surfer = AddSurfer(entered_gender=entered_gender,
                               entered_first_name=entered_first_name,
                               entered_last_name=entered_last_name,
                               entered_stance=entered_stance,
                               entered_rep_continent=entered_rep_continent,
                               entered_rep_country=entered_rep_country,
                               entered_birthday=entered_birthday,
                               entered_height=entered_height,
                               entered_weight=entered_weight,
                               entered_first_season=entered_first_season,
                               entered_first_tour=entered_first_tour,
                               entered_home_continent=entered_home_continent,
                               entered_home_country=entered_home_country,
                               entered_home_region=entered_home_region,
                               entered_home_city=entered_home_city)

        new_surfer.add_new_surfer()

        self.slot_pb_addsurfer_clear_clicked()

########################################################################################################################

if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget()
    win.show()

    sys.exit(app.exec())
