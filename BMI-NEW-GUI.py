from PyQt5 import QtCore, QtGui, QtWidgets
import sys,requests,os

pc = os.getlogin()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(28, 30, 41);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line2 = QtWidgets.QLineEdit(self.frame)
        self.line2.setGeometry(QtCore.QRect(120, 80, 201, 41))
        self.line2.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #fff;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(34,36,44);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"}")
        self.line2.setText("")
        self.line2.setObjectName("line2")
        self.line1 = QtWidgets.QLineEdit(self.frame)
        self.line1.setGeometry(QtCore.QRect(120, 140, 201, 41))
        self.line1.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #fff;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(34,36,44);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"}")
        self.line1.setText("")
        self.line1.setObjectName("line1")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 20px;\n"
"    color: #fff;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    background-color: rgb(34,36,44);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(48,50,62);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(10, 70, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label1.setFont(font)
        self.label1.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(10, 130, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label2.setFont(font)
        self.label2.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label2.setObjectName("label2")
        self.label1_2 = QtWidgets.QLabel(self.frame)
        self.label1_2.setGeometry(QtCore.QRect(60, 10, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label1_2.setFont(font)
        self.label1_2.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label1_2.setObjectName("label1_2")
        self.label1_2.raise_()
        self.line2.raise_()
        self.line1.raise_()
        self.pushButton.raise_()
        self.label1.raise_()
        self.label2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        validator = QtGui.QDoubleValidator(0.0,999.9,2)
        validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.line1.setValidator(validator)
        self.line2.setValidator(validator)

        self.pushButton.clicked.connect(self.cal_bmi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "คำนวณ BMI - Puripong"))
        self.line2.setPlaceholderText(_translate("MainWindow", "ใส่ส่วนสูงเพื่อคำนวณ BMI"))
        self.line1.setPlaceholderText(_translate("MainWindow", "ใส่น้ำหนักเพื่อคำนวณ BMI"))
        self.pushButton.setText(_translate("MainWindow", "คำนวณ"))
        self.label1.setText(_translate("MainWindow", "ส่วนสูง"))
        self.label2.setText(_translate("MainWindow", "น้ำหนัก"))
        self.label1_2.setText(_translate("MainWindow", "คำนวณหาค่า BMI"))

    def cal_bmi(self):
        try:
            height_cm = float(self.line2.text())
            weight_kg = float(self.line1.text())
            height_m = height_cm /100
            bmi = weight_kg / (height_m **2)
            if bmi < 18.5:
                result = "น้ำหนักน้อย / ผอม	- ภาวะเสี่ยง : มากกว่าคนปกติ"
                print(result)
            elif 18.5 <= bmi <=22.9:
                result = "ปกติ (สุขภาพดี) - ภาวะเสี่ยง: เท่าคนปกติ"
                print(result)
            elif 23 <= bmi <= 24.9:
                result = "ท้วม / โรคอ้วนระดับ 1 - ภาวะเสี่ยง: อันตรายระดับ 1"
                print(result)
            elif 25 <= bmi <= 29.9:
                result = "อ้วน / โรคอ้วนระดับ 2 - ภาวะเสี่ยง: อันตรายระดับ 2"
                print(result)
            else:
                result = "อ้วนมาก / โรคอ้วนระดับ 3 - ภาวะเสี่ยง: อันตรายระดับ 3"
                print(result)

            QtWidgets.QMessageBox.information(None,"ผลลัพธ์ BMI", f"BMI ของคุณคือ {bmi:.2f}\n{result}")
            self.send_to_discord(bmi,result,height_cm,weight_kg)
        except ValueError:
            QtWidgets.QMessageBox.warning(None,"ข้อผิดพลาด","กรุณาใส่ข้อมูลให้ถูกต้อง")
    def send_to_discord(self,bmi,result,height_cm,weight_kg):
        webhook_url = "https://discord.com/api/webhooks/1335976933409820722/XEksDOC-5rlpILq-Ikpr7Hm5gYxCnLf8DY3YpEjnRjDkS8lNI2xQYTERFOJ5BPK4vAKh"
        data = {
            "content": f"ชื่อผู้ใช้งาน : {pc}\n ส่วนสูง : {height_cm} \n น้ำหนัก : {weight_kg} \nผลลัพธ์ BMI\nBMI: {bmi:.2f}\nผล: {result}"
        }
        try:
            response = requests.post(webhook_url,json=data)
            if response.status_code == 204:
                print("ส่งข้อมูลสำเร็จ")
            else:
                print("ส่งข้อมูลไม่สำเร็จ")
        except Exception  as e:
            print("เกิดข้อผิดพลาด"+ str(e))


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())