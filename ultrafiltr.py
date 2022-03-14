from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel, QByteArray
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtPositioning import QGeoCoordinate
from PySide2 import QtCore
from enum import Enum
import typing
import sys
import json

#VIEW_URL = "ultraview.qml"
VIEW_URL = "superview.qml"
PUVODNI_LIST_FILE = "mesta.json"


class FiltrModel(QAbstractListModel):

    class Roles(Enum):
        LOCATION = QtCore.Qt.UserRole+0
        AREA = QtCore.Qt.UserRole+1
        POPULATION = QtCore.Qt.UserRole+2
        TYP = QtCore.Qt.UserRole+3
        KRAJ = QtCore.Qt.UserRole+4
        OKRES = QtCore.Qt.UserRole+5

    def __init__ (self,filename=None):
        QAbstractListModel.__init__(self)
        self._min_po = 0
        self._max_po = 100
        self._typ_filtr = []
        self._kraj_filtr = ""
        self._okres_filtr = ""
        self.city_list = []
        self.puvodni_list = []
        if filename:
            self.load_from_json(filename)
    
    #property min_po
    def get_min_po(self):
        return self._min_po
    
    def set_min_po(self,val):
        if val != self.min_po:
            self._min_po = val
            self.min_po_changed.emit()
    
    min_po_changed = Signal()
    min_po = Property(int, get_min_po, set_min_po, notify=min_po_changed)

    #property max_po
    def get_max_po(self):
        return self._max_po
    
    def set_max_po(self,val):
        if val != self.max_po:
            self._max_po = val
            self.max_po_changed.emit()
    
    max_po_changed = Signal()
    max_po = Property(int, get_max_po, set_max_po, notify=max_po_changed)

    #property typ_filtr
    def get_typ_filtr(self):
        return self._typ_filtr
    
    def set_typ_filtr(self,val):
        if val != self.typ_filtr:
            self._typ_filtr = val
            self.typ_filtr_changed.emit()
    
    typ_filtr_changed = Signal()
    typ_filtr = Property(list, get_typ_filtr, set_typ_filtr, notify=typ_filtr_changed)

    #property kraj_filtr
    def get_kraj_filtr(self):
        return self._kraj_filtr
    
    def set_kraj_filtr(self,val):
        if val != self.kraj_filtr:
            self._kraj_filtr = val
            self.kraj_filtr_changed.emit()
    
    kraj_filtr_changed = Signal()
    kraj_filtr = Property(str, get_kraj_filtr, set_kraj_filtr, notify=kraj_filtr_changed)

    #property okres_filtr
    def get_okres_filtr(self):
        return self._okres_filtr
    
    def set_okres_filtr(self,val):
        if val != self.okres_filtr:
            self._okres_filtr = val
            self.okres_filtr_changed.emit()
    
    okres_filtr_changed = Signal()
    okres_filtr = Property(str, get_okres_filtr, set_okres_filtr, notify=okres_filtr_changed)


    
    def load_from_json(self,filename):
        with open(filename,encoding="utf-8") as f:
            self.puvodni_list = json.load(f)

            # Create QGeoCoordinate from the original JSON location
            for c in self.puvodni_list:
                pos = c['location']
                lon,lat = pos.split("(")[1].split(")")[0].split(" ")
                c['location'] = QGeoCoordinate(float(lat),float(lon))

    def rowCount(self, parent:QtCore.QModelIndex=...) -> int:
        """ Return number of cities in the list"""
        return len(self.city_list)
    
    def data(self, index:QtCore.QModelIndex, role:int=...) -> typing.Any:
        if role == QtCore.Qt.DisplayRole: # On DisplayRole return name
            return self.city_list[index.row()]["muniLabel"]
        elif role == self.Roles.LOCATION.value: # On location role return coordinates
            return self.city_list[index.row()]["location"]
        elif role == self.Roles.AREA.value: # On area role return area
            return self.city_list[index.row()]["area"]
        elif role == self.Roles.POPULATION.value: # On population role return population
            return self.city_list[index.row()]["population"]
        elif role == self.Roles.TYP.value: 
            return self.city_list[index.row()]["typ"]
        elif role == self.Roles.KRAJ.value: 
            return self.city_list[index.row()]["kraj"]
        elif role == self.Roles.OKRES.value: 
            return self.city_list[index.row()]["okres"]
    
    def roleNames(self) -> typing.Dict[int, QByteArray]:
        """Returns dict with role numbers and role names for default and custom roles together"""
        # Append custom roles to the default roles and give them names for a usage in the QML
        roles = super().roleNames() #vrátí seznam původních rolí
        roles[self.Roles.LOCATION.value] = QByteArray(b'location')
        roles[self.Roles.AREA.value] = QByteArray(b'area')
        roles[self.Roles.POPULATION.value] = QByteArray(b'population')
        roles[self.Roles.TYP.value] = QByteArray(b'typ')
        roles[self.Roles.KRAJ.value] = QByteArray(b'kraj')
        roles[self.Roles.OKRES.value] = QByteArray(b'okres')
        print(roles)
        return roles

    @Slot(str)
    def add_to_typ(self, val: str):
        self.typ_filtr.append(val)
        print(self.typ_filtr)

    @Slot(str)
    def remove_from_typ(self, val: str):
        self.typ_filtr.remove(val)
        print(self.typ_filtr)
    
    @Slot()
    def filtrovat(self):
        #vymažu všechny řádky
        self.beginRemoveRows(self.index(0).parent(), 0 , len(self.city_list)-1)
        self.city_list = []
        self.endRemoveRows()

        input_idx = 0
        for feature in self.puvodni_list:
            '''
            if self.Roles.TYP.value in self.typ_filtr\
                and self.Roles.POPULATION.value > self.min_po\
                and self.Roles.POPULATION.value < self.max_po\
                and self.Roles.KRAJ.value == self.kraj_filtr\
                and self.Roles.OKRES.value == self.okres_filtr:
                print(feature)
            '''
            pocet_obyv = int(feature["population"])
            if pocet_obyv > self.min_po and pocet_obyv < self.max_po:
                #začínám přidávat
                self.beginInsertRows(self.index(0).parent(),input_idx,input_idx)
                self.city_list.append(feature)
                #končím přidávání
                self.endInsertRows()
                input_idx += 1
                print(f"přidávám feature {input_idx}")
            
        print(self.city_list)
            

app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
puvodnilist_model = FiltrModel(PUVODNI_LIST_FILE)
ctxt = view.rootContext()
ctxt.setContextProperty('filtrModel',puvodnilist_model)
view.setSource(url)
view.show()
app.exec_()