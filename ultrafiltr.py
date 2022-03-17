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
PUVODNI_LIST_FILE = "data_ukol1.json"


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
        self._obce = True
        self._mesta = True
        self.kraj_filtr = ["všechny"]
        self.okres_filtr = ["všechny"]
        self.kraj_all = ["Jihočeský", "Jihomoravský", "Karlovarský", "Královéhradecký", "Liberecký", "Moravskoslezský", "Olomoucký", "Pardubický", "Plzeňský", "Praha", "Středočeský", "Ústecký", "Vysočina", "Zlínský"]
        self.okres_all = ["České Budějovice", "Český Krumlov", "Jindřichův Hradec", "Písek", "Prachatice", "Strakonice", "Tábor", "Blansko", "Brno-město", "Brno-venkov", "Břeclav", "Hodonín", "Vyškov", "Znojmo", "Cheb", "Karlovy Vary", "Sokolov", "Hradec Králové", "Jičín", "Náchod", "Rychnov nad Kněžnou", "Trutnov", "Česká Lípa", "Jablonec nad Nisou", "Liberec", "Semily", "Bruntál", "Frýdek-Místek", "Karviná", "Nový Jičín", "Opava", "Ostrava-město", "Jeseník", "Olomouc", "Prostějov", "Přerov", "Šumperk", "Chrudim", "Pardubice", "Svitavy", "Ústí nad Orlicí", "Domažlice", "Klatovy", "Plzeň-jih", "Plzeň-město", "Plzeň-sever", "Rokycany", "Tachov", "Praha", "Benešov", "Beroun", "Kladno", "Kolín", "Kutná Hora", "Mělník", "Mladá Boleslav", "Nymburk", "Praha-východ", "Praha-západ", "Příbram", "Rakovník", "Děčín", "Chomutov", "Litoměřice", "Louny", "Most", "Teplice", "Ústí nad Labem", "Havlíčkův Brod", "Jihlava", "Pelhřimov", "Třebíč", "Žďár nad Sázavou", "Kroměříž", "Uherské Hradiště", "Vsetín", "Zlín"]
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

    #property obce
    def get_obce(self):
        return self._obce
    
    def set_obce(self,val):
        if val != self.obce:
            self._obce = val
            self.obce_changed.emit()
    
    obce_changed = Signal()
    obce = Property(list, get_obce, set_obce, notify=obce_changed)

    #property mesta
    def get_mesta(self):
        return self._mesta
    
    def set_mesta(self,val):
        if val != self.mesta:
            self._mesta = val
            self.mesta_changed.emit()
    
    mesta_changed = Signal()
    mesta = Property(list, get_mesta, set_mesta, notify=mesta_changed)

    
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
            return self.city_list[index.row()]["obecLabel"]
        elif role == self.Roles.LOCATION.value: # On location role return coordinates
            return self.city_list[index.row()]["location"]
        elif role == self.Roles.AREA.value: # On area role return area
            return self.city_list[index.row()]["area"]
        elif role == self.Roles.POPULATION.value: # On population role return population
            return self.city_list[index.row()]["population"]
        elif role == self.Roles.TYP.value: 
            return self.city_list[index.row()]["mestoLabel"]
        elif role == self.Roles.KRAJ.value: 
            return self.city_list[index.row()]["krajLabel"]
        elif role == self.Roles.OKRES.value: 
            return self.city_list[index.row()]["okresLabel"]
    
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

    @Slot(str)
    def add_to_kraj(self, val: str):
        self.kraj_filtr.append(val)
        print(self.kraj_filtr)

    @Slot()
    def remove_from_kraj(self):
        self.kraj_filtr = []
        print(self.kraj_filtr)

    @Slot(str)
    def add_to_okres(self, val: str):
        self.okres_filtr.append(val)
        print(self.okres_filtr)

    @Slot()
    def remove_from_okres(self):
        self.okres_filtr = []
        print(self.okres_filtr)
    
    @Slot()
    def filtrovat(self):
        #Delete all rows from city_list
        self.beginRemoveRows(self.index(0).parent(), 0 , len(self.city_list)-1)
        self.city_list = []
        self.endRemoveRows()

        print(self.obce)
        print(self.mesta)

        input_idx = 0
        if "všechny" in self.kraj_filtr:
            self.kraj_filtr = self.kraj_all
        
        if "všechny" in self.okres_filtr:
            self.okres_filtr = self.okres_all

        for feature in self.puvodni_list:
            pocet_obyv = int(feature["population"])
            if "mestoLabel" not in feature and self.obce == True\
                and pocet_obyv > self.min_po and pocet_obyv < self.max_po\
                and feature["krajLabel"] in self.kraj_filtr\
                and feature["okresLabel"] in self.okres_filtr:

                self.beginInsertRows(self.index(0).parent(),input_idx,input_idx)
                self.city_list.append(feature)
                self.endInsertRows()
                input_idx += 1
                #print(f"přidávám feature {input_idx}")
            
            if self.mesta == True and "mestoLabel" in feature:
                if feature["mestoLabel"] == "město v Česku"\
                    and pocet_obyv > self.min_po and pocet_obyv < self.max_po\
                    and feature["krajLabel"] in self.kraj_filtr\
                    and feature["okresLabel"] in self.okres_filtr:

                    self.beginInsertRows(self.index(0).parent(),input_idx,input_idx)
                    self.city_list.append(feature)
                    self.endInsertRows()
                    input_idx += 1

        #print(self.city_list)    
        print(f"Načteno {input_idx} obcí.")
            

app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
puvodnilist_model = FiltrModel(PUVODNI_LIST_FILE)
ctxt = view.rootContext()
ctxt.setContextProperty('filtrModel',puvodnilist_model)
view.setSource(url)
view.show()
app.exec_()