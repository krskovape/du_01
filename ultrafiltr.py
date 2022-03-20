from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel, QByteArray
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtPositioning import QGeoCoordinate
from PySide2 import QtCore
from enum import Enum
import typing
import sys
import json

VIEW_URL = "superview.qml"
PUVODNI_LIST_FILE = "data_ukol1_znak.json"

#Class for maintaining list of tasks
class FiltrModel(QAbstractListModel):

    #Enum with added custom roles
    class Roles(Enum):
        LOCATION = QtCore.Qt.UserRole+0
        AREA = QtCore.Qt.UserRole+1
        POPULATION = QtCore.Qt.UserRole+2
        TYP = QtCore.Qt.UserRole+3
        KRAJ = QtCore.Qt.UserRole+4
        OKRES = QtCore.Qt.UserRole+5
        ZNAK = QtCore.Qt.UserRole+6

    #Initialize and load list from given file
    def __init__ (self,filename=None):
        QAbstractListModel.__init__(self)
        self._min_po = 0
        self._max_po = 1500000
        self._min_area = 0.0
        self._max_area = 500.0
        self._obce = False
        self._mesta = False
        self.kraj_filtr = ["všechny"]
        self.okres_filtr = ["všechny"]
        self.kraj_all = set()
        self.okres_all = set()
        self._output_file = "Sem zadejte cestu k výstupnímu souboru"
        self.city_list = []
        self.puvodni_list = []
        if filename:
            self.load_from_json(filename)
    
    #Property min_po
    def get_min_po(self):
        return self._min_po
    
    def set_min_po(self,val):
        if val != self.min_po:
            self._min_po = val
            self.min_po_changed.emit()
    
    min_po_changed = Signal()
    min_po = Property(int, get_min_po, set_min_po, notify=min_po_changed)

    #Property max_po
    def get_max_po(self):
        return self._max_po
    
    def set_max_po(self,val):
        if val != self.max_po:
            self._max_po = val
            self.max_po_changed.emit()
    
    max_po_changed = Signal()
    max_po = Property(int, get_max_po, set_max_po, notify=max_po_changed)

    #Property min_area
    def get_min_area(self):
        return self._min_area
    
    def set_min_area(self,val):
        if val != self.min_area:
            self._min_area = int(val)
            self.min_area_changed.emit()
    
    min_area_changed = Signal()
    min_area = Property(float, get_min_area, set_min_area, notify=min_area_changed)

    #Property max_area
    def get_max_area(self):
        return self._max_area
    
    def set_max_area(self,val):
        if val != self.max_area:
            self._max_area = int(val)
            self.max_area_changed.emit()
    
    max_area_changed = Signal()
    max_area = Property(float, get_max_area, set_max_area, notify=max_area_changed)

    #Property obce
    def get_obce(self):
        return self._obce
    
    def set_obce(self,val):
        if val != self.obce:
            self._obce = val
            self.obce_changed.emit()
    
    obce_changed = Signal()
    obce = Property(bool, get_obce, set_obce, notify=obce_changed)

    #Property mesta
    def get_mesta(self):
        return self._mesta
    
    def set_mesta(self,val):
        if val != self.mesta:
            self._mesta = val
            self.mesta_changed.emit()
    
    mesta_changed = Signal()
    mesta = Property(bool, get_mesta, set_mesta, notify=mesta_changed)

    #Property output_file
    def get_output_file(self):
        return self._output_file
    
    def set_output_file(self,val):
        if val != self.output_file:
            self._output_file = val
            self.output_file_changed.emit()
    
    output_file_changed = Signal()
    output_file = Property(str, get_output_file, set_output_file, notify=output_file_changed)

    #Load list of cities from given file
    def load_from_json(self,filename):
        with open(filename,encoding="utf-8") as f:
            self.puvodni_list = json.load(f)

            for c in self.puvodni_list:
                #Create QGeoCoordinate from the original JSON location
                pos = c['location']
                lon,lat = pos.split("(")[1].split(")")[0].split(" ")
                c['location'] = QGeoCoordinate(float(lat),float(lon))

                #Add value of 'krajLabel' and 'okresLabel' to set property
                self.kraj_all.add(c['krajLabel'])
                self.okres_all.add(c['okresLabel'])

                #Check if feature contains attribute 'mestoLabel' and set value to 'obec' if not
                if "mestoLabel" not in c:
                    c["mestoLabel"] = "obec"
                
                #Check if feature contains URL of its symbol, add URL of white rectangle if not
                if "znak" not in c:
                    c["znak"] = "https://www.meme-arsenal.com/memes/422425412debbe780318e9bfee9efdac.jpg" #bílý obdélník

    #Return number of cities in the list
    def rowCount(self, parent:QtCore.QModelIndex=...) -> int:
        """ Return number of cities in the list"""
        return len(self.city_list)
    
    #For given index and role return information of the city
    def data(self, index:QtCore.QModelIndex, role:int=...) -> typing.Any:
        if role == QtCore.Qt.DisplayRole: # On DisplayRole return name
            return self.city_list[index.row()]["obecLabel"]
        elif role == self.Roles.LOCATION.value: # On location role return coordinates
            return self.city_list[index.row()]["location"]
        elif role == self.Roles.AREA.value: # On area role return area
            return self.city_list[index.row()]["area"]
        elif role == self.Roles.POPULATION.value: # On population role return population
            return self.city_list[index.row()]["population"]
        elif role == self.Roles.TYP.value: # On typ role return city/municipality
            return self.city_list[index.row()]["mestoLabel"]
        elif role == self.Roles.KRAJ.value: # On kraj role return name of the region
            return self.city_list[index.row()]["krajLabel"]
        elif role == self.Roles.OKRES.value: # On okres role return name of the district
            return self.city_list[index.row()]["okresLabel"]
        elif role == self.Roles.ZNAK.value: # On znak role return URL of city's symbol
            return self.city_list[index.row()]["znak"]
    
    #Returns dict with role numbers and role names for default and custom roles together
    def roleNames(self) -> typing.Dict[int, QByteArray]:
        roles = super().roleNames()
        roles[self.Roles.LOCATION.value] = QByteArray(b'location')
        roles[self.Roles.AREA.value] = QByteArray(b'area')
        roles[self.Roles.POPULATION.value] = QByteArray(b'population')
        roles[self.Roles.TYP.value] = QByteArray(b'typ')
        roles[self.Roles.KRAJ.value] = QByteArray(b'kraj')
        roles[self.Roles.OKRES.value] = QByteArray(b'okres')
        roles[self.Roles.ZNAK.value] = QByteArray(b'znak')
        return roles

    #Sets the value of property kraj_filtr
    @Slot(str)
    def set_kraj(self, val: str):
        self.kraj_filtr = []
        self.kraj_filtr.append(val)
        print(self.kraj_filtr)

    #Sets the value of property okres_filtr
    @Slot(str)
    def set_okres(self, val: str):
        self.okres_filtr = []
        self.okres_filtr.append(val)
        print(self.okres_filtr)
    
    #Filters the original list of cities
    @Slot()
    def filtrovat(self):
        #Delete all rows from city_list
        self.beginRemoveRows(self.index(0).parent(), 0 , len(self.city_list)-1)
        self.city_list = []
        self.endRemoveRows()

        #Set values of kraj_filtr and okres_filtr if all menu items are chosen
        if "všechny" in self.kraj_filtr:
            self.kraj_filtr = self.kraj_all
        
        if "všechny" in self.okres_filtr:
            self.okres_filtr = self.okres_all

        #Filter the original list and add items to new one
        input_idx = 0
        for feature in self.puvodni_list:
            pocet_obyv = int(feature["population"])
            rozloha = float(feature["area"])

            #Municipalities
            if self.obce == True:
                if feature["mestoLabel"] == "obec"\
                    and pocet_obyv > self.min_po and pocet_obyv < self.max_po\
                    and rozloha > self.min_area and rozloha < self.max_area\
                    and feature["krajLabel"] in self.kraj_filtr\
                    and feature["okresLabel"] in self.okres_filtr:

                    self.beginInsertRows(self.index(0).parent(),input_idx,input_idx)
                    self.city_list.append(feature)
                    self.endInsertRows()
                    input_idx += 1
            
            #Towns
            if self.mesta == True:
                if feature["mestoLabel"] == "město v Česku"\
                    and pocet_obyv > self.min_po and pocet_obyv < self.max_po\
                    and rozloha > self.min_area and rozloha < self.max_area\
                    and feature["krajLabel"] in self.kraj_filtr\
                    and feature["okresLabel"] in self.okres_filtr:

                    self.beginInsertRows(self.index(0).parent(),input_idx,input_idx)
                    self.city_list.append(feature)
                    self.endInsertRows()
                    input_idx += 1
    
        print(f"Načteno {input_idx} obcí.")
    
    #Save filtered list of cities to a file
    # @Slot()
    # def save_to_file(self):
    #     with open(self.output_file, 'w', encoding ='utf8') as json_file:
    #         json.dump(self.city_list, json_file, ensure_ascii = False)
            

app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
puvodnilist_model = FiltrModel(PUVODNI_LIST_FILE)
ctxt = view.rootContext()
ctxt.setContextProperty('filtrModel',puvodnilist_model)
view.setSource(url)
view.show()
app.exec_()