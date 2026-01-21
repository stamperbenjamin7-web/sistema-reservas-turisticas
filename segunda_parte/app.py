import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
)

class SistemaReservas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Reservas Turísticas - Aruba")
        self.setGeometry(200, 200, 700, 500)

        layout = QVBoxLayout()

        # Título
        titulo = QLabel("Administración de Reservas Turísticas")
        layout.addWidget(titulo)

        # Campos de entrada
        self.input_cliente = QLineEdit()
        self.input_cliente.setPlaceholderText("Nombre del cliente")

        self.input_actividad = QLineEdit()
        self.input_actividad.setPlaceholderText("Actividad turística")

        self.input_fecha = QLineEdit()
        self.input_fecha.setPlaceholderText("Fecha (YYYY-MM-DD)")

        self.input_personas = QLineEdit()
        self.input_personas.setPlaceholderText("Número de personas")

        layout.addWidget(self.input_cliente)
        layout.addWidget(self.input_actividad)
        layout.addWidget(self.input_fecha)
        layout.addWidget(self.input_personas)

        # Botón agregar
        boton_agregar = QPushButton("Agregar Reserva")
        boton_agregar.clicked.connect(self.agregar_reserva)
        layout.addWidget(boton_agregar)

        # Tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels([
            "Cliente", "Actividad", "Fecha", "Personas"
        ])
        layout.addWidget(self.tabla)

        # Botón salir
        boton_salir = QPushButton("Salir")
        boton_salir.clicked.connect(self.close)
        layout.addWidget(boton_salir)

        self.setLayout(layout)

    def agregar_reserva(self):
        cliente = self.input_cliente.text()
        actividad = self.input_actividad.text()
        fecha = self.input_fecha.text()
        personas = self.input_personas.text()

        if not cliente or not actividad or not fecha or not personas:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        fila = self.tabla.rowCount()
        self.tabla.insertRow(fila)

        self.tabla.setItem(fila, 0, QTableWidgetItem(cliente))
        self.tabla.setItem(fila, 1, QTableWidgetItem(actividad))
        self.tabla.setItem(fila, 2, QTableWidgetItem(fecha))
        self.tabla.setItem(fila, 3, QTableWidgetItem(personas))

        # Limpiar campos
        self.input_cliente.clear()
        self.input_actividad.clear()
        self.input_fecha.clear()
        self.input_personas.clear()

        QMessageBox.information(self, "Éxito", "Reserva agregada correctamente")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SistemaReservas()
    ventana.show()
    sys.exit(app.exec())
