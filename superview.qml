import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQml.Models 2.1
import QtLocation 5.14
import QtPositioning 5.14
import QtQuick.Layouts 1.15


RowLayout {
    implicitWidth: 800
    implicitHeight: 500
    anchors.fill: parent

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
        }
    }
    
    Item {
        width: 200
        height: parent.height
        Layout.alignment: Qt.AlignTop

        Label {
            text: "Seznam měst:"
        }
    }
}
