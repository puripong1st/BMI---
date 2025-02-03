import requests
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line2 = QtWidgets.QLineEdit(self.frame)
        self.line2.setGeometry(QtCore.QRect(270, 150, 231, 41))
        self.line2.setText("")
        self.line2.setObjectName("line2")
        self.line1 = QtWidgets.QLineEdit(self.frame)
        self.line1.setGeometry(QtCore.QRect(270, 230, 231, 41))
        self.line1.setText("")
        self.line1.setObjectName("line1")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(280, 290, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(180, 140, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(180, 220, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Add input validators
        validator = QtGui.QDoubleValidator(0.0, 999.9, 2)  # Allow numbers from 0.0 to 999.9 with 2 decimal places
        validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.line1.setValidator(validator)
        self.line2.setValidator(validator)

        # Connect button click to calculate BMI
        self.pushButton.clicked.connect(self.calculate_bmi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "โปรแกรมคำนวณ BMI"))
        self.line2.setPlaceholderText(_translate("MainWindow", "ใส่ส่วนสูง (cm)"))
        self.line1.setPlaceholderText(_translate("MainWindow", "ใส่น้ำหนัก (kg)"))
        self.pushButton.setText(_translate("MainWindow", "คำนวณ"))
        self.label1.setText(_translate("MainWindow", "ส่วนสูง"))
        self.label2.setText(_translate("MainWindow", "น้ำหนัก"))

    def calculate_bmi(self):
        try:
            height_cm = float(self.line2.text())
            weight_kg = float(self.line1.text())
            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)

            if bmi < 18.5:
                result = "น้ำหนักน้อย / ผอม - ภาวะเสี่ยง: มากกว่าคนปกติ"
            elif 18.5 <= bmi <= 22.9:
                result = "ปกติ (สุขภาพดี) - ภาวะเสี่ยง: เท่าคนปกติ"
            elif 23 <= bmi <= 24.9:
                result = "ท้วม / โรคอ้วนระดับ 1 - ภาวะเสี่ยง: อันตรายระดับ 1"
            elif 25 <= bmi <= 29.9:
                result = "อ้วน / โรคอ้วนระดับ 2 - ภาวะเสี่ยง: อันตรายระดับ 2"
            else:
                result = "อ้วนมาก / โรคอ้วนระดับ 3 - ภาวะเสี่ยง: อันตรายระดับ 3"

            # Display result in popup
            QtWidgets.QMessageBox.information(None, "ผลลัพธ์ BMI", f"BMI ของคุณคือ {bmi:.2f}\n{result}")

            # Send data to Discord
            self.send_to_discord(bmi, result)

        except ValueError:
            QtWidgets.QMessageBox.warning(None, "ข้อผิดพลาด", "กรุณาใส่ข้อมูลให้ถูกต้อง")

    def send_to_discord(self, bmi, result):
        webhook_url = "https://discord.com/api/webhooks/1335975411796148235/6d0dXwxyyzGRx7adHLCslOJATweY_gPP7yiNDEXGgq4LQNuEFPEzUPBgnFSJ6jnIj1Oa"  # Replace with your Discord Webhook URL
        data = {
            "content": f"ผลลัพธ์ BMI:\nBMI: {bmi:.2f}\nผล: {result}"
        }
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                QtWidgets.QMessageBox.information(None, "แจ้งเตือน", "ส่งข้อมูลไปยัง Discord สำเร็จ!")
            else:
                QtWidgets.QMessageBox.warning(None, "ข้อผิดพลาด", "ไม่สามารถส่งข้อมูลไปยัง Discord ได้")
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "ข้อผิดพลาด", f"เกิดข้อผิดพลาด: {str(e)}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
