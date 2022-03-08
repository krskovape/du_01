import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQml.Models 2.1
import QtLocation 5.14
import QtPositioning 5.14
import QtQuick.Layouts 1.15


ColumnLayout {
    implicitWidth: 500
    implicitHeight: 500
    anchors.fill: parent

    Row {
        Column {
            width: 150
            Layout.fillHeight: true

            Row {
                CheckBox {
                    text: "Města"
                    checkable: true
                }
                CheckBox {
                    text: "Obce"
                    checkable: true
                }
            }

            RowLayout {
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignBottom

                Button {
                    id: filtrButton
                    text: "Filtrovat"
                }
            }
        }

        Column {
            width: 150
            Layout.fillHeight: true
            
            Rectangle {
                width: parent.width
                height: parent.height
                border.width: 1
                border.color: "black"
                radius: 5
                Label {
                    text: "tady bude mapa"
                }
            }
        }
    }
}
