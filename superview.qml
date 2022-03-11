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
        
        Item {
            width: parent.width
            //height: parent.height
            height: 400
            //Layout.fillHeight: true
            Layout.alignment: Qt.AlignTop
            
            Column {
                width: parent.width
                spacing: 15
                Row {
                    spacing: 5
                    CheckBox {
                        text: "Města"
                        checkable: true
                    }
                    CheckBox {
                        text: "Obce"
                        checkable: true
                    }
                }

                Label {
                    text: "Počet obyvatel"
                }

                RangeSlider {
                    from: 1
                    to: 100
                    first.value: 10
                    second.value: 90
                }

                Row {
                    spacing: 100
                    //tohle budou TextInputy provázané na value z RangeSlider
                    Label {
                        text: "Od: 1"
                    }
                    Label {
                        text: "Do: 100"
                    }
                }

                Label {
                    text: "Kraj"
                }

                ComboBox {
                    width: parent.width
                    model: ["Praha", "Středočeský", "Královéhradecký"]
                }

                Label {
                    text: "Okresy"
                }

                ComboBox {
                    width: parent.width
                    model: ["Rychnov n. Kn.", "Trutnov", "Jičín", "Náchod"]
                }
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
            }
        }
    }

    Rectangle {
        Layout.fillWidth: true
        Layout.fillHeight: true
        border.width: 1
        border.color: "black"
        radius: 5

        Plugin {
                id: mapPlugin
                name: "osm"
                PluginParameter {
                    name:"osm.mapping.custom.host"
                    value:"https://maps.wikimedia.org/osm/"
                }
            }

        Map {
            width: parent.width
            height: parent.height

            plugin: mapPlugin
            activeMapType: supportedMapTypes[supportedMapTypes.length - 1]

            /*
            //visibleRegion: geoshape
            visibleRegion: Item {
                property variant region: QtPositioning.shape(model.location)
            }*/

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

        Component {
            id: cityListDelegate
            Item {
                width: parent.width
                height: childrenRect.height
                Column {
                    //spacing: 5
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
