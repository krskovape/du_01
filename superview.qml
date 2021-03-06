import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQml.Models 2.1
import QtLocation 5.14
import QtPositioning 5.14
import QtQuick.Layouts 1.15
import QtPositioning 5.2
import QtQuick.Dialogs 1.3


RowLayout {
    implicitWidth: 800
    implicitHeight: 500
    anchors.fill: parent

    // Create property holding model of currently selected city
    property var currentModelItem;

    ColumnLayout {
        Layout.preferredWidth: 200
        Layout.maximumWidth: 200
        height: parent.height
        Layout.alignment: Qt.AlignTop
        spacing: 15

        // ChechBoxes for towns and municipalities
        Row {
            spacing: 5
            topPadding: 3
            Layout.alignment: Qt.AlignHCenter
            CheckBox {
                id: městaCheck
                text: "Města"
                checkable: true
                onCheckStateChanged: filtrModel.mesta = městaCheck.checked
            }
            CheckBox {
                id: obceCheck
                text: "Obce"
                checkable: true
                onCheckStateChanged: filtrModel.obce = obceCheck.checked
            }
        }

        // Choosing the range of population
        Label {
            text: "Počet obyvatel"
            Layout.alignment: Qt.AlignHCenter
            topPadding: 8
            font.bold: true
        }

        RangeSlider {
            id: sliderObyv
            from: 0
            to: 1500000
            first.value: filtrModel.min_po
            second.value: filtrModel.max_po
            Layout.alignment: Qt.AlignHCenter

            Component.onCompleted: {
                    sliderObyv.setValues(0,1500000)
            }
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

        RowLayout {
            Label {
                text: "Od: "
            }
            TextInput {
                id: minPoInput
                text: filtrModel.min_po
                Binding {
                    target: filtrModel
                    property: "min_po"
                    value: minPoInput.text
                }
            }
            Rectangle {
                Layout.fillWidth: true
            }

            Label {
                text: "Do: "
            }
            TextInput {
                id: maxPoInput
                text: filtrModel.max_po
                Binding {
                    target: filtrModel
                    property: "max_po"
                    value: maxPoInput.text
                }
            }    
        }

        // Choosing the range of area
        Label {
            textFormat: Text.RichText
            text: "Rozloha [km<sup>2</sup>]"
            Layout.alignment: Qt.AlignHCenter
            topPadding: 15
            font.bold: true
        }

        RangeSlider {
            id: sliderArea
            from: 0
            to: 500
            first.value: filtrModel.min_area
            second.value: filtrModel.max_area
            Layout.alignment: Qt.AlignHCenter

            Component.onCompleted: {
                    sliderArea.setValues(0,500)
            }
            Binding {
                target: filtrModel
                property: "min_area"
                value: sliderArea.first.value
            }
            Binding {
                target: filtrModel
                property: "max_area"
                value: sliderArea.second.value
            }

        }

        RowLayout {
            Label {
                text: "Od: "
            }
            TextInput {
                id: minAreaInput
                text: filtrModel.min_area
                Binding {
                    target: filtrModel
                    property: "min_area"
                    value: minAreaInput.text
                }
            }

            Rectangle {
                Layout.fillWidth: true
            }
        
            Label {
                text: "Do: "
            }
            TextInput {
                id: maxAreaInput
                text: filtrModel.max_area
                Binding {
                    target: filtrModel
                    property: "max_area"
                    value: maxAreaInput.text
                }
            }
        }

        // Choosing the region
        Label {
            text: "Kraj"
            Layout.alignment: Qt.AlignHCenter
            topPadding: 15
            font.bold: true
        }

        ComboBox {
            id: krajBox
            Layout.fillWidth: true
            model: ["všechny","Jihočeský", "Jihomoravský", "Karlovarský", "Královéhradecký", "Liberecký", "Moravskoslezský", "Olomoucký", "Pardubický", "Plzeňský", "Praha", "Středočeský", "Ústecký", "Vysočina", "Zlínský"]
            onActivated: {
                console.log("kraj: "+currentText)
                filtrModel.set_kraj(currentText)
                if (currentIndex == 0)
                    okresBox.model = ["všechny"]
                    filtrModel.set_okres("všechny")
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
                    okresBox.model = ["všechny"]
                if (currentIndex == 11)
                    okresBox.model = ["všechny", "Benešov", "Beroun", "Kladno", "Kolín", "Kutná Hora", "Mělník", "Mladá Boleslav", "Nymburk", "Praha-východ", "Praha-západ", "Příbram", "Rakovník"]
                if (currentIndex == 12)
                    okresBox.model = ["všechny", "Děčín", "Chomutov", "Litoměřice", "Louny", "Most", "Teplice", "Ústí nad Labem"]
                if (currentIndex == 13)
                    okresBox.model = ["všechny", "Havlíčkův Brod", "Jihlava", "Pelhřimov", "Třebíč", "Žďár nad Sázavou"]
                if (currentIndex == 14)
                    okresBox.model = ["všechny", "Kroměříž", "Uherské Hradiště", "Vsetín", "Zlín"]                      
            }
        }

        //Choosing the district
        Label {
            text: "Okres"
            Layout.alignment: Qt.AlignHCenter
            topPadding: 15
            font.bold: true
        }

        ComboBox {
            id: okresBox
            Layout.fillWidth: true
            model: ["všechny"]
            onActivated: {
                console.log("okes: "+currentText)
                filtrModel.set_okres(currentText)
            }
        }

        // Button for calling the filter function
        Button {
            Layout.fillWidth: true
            id: filtrButton
            text: "Filtrovat"

            onClicked: {
                filtrModel.filtrovat()
                cityList.currentIndex = -1
                mapaObce.fitViewportToVisibleMapItems()
            }
        }

        // Button for saving filtered cities to file
        Button {
            id: saveButton
            Layout.fillWidth: true
            text: "Uložit"

            onClicked: saveFileDialog.open()
        }
    }

    Rectangle {
        Layout.fillWidth: true
        Layout.fillHeight: true

        // Dialog for choosing file to save filtered cities
        FileDialog {
            id: saveFileDialog
            title: "Vyberte soubor pro uložení vyfiltrovaných měst"
            folder: shortcuts.home
            selectExisting: false
            defaultSuffix: "json"
            nameFilters: ["*.json"]
            onAccepted: {
                console.log("Vybrali jste soubor: " + saveFileDialog.fileUrl)
                filtrModel.output_file = saveFileDialog.fileUrl.toString().replace("file:///","")
                filtrModel.save_to_file()
                Qt.quit()
            }
            onRejected: Qt.quit()
        }

        // The map component
        Plugin {
                id: mapPlugin
                name: "osm"
                PluginParameter {
                    name:"osm.mapping.custom.host"
                    value:"https://www.openstreetmap.org/#map"
                }
            }

        Map {
            id: mapaObce
            width: parent.width
            height: parent.height

            plugin: mapPlugin
            activeMapType: supportedMapTypes[supportedMapTypes.length - 3]

            // Center set to show the Czech Republic
            center: QtPositioning.coordinate(49.7437572, 15.3386383)
            zoomLevel: 7.5

            MapItemView {
                model: filtrModel
                delegate: MapQuickItem {
                    coordinate: model.location
                    sourceItem: Column {
                        spacing: 2
                        Image {
                            height: 50
                            width: 50
                            fillMode: Image.PreserveAspectFit
                            //source: "http://i.kym-cdn.com/entries/icons/original/000/002/144/You_Shall_Not_Pass!_0-1_screenshot.jpg" //funguje
                            source: model.znak
                        }
                        Text {
                            text: model.display
                            color: {
                                color = "black"
                                if (model.typ == "město v Česku")
                                    color = "red"
                            }
                            font.bold: {
                                font.bold = false
                                if (model.typ == "město v Česku")
                                    font.bold = true
                            }                        
                        }
                        Rectangle {
                            height: 7
                            width: 7
                            radius: 360
                            color: 'black'
                        }
                    }
                }
            }
        }
    }
    
    // List of all filtered cities displaying name, area, population, region and symbol
    ListView {
        id: cityList
        width: 160
        height: parent.height
        focus: true
        Layout.alignment: Qt.AlignTop
        Layout.fillHeight: true
        currentIndex : -1

        Component {
            id: cityListDelegate
            Item {
                width: parent.width
                height: childrenRect.height
                Column {
                    bottomPadding: 8
                    spacing: 2
                    Text {
                        text: model.display
                        color: {
                            color = "black"
                            if (model.typ == "město v Česku")
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
                    
                    Image {
                        height:100
                        width: parent.width
                        fillMode: Image.PreserveAspectFit
                        //source: "http://i.kym-cdn.com/entries/icons/original/000/002/144/You_Shall_Not_Pass!_0-1_screenshot.jpg" //funguje"
                        source: model.znak
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

        // When current item of the list is changed, update the currentModelItem property and center of the map
        onCurrentItemChanged: {
            currentModelItem = cityListDelegateModel.items.get(cityList.currentIndex).model
            mapaObce.center= currentModelItem.location
            mapaObce.zoomLevel = 12}

        highlight: Rectangle {
            color: "lightsteelblue"
        }
    }
}