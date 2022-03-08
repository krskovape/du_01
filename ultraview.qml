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

                Slider {
                    from: 1
                    to: 100
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
        width: 300
        height: parent.height
        
        Rectangle {
            width: parent.width
            height: 300
            Layout.alignment: Qt.AlignVCenter
            border.width: 1
            border.color: "black"
            radius: 5
            Label {
                text: "tady bude mapa"
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
