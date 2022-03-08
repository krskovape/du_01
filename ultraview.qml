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
        width: 150
        height: parent.height
        RowLayout {
            Layout.fillWidth: true
            Layout.alignment: Qt.Align
            
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
        height: parent.height
        
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
