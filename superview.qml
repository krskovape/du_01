import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQml.Models 2.1
import QtLocation 5.14
import QtPositioning 5.14
import QtQuick.Layouts 1.15
import QtPositioning 5.2


RowLayout {
    implicitWidth: 800
    implicitHeight: 500
    anchors.fill: parent

    // Create property holding model of currently selected city
    property var currentModelItem;

    ColumnLayout {
        width: 200
        height: parent.height
        //Layout.fillHeight: true
        Layout.alignment: Qt.AlignTop
        
        Column {
            width: parent.width
            height: 500
            spacing: 15
            topPadding: 3
            bottomPadding: 30

            Row {
                spacing: 5
                CheckBox {
                    id: městaCheck
                    text: "Města"
                    checkable: true
                    onCheckedChanged: {
                        if (checkState === Qt.Checked) {
                            console.log("Města checked")
                            filtrModel.add_to_typ("město") 
                        }
                        if (checkState === Qt.Unchecked) {
                            console.log("Města unchecked")
                            filtrModel.remove_from_typ("město")
                        }
                    }
                }
                CheckBox {
                    id: obceCheck
                    text: "Obce"
                    checkable: true
                    onCheckedChanged: {
                        if (checkState === Qt.Checked) {
                            console.log("Obce checked")
                            filtrModel.add_to_typ("obec") 
                        }
                        if (checkState === Qt.Unchecked) {
                            console.log("Obce unchecked")
                            filtrModel.remove_from_typ("obec")
                        }  
                    }
                }
            }

            Label {
                text: "Počet obyvatel"
            }

            RangeSlider {
                id: sliderObyv
                from: 0
                to: 1500000
                first.value: filtrModel.min_po
                second.value: filtrModel.max_po
                Binding {
                    target: filtrModel
                    property: "min_po"
                    value: sliderObyv.first.value
                }
                Binding {
                    target: filtrModel
                    property: "max_po"
                    value: sliderObyv.second.value
                }

            }

            Row {
                spacing: 70

                Row {
                    spacing: 5

                    Label {
                        text: "Od: "
                    }
                    TextInput {
                        id: minPoIntup
                        text: filtrModel.min_po
                        Binding {
                            target: filtrModel
                            property: "min_po"
                            value: minPoIntup.text
                        }
                    }
                }
                Row {
                    spacing: 5

                    Label {
                        text: "Do: "
                    }
                    TextInput {
                        id: maxPoIntup
                        text: filtrModel.max_po
                        Binding {
                            target: filtrModel
                            property: "max_po"
                            value: maxPoIntup.text
                        }
                    }
                }
            }

            Label {
                text: "Kraj"
            }

            ComboBox {
                id: krajBox
                width: parent.width
                model: ["všechny","Jihočeský", "Jihomoravský", "Karlovarský", "Královéhradecký", "Liberecký", "Moravskoslezský", "Olomoucký", "Pardubický", "Plzeňský", "Praha", "Středočeský", "Ústecký", "Vysočina", "Zlínský"]
                onActivated: {
                    console.log("kraj: "+currentText)
                    filtrModel.remove_from_kraj()
                    filtrModel.add_to_kraj(currentText)
                    if (currentIndex == 1)
                        okresBox.model = ["všechny", "České Budějovice", "Český Krumlov", "Jindřichův Hradec", "Písek", "Prachatice", "Strakonice", "Tábor"]
                    if (currentIndex == 2)
                        okresBox.model = ["všechny", "Blansko", "Brno-město", "Brno-venkov", "Břeclav", "Hodonín", "Vyškov", "Znojmo"]
                    if (currentIndex == 3)
                        okresBox.model = ["všechny", "Cheb", "Karlovy Vary", "Sokolov"]
                    if (currentIndex == 4)
                        okresBox.model = ["všechny", "Hradec Králové", "Jičín", "Náchod", "Rychnov nad Kněžnou", "Trutnov"]
                    if (currentIndex == 5)
                        okresBox.model = ["všechny", "Česká Lípa", "Jablonec nad Nisou", "Liberec", "Semily"]
                    if (currentIndex == 6)
                        okresBox.model = ["všechny", "Bruntál", "Frýdek-Místek", "Karviná", "Nový Jičín", "Opava", "Ostrava-město"]
                    if (currentIndex == 7)
                        okresBox.model = ["všechny", "Jeseník", "Olomouc", "Prostějov", "Přerov", "Šumperk"]
                    if (currentIndex == 8)
                        okresBox.model = ["všechny", "Chrudim", "Pardubice", "Svitavy", "Ústí nad Orlicí"]
                    if (currentIndex == 9)
                        okresBox.model = ["všechny", "Domažlice", "Klatovy", "Plzeň-jih", "Plzeň-město", "Plzeň-sever", "Rokycany", "Tachov"]
                    if (currentIndex == 10)
                        okresBox.model = ["Praha"]
                    if (currentIndex == 11)
                        okresBox.model = ["všechny", "Benešov", "Beroun", "Kladno", "Kolín", "Kutná Hora", "Mělník", "Mladá Boleslav", "Nymburk", "Praha-východ", "Praha-západ", "Příbram", "Rakovník"]
                    if (currentIndex == 12)
                        okresBox.model = ["všechny", "Děčín", "Chomutov", "Litoměřice", "Louny", "Most", "Teplice", "Ústí nad Labem"]
                    if (currentIndex == 13)
                        okresBox.model = ["všechny", "Havlíčkův Brod", "Jihlava", "Pelhřimov", "Třebíč", "Žďár nad Sázavou"]
                    if (currentIndex == 14)
                        okresBox.model = ["všechny", "Kroměříž", "Uherské Hradiště", "Vsetín", "Zlín"]                      
                }
                /*Binding {
                    target: filtrModel
                    property: "kraj_filtr"
                    value: krajBox.currentText
                }*/
            }

            Label {
                text: "Okres"
            }

            ComboBox {
                id: okresBox
                width: parent.width
                model: ["všechny"]
                onActivated: {
                    console.log("okes: "+currentText)
                    filtrModel.remove_from_okres()
                    filtrModel.add_to_okres(currentText)
                }
                /*Binding {
                    target: filtrModel
                    property: "okres_filtr"
                    value: okresBox.currentText
                }*/
            }
        }
        
        Item {
            width: parent.width
            height: children.height
            Layout.alignment: Qt.AlignBottom

            Button {
                width: parent.width
                //Layout.alignment: Qt.AlignBottom

                id: filtrButton
                text: "Filtrovat"

                onClicked: {
                    filtrModel.filtrovat()
                    cityList.currentIndex = -1
                }
            }
        }
    }

    Rectangle {
        Layout.fillWidth: true
        Layout.fillHeight: true

        Plugin {
                id: mapPlugin
                name: "osm"
                /*PluginParameter {
                    name:"osm.mapping.custom.host"
                    value:"https://maps.wikimedia.org/osm/"
                }*/
            }

        Map {
            width: parent.width
            height: parent.height

            plugin: mapPlugin
            activeMapType: supportedMapTypes[supportedMapTypes.length - 1]

            
            //visibleRegion: geoshape
            //visibleRegion: QtPositioning.shape(model.location)

            center: currentModelItem.location // Center to the selected city
            zoomLevel: 12

            MapItemView {
                model: filtrModel
                delegate: MapQuickItem {
                    coordinate: model.location
                    sourceItem: Text {
                        text: model.display
                    }
                }
            }
        }
    }
    
    ListView {
        id: cityList
        width: 250
        height: parent.height
        focus: true
        Layout.alignment: Qt.AlignTop
        Layout.fillHeight: true
        //currentIndex : -1

        Component {
            id: cityListDelegate
            Item {
                width: parent.width
                height: childrenRect.height
                Column {
                    bottomPadding: 7
                    Text {
                        text: model.display
                        color: {
                            color = "black"
                            if (model.typ == "město")
                                color = "red"
                        }
                        font.bold: true
                    }
                    Row {
                        spacing: 4
                        Text {
                            text: "Rozloha:"
                        }
                        Text {
                            textFormat: Text.RichText
                            text: model.area+" km<sup>2</sup>"
                        }
                    }
                    Row {
                        spacing: 4
                        Text {
                            text: "Počet obyvatel:"
                        }
                        Text {
                            text: model.population
                        }
                    }
                    Row {
                        spacing: 4
                        Text {
                            text: "Okres:"
                        }
                        Text {
                            text: model.okres
                        }
                    }
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: cityList.currentIndex = index
                }
            }
        }

        model: DelegateModel {
            id: cityListDelegateModel
            model: filtrModel
            delegate: cityListDelegate
        }

        // na currentModelItem připojí aktuální cityListDelegateModel
        onCurrentItemChanged: currentModelItem = cityListDelegateModel.items.get(cityList.currentIndex).model

        highlight: Rectangle {
            color: "lightsteelblue"
        }
    }
}
