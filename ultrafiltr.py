from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel, QByteArray
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtPositioning import QGeoCoordinate
from PySide2 import QtCore
from enum import Enum
import typing
import sys
import json

VIEW_URL = "ultraview.qml"
CITY_LIST_FILE = "souradnice.json"

class FiltrModel(QAbstractListModel):

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


app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
tasklist_model = FiltrModel(CITY_LIST_FILE)
ctxt = view.rootContext()
ctxt.setContextProperty('taskListModel',tasklist_model)
view.setSource(url)
view.show()
app.exec_()