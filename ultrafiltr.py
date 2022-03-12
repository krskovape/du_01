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
CITY_LIST_FILE = "mesta.json"

praha = ["Praha"]
jihočeský = ["České Budějovice", "Český Krumlov", "Jindřichův Hradec", "Písek", "Prachatice", "Strakonice", "Tábor"]
královéhradecký = ["Hradec Králové", "Jičín", "Náchod", "Rychnov nad Kněžnou", "Trutnov"]
liberecký = ["Česká Lípa", "Jablonec nad Nisou", "Liberec", "Semily"]
pardubický = ["Chrudim", "Pardubice", "Svitavy", "Ústí nad Orlicí"]
středočeský = ["Benešov", "Beroun", "Kladno", "Kolín", "Kutná Hora", "Mělník", "Mladá Boleslav", "Nymburk", "Praha-východ", "Praha-západ", "Příbram", "Rakovník"]

všechny_okresy = ["Benešov", "Beroun", "Blansko", "Brno-město", "Brno-venkov", "Bruntál", "Břeclav", "Česká Lípa"]
všechny_kraje = ["Jihočeský", "Jihomoravský", "Karlovarský", "Vysočina", "Královéhradecký", "Liberecký", "Moravskoslezský", "Olomoucký", "Pardubický", "Plzeňský", "Praha", "Středočeský", "Ústecký", "Zlínský"]

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
        self.city_list = []
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
    
    def load_from_json(self,filename):
        with open(filename,encoding="utf-8") as f:
            self.city_list = json.load(f)

            # Create QGeoCoordinate from the original JSON location
            for c in self.city_list:
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
    
    '''
    @Slot(list,str)
    def add_to_list(self, input_list: list, val: str):
        input_list.append(val)
        print(input_list)
    '''

    @Slot(str)
    def add_to_typ(self, val: str):
        self.typ_filtr.append(val)
        print(self.typ_filtr)



app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
citylist_model = FiltrModel(CITY_LIST_FILE)
ctxt = view.rootContext()
ctxt.setContextProperty('filtrModel',citylist_model)
view.setSource(url)
view.show()
app.exec_()