import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQml.Models 2.1
import QtLocation 5.14
import QtPositioning 5.14
import QtQuick.Layouts 1.15


Row {
    width: 800
    height: 500
    anchors.fill: parent

    ColumnLayout {
        width: 200
        height: parent.height

        Item {
            Layout.alignment: Qt.Align
            
            Column {
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
                    model: ["Praha", "Středočeský", "Královéhradecký"]
                }

                Label {
                    text: "Okresy"
                }

                ComboBox {
                    model: ["Rychnov n. Kn.", "Trutnov", "Jičín", "Náchod"]
                }
            }
        }

        Button {
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignBottom

            id: filtrButton
            text: "Filtrovat"
        }
    }

    ColumnLayout {
        width: 500
        height: parent.height
        
        Rectangle {
            width: parent.width
            height: 500
            Layout.alignment: Qt.AlignVCenter
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
    }

    Column {
        width: 200
        height: parent.height
        padding: 5

        Label {
            text: "Seznam měst:"
        }
    }
}
