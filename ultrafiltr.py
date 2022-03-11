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
        self.city_list = []
        if filename:
            self.load_from_json(filename)
    
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


app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
citylist_model = FiltrModel(CITY_LIST_FILE)
ctxt = view.rootContext()
ctxt.setContextProperty('filtrModel',citylist_model)
view.setSource(url)
view.show()
app.exec_()