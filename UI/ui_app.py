# UI


import sys
import os
import arabic_reshaper
import pandas as pd
import chardet   
import csv       
from bidi.algorithm import get_display
from PyQt6 import QtWidgets, QtCore, QtGui, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPdfWriter, QPainter, QPageSize
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QMarginsF, QDateTime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from ai.ai_client import AIClient
 
 # مدیریت مسیر فایل‌ها در حالت اجرا و خروجی نهایی
 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# مدل نمایش داده‌ها در جدول

class PandasModel(QtCore.QAbstractTableModel):

    def __init__(self, df=pd.DataFrame()):
        super().__init__()
        self._df = df

    def rowCount(self, parent=None):
        return len(self._df.index)

    def columnCount(self, parent=None):
        return len(self._df.columns)

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):

        if not index.isValid():
            return None

        value = self._df.iloc[index.row(), index.column()]

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return str(value)

        if role == QtCore.Qt.ItemDataRole.TextAlignmentRole:
            if pd.api.types.is_numeric_dtype(self._df.iloc[:, index.column()]):
                return int(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
            return int(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)

        if role == QtCore.Qt.ItemDataRole.BackgroundRole:
            if index.row() % 2 == 0:
                return QtGui.QColor("#ffffff")
            return QtGui.QColor("#f8fafc")

        return None

    def headerData(self, section, orientation, role):

        if role != QtCore.Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == QtCore.Qt.Orientation.Horizontal:
            return str(self._df.columns[section])

        return str(section + 1)

# مدیریت رابط اصلی برنامه

class Ui_App(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        icon_path = resource_path("ui/logo.ico")
        self.setWindowIcon(QtGui.QIcon(icon_path))


        intro_ui = resource_path("ui/Intro.ui")
        data_ui = resource_path("ui/data_select_page.ui")

        self.stacked = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked)

        self.intro_page = QtWidgets.QWidget()
        uic.loadUi(intro_ui, self.intro_page)
        self.stacked.addWidget(self.intro_page)

        self.data_page = QtWidgets.QWidget()
        uic.loadUi(data_ui, self.data_page)
        self.stacked.addWidget(self.data_page)

        
        results_ui = resource_path("ui/result_core.ui")
        self.results_page = uic.loadUi(results_ui)
        self.stacked.addWidget(self.results_page)
        
                
        ai_ui = resource_path("ui/analysis_ai_page.ui")
        self.ai_page = uic.loadUi(ai_ui)
        self.stacked.addWidget(self.ai_page)

        self.ai_client = AIClient() 
        self.ai_controller = AIAnalysisController(self.ai_page, self)




        self.find_widgets()
        self.connect_buttons()

        self.prepare_drag_drop()
        self.prepare_table()

        self.dataframe = None
        self.model = None

        self.result_controller = ResultPageController(self.results_page, self)  

        self.wait_label = QtWidgets.QLabel("چند لحظه منتظر بمانید...", self.results_page)  
        self.wait_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.wait_label.setStyleSheet("font-size: 18px; background: rgba(255,255,255,220); padding: 20px; border-radius: 10px;")  # <--- اضافه شد
        self.wait_label.setGeometry(0, 0, 400, 100)  
        self.wait_label.hide()  
        self.wait_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)  
        if self.result_controller.table:  
            self.wait_label.raise_()  

        print("UI Ready")
        
    # دریافت ویجت‌های رابط کاربری

    def find_widgets(self):

        self.btn_start = self.intro_page.findChild(QtWidgets.QPushButton, "btn_next")
        self.btn_about = self.intro_page.findChild(QtWidgets.QPushButton, "pushButton_2")
        self.btn_exit = self.intro_page.findChild(QtWidgets.QPushButton, "pushButton_3")

        self.btn_back = self.data_page.findChild(QtWidgets.QPushButton, "btn_back")
        self.btn_analyze = self.data_page.findChild(QtWidgets.QPushButton, "btn_start")  

        self.btn_clear_file = self.data_page.findChild(QtWidgets.QPushButton, "btn_clear_file")

        self.drop_label = self.data_page.findChild(QtWidgets.QLabel, "drop_label")
        self.credit_label = self.data_page.findChild(QtWidgets.QLabel, "label_2")

        self.table = self.data_page.findChild(QtWidgets.QTableView, "table_preview")

        if not self.table:
            self.table = self.data_page.findChild(QtWidgets.QTableView, None)

        if self.table:
            print("✅ Found Table 'table_preview'.")
        else:
            print("❌ Table not found!")
            for child in self.data_page.findChildren(QtWidgets.QTableView):
                print("🔍 Trying:", child.objectName())
                if child.objectName() == "table_preview":
                    self.table = child
                    print("✅ Found table by fallback search!")
                    break
    # اتصال دکمه‌ها به رویدادها
    
    def connect_buttons(self):

        if self.btn_start:
            self.btn_start.clicked.connect(self.show_data_page)

        if self.btn_about:
            self.btn_about.clicked.connect(self.show_about)

        if self.btn_exit:
            self.btn_exit.clicked.connect(QtWidgets.QApplication.quit)

        if self.btn_back:
            self.btn_back.clicked.connect(self.show_intro_page)

        if self.btn_analyze:
            self.btn_analyze.clicked.connect(self.start_full_analysis)  

        if self.btn_clear_file:
            self.btn_clear_file.clicked.connect(self.clear_file)
            print("✅ btn_clear_file connected!")
        else:
            print("❌ btn_clear_file not found")



    def show_data_page(self):
        self.stacked.setCurrentWidget(self.data_page)

    def show_intro_page(self):
        self.reset_data_page()
        self.stacked.setCurrentWidget(self.intro_page)

    def show_results_page(self):
        self.stacked.setCurrentWidget(self.results_page)

    def show_data_select_page(self):
        self.stacked.setCurrentWidget(self.data_page)

    def show_about(self):
        dialog = QtWidgets.QDialog(self)
        uic.loadUi(resource_path("ui/about.ui"), dialog)

        btn_close = dialog.findChild(QtWidgets.QPushButton, "btn_close")
        btn_close.clicked.connect(dialog.close)

        dialog.exec()
    # فعال‌سازی Drag & Drop فایل
    
    def prepare_drag_drop(self):

        if not self.drop_label:
            return

        self.drop_label.setAcceptDrops(True)

        def drag_enter(event):

            if event.mimeData().hasUrls():
                event.acceptProposedAction()
            else:
                event.ignore()

        def drop_event(event):

            urls = event.mimeData().urls()
            if urls:
                path = urls[0].toLocalFile()
                self.load_file(path)

        def mouse_click(event):

            if event.button() == QtCore.Qt.MouseButton.LeftButton:
                self.open_file_dialog()

        self.drop_label.dragEnterEvent = drag_enter
        self.drop_label.dropEvent = drop_event
        self.drop_label.mousePressEvent = mouse_click

    def open_file_dialog(self):

        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "Data Files (*.csv *.xlsx *.xls)"
        )

        if file:
            self.load_file(file)

    # بارگذاری و آماده‌سازی فایل داده
    
    def load_file(self, path):

        try:
            if path.endswith(".csv"):

                with open(path, "rb") as f:
                    raw = f.read(50000)
                enc_guess = chardet.detect(raw)["encoding"]
                if not enc_guess:
                    enc_guess = "utf-8"

                with open(path, encoding=enc_guess, errors="replace") as f:
                    sniffer = csv.Sniffer()
                    sample = f.read(2048)
                    try:
                        delimiter = sniffer.sniff(sample).delimiter
                    except:
                        delimiter = ','

                df = pd.read_csv(
                    path,
                    encoding=enc_guess,
                    sep=delimiter,
                    on_bad_lines="skip",
                    engine="python"
                )

            else:
                df = pd.read_excel(path)

            file_name = os.path.basename(path)
            
            self.current_file_name = file_name


            if df.columns.tolist()[0] is None or str(df.columns[0]).isdigit():
                df.columns = [f"ستون {i+1}" for i in range(len(df.columns))]

            extra_row = [None] * len(df.columns)

            top_row = pd.DataFrame([extra_row], columns=df.columns)
            df = pd.concat([top_row, df], ignore_index=True)

            self.dataframe = df
            self.show_table(df)

            self.drop_label.setText("File Loaded ✔️")

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))
    # بازنشانی کامل صفحه داده
    
    def reset_data_page(self):

        self.dataframe = None
        self.model = None

        if self.table:
            self.table.setModel(None)
            self.table.clearSelection()
            self.table.reset()
            self.table.viewport().update()
            self.table.repaint()              
            QtWidgets.QApplication.processEvents()

        if self.drop_label:
            self.drop_label.setText("Drop file here or click to load")


    def clear_file(self):
        self.dataframe = None
        self.model = None

        if self.table:
            self.table.setModel(None)
            self.table.clearSelection()
            self.table.reset()
            self.table.viewport().update()
            self.table.repaint()              # <--- مهم
            QtWidgets.QApplication.processEvents()

        if self.drop_label:
            self.drop_label.setText("Drop file here or click to load")
    # تنظیمات جدول نمایش داده
    
    def prepare_table(self):

        if not self.table:
            return

        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )

        self.table.horizontalHeader().setMinimumSectionSize(120)
        self.table.verticalHeader().setVisible(False)

        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)

        self.table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectColumns
        )

        self.table.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )

        self.table.setStyleSheet("""

QTableView {
    background: #ffffff;
    alternate-background-color: #ffffff;
    gridline-color: #d0d7de;
    selection-background-color: #cce5ff;
    selection-color: #000000;
    border: 1px solid #d0d7de;
    border-radius: 3px;
    font-size: 13px;
}

QTableView::item {
    padding: 4px 6px;
    border-right: 1px solid #d0d7de;
    border-bottom: 1px solid #d0d7de;
}

QHeaderView::section {
    background-color: #f3f4f6;
    padding: 6px 8px;
    border-right: 1px solid #d0d7de;
    border-bottom: 1px solid #d0d7de;
    font-weight: normal;
    font-size: 13px;
}

QTableCornerButton::section {
    background-color: #f3f4f6;
    border-right: 1px solid #d0d7de;
    border-bottom: 1px solid #d0d7de;
}

        """)
    # نمایش داده‌ها در جدول
    
    def show_table(self, df):

        if not self.table:
            print("table not found")
            return

        df_preview = df.head(500)

        self.model = PandasModel(df_preview)
        self.table.setModel(self.model)

        self.table.resizeColumnsToContents()

        QtWidgets.QApplication.processEvents()
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    # اجرای کامل تحلیل داده
    
    def start_full_analysis(self):  

        if self.dataframe is None:

            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "Load a file first"
            )
            return

        indexes = self.table.selectionModel().selectedColumns()

        if not indexes:

            QtWidgets.QMessageBox.information(
                self,
                "Info",
                "Select a column"
            )
            return

        col = indexes[0].column()
        col_name = self.dataframe.columns[col]

        self.stacked.setCurrentWidget(self.results_page)
        QtWidgets.QApplication.processEvents()

        self.center_wait_label()
        self.wait_label.show()
        self.wait_label.raise_()
        QtWidgets.QApplication.processEvents()

        result = self.result_controller.run_analysis(self.dataframe, col_name)
        self.result_controller.display_results(result)

        self.wait_label.hide()

    def center_wait_label(self):  
        if not self.result_controller.table:
            return
        table_geom = self.result_controller.table.geometry()
        label_w = self.wait_label.width()
        label_h = self.wait_label.height()
        x = table_geom.x() + (table_geom.width() - label_w) // 2
        y = table_geom.y() + (table_geom.height() - label_h) // 2
        self.wait_label.setGeometry(x, y, label_w, label_h)
        
# مدیریت صفحه نتایج تحلیل
        
class ResultPageController:

    def __init__(self, page_widget, app_window):

        self.page = page_widget
        self.app_window = app_window

        print("=== CHILDREN OF RESULT PAGE ===")
        for w in self.page.findChildren(QtWidgets.QWidget):
            print(type(w).__name__, "->", w.objectName())
        print("================================")


        self.table = self.page.findChild(QtWidgets.QTableView, "table_results", Qt.FindChildOption.FindChildrenRecursively)
        self.btn_back = self.page.findChild(QtWidgets.QPushButton, "btn_back")
        self.btn_save = self.page.findChild(QtWidgets.QPushButton, "btn_save")
        self.btn_ai = self.page.findChild(QtWidgets.QPushButton, "btn_ai")

        self._setup_table()
        self._connect_buttons()


    def _setup_table(self):

        if not isinstance(self.table, QtWidgets.QTableView):
            return

        self.model = QtGui.QStandardItemModel()

        self.model.setHorizontalHeaderLabels([
            "📊 بخش",
            "🔎 پارامتر",
            "📈 مقدار"
        ])

        self.table.setModel(self.model)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.table.verticalHeader().setVisible(False)

        self.table.setAlternatingRowColors(True)

        self.table.setStyleSheet("""
        QTableView{
            background:#ffffff;
            alternate-background-color:#f5f7fb;
            border:1px solid #e3e6ee;
            font-size:13px;
        }

        QHeaderView::section{
            background:#eef2f7;
            padding:6px;
            border:none;
            font-weight:bold;
        }
        """)

        self.table.verticalHeader().setDefaultSectionSize(28)

        self.table.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )




    def _connect_buttons(self):

        if self.btn_back:
            self.btn_back.clicked.connect(self.back_clicked)

        if self.btn_save:
            self.btn_save.clicked.connect(self.save_clicked)

        if self.btn_ai:
            self.btn_ai.clicked.connect(self.ai_clicked)


    def clean_numeric_column(self, series):

        series = pd.to_numeric(series, errors="coerce")

        series = series.dropna()

        return series

    # اجرای تحلیل آماری روی ستون انتخاب‌شده
    
    def run_analysis(self, df, column_name):
        import pandas as pd
        import numpy as np
        from core.numpy_analysis import run_numpy_analysis

        if df is None or column_name not in df.columns:
            print("❌ DataFrame یا ستون معتبر نیست")
            return None

        column_data = df[column_name]

        if isinstance(column_data, pd.DataFrame):
            column_data = column_data.iloc[:, 0]

        column_data = column_data.apply(lambda x: x[0] if isinstance(x, (list, tuple)) and len(x) == 1 else x)

        column_data = pd.to_numeric(column_data, errors="coerce").dropna()

        if column_data.empty:
            print("❌ ستون عددی معتبری برای تحلیل وجود ندارد")
            return None

        data_list = column_data.tolist()

        data_array = np.array(data_list)

        result_dict = run_numpy_analysis(data_array)
        
        result_dict["اسم فایل"] = getattr(self.app_window, "current_file_name", "")
        result_dict["ستون انالیز شده"] = column_name
        result_dict["تعداد سطر ها"] = len(data_array)

        
        print(result_dict)


        return result_dict




    def add_row(self, section, param, value):

        s = QtGui.QStandardItem(str(section))
        p = QtGui.QStandardItem(str(param))
        v = QtGui.QStandardItem(str(value))

        s.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        p.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        v.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.model.appendRow([s, p, v])

    # نمایش نتایج تحلیل در جدول
    
    def display_results(self, result_dict):
        self.model.removeRows(0, self.model.rowCount())

        file_name = result_dict.get("اسم فایل", "")
        column_name = result_dict.get("ستون انالیز شده", "")
        row_count = result_dict.get("تعداد سطر ها", "")

        self.add_row("📁 فایل", "نام فایل", file_name)
        self.add_row("📊 ستون", "ستون تحلیل شده", column_name)
        self.add_row("📑 داده", "تعداد سطر", row_count)

        analysis = result_dict
        stats = analysis.get("وضعیت کلی داده", {})

        mean_val = stats.get("میانگین", "")
        std_val = stats.get("انحراف معیار", "")
        total_rows = stats.get("تعداد ردیف ها", "")

        self.add_row("📈 آمار", "میانگین", mean_val)
        self.add_row("📈 آمار", "انحراف معیار", std_val)
        self.add_row("📈 آمار", "تعداد ردیف", total_rows)

        z = analysis.get("محاسبه با z-scores ", {})
        
        print(
            "REAL Z OUTLIERS LEN =",
            len(z.get("داده های ناهنجار", []))
        )


        z_data_count = z.get("تعداد دیتا های دریافت شده", "")
        z_outlier_count = z.get("تعداد ناهنجاری ها", "")
        z_outlier_percent = z.get("درصد ناهنجاری به کل", "")

        self.add_row("🧠 ZScore", "تعداد داده", z_data_count)
        self.add_row("🧠 ZScore", "تعداد ناهنجاری", z_outlier_count)
        self.add_row("🧠 ZScore", "درصد", z_outlier_percent)

        for item in z.get("داده های ناهنجار", []):
            txt = f"⚠️ {item.get('مقدار')} | ریسک {item.get('مقدار ریسک')} | سطح {item.get('اندازه ناهنجاری')}"
            self.add_row("🧠 ZScore", "ناهنجاری", txt)

        iqr = analysis.get("محاسبه با IQR", {})

        iqr_total = iqr.get("مجموع تمام داده ها ", "")
        iqr_outlier_count = iqr.get("تعداد ناهنجاری ها ", "")
        iqr_outlier_percent = iqr.get("نسبت ناهنجاری ها به کل", "")

        self.add_row("📐 IQR", "کل داده", iqr_total)
        self.add_row("📐 IQR", "تعداد ناهنجاری", iqr_outlier_count)
        self.add_row("📐 IQR", "درصد", iqr_outlier_percent)

        for item in iqr.get("ناهنجاری ها ", []):
            txt = f"⚠️ {item.get('داده ناهنجار ')} | ریسک {item.get('نمره ریسک')} | سطح {item.get('شدت ناهنجاری ')}"
            self.add_row("📐 IQR", "ناهنجاری", txt)
            
        iso = analysis.get("محاسبه با Isolation Forest", {})
        
        iso_total = iso.get("تعداد کل داده ها", "")
        iso_outlier_count = iso.get("تعداد ناهنجاری ها", "")
        iso_outlier_percent = iso.get("درصد ناهنجاری", "")

        self.add_row("🌲 Isolation", "کل داده", iso_total)
        self.add_row("🌲 Isolation", "تعداد ناهنجاری", iso_outlier_count)
        self.add_row("🌲 Isolation", "درصد", f"{iso_outlier_percent:.2f}%")

        for item in iso.get("داده های ناهنجار", []):
            txt = f"⚠️ {item.get('مقدار')} | ریسک {item.get('نمره ریسک')} | سطح {item.get('شدت ناهنجاری')}"
            self.add_row("🌲 Isolation", "ناهنجاری", txt)


    def back_clicked(self):

        self.app_window.show_data_select_page()

    # ذخیره گزارش تحلیل به PDF
    
    def save_clicked(self):

        path, _ = QFileDialog.getSaveFileName(
            self.page,
            "ذخیره گزارش تحلیل",
            "analysis_report.pdf",
            "PDF Files (*.pdf)"
        )

        if not path:
            return

        pdf = QPdfWriter(path)
        pdf.setPageSize(QPageSize(QPageSize.PageSizeId.A4))
        pdf.setResolution(300)
        pdf.setPageMargins(QMarginsF(12, 12, 12, 12))

        painter = QPainter()

        if not painter.begin(pdf):
            print("PDF painter error")
            return

        model = self.table.model()

        if model is None:
            painter.end()
            return

        page_width = pdf.width()
        page_height = pdf.height()

        margin_x = 120
        top_margin = 110
        bottom_margin = 120
        content_width = page_width - (margin_x * 2)

        title_font = QtGui.QFont("Segoe UI", 20, QtGui.QFont.Weight.Bold)
        subtitle_font = QtGui.QFont("Segoe UI", 13)
        header_font = QtGui.QFont("Segoe UI", 13, QtGui.QFont.Weight.Bold)
        cell_font = QtGui.QFont("Segoe UI", 12)
        warning_title_font = QtGui.QFont("Segoe UI", 18, QtGui.QFont.Weight.Bold)
        warning_font = QtGui.QFont("Segoe UI", 20)

        title_bg = QtGui.QColor("#d9e4f5")
        title_text = QtGui.QColor("#374151")
        header_bg = QtGui.QColor("#e8f3ff")
        header_border = QtGui.QColor("#bcd7f5")
        cell_border = QtGui.QColor("#d0d7e2")
        row_even = QtGui.QColor("#ffffff")
        row_odd = QtGui.QColor("#f9fafb")
        anomaly_bg = QtGui.QColor("#fff4e5")
        anomaly_text = QtGui.QColor("#9a3412")
        normal_text = QtGui.QColor("#2f3640")
        warning_bg = QtGui.QColor("#fff7e6")
        warning_border = QtGui.QColor("#f0c36d")
        warning_text = QtGui.QColor("#6b4f1d")

        title_height = 135
        meta_height = 68
        header_height = 105
        row_height = 125

        padding_x = 30
        padding_y = 28

        headers = []
        for c in range(model.columnCount()):
            headers.append(model.headerData(c, Qt.Orientation.Horizontal))

        col_widths = [
            int(content_width * 0.22),
            int(content_width * 0.28),
            int(content_width * 0.50)
        ]

        warning_label = self.page.findChild(QtWidgets.QLabel, "label_warning")
        warning_text_value = ""
        if warning_label:
            warning_text_value = warning_label.text()

        def draw_top_block(current_y):
            rect = QtCore.QRectF(margin_x, current_y, content_width, title_height)
            painter.fillRect(rect, title_bg)
            painter.setPen(QtGui.QPen(QtGui.QColor("#c7d7ee")))
            painter.drawRoundedRect(rect, 10, 10)

            painter.setPen(title_text)
            painter.setFont(title_font)
            painter.drawText(
                rect,
                int(Qt.AlignmentFlag.AlignCenter),
                "نتایج تحلیل آماری (NumPy)"
            )

            current_y += title_height + 28

            painter.setPen(QtGui.QColor("#4b5563"))
            painter.setFont(subtitle_font)
            current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm")
            painter.drawText(
                QtCore.QRectF(margin_x, current_y, content_width, meta_height),
                int(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter),
                f"تاریخ ایجاد گزارش: {current_time}"
            )

            current_y += meta_height + 42
            return current_y

        def draw_table_header(current_y):
            x = margin_x
            painter.setFont(header_font)

            for i, text in enumerate(headers):
                rect = QtCore.QRectF(x, current_y, col_widths[i], header_height)
                painter.fillRect(rect, header_bg)
                painter.setPen(QtGui.QPen(header_border))
                painter.drawRect(rect)

                painter.setPen(QtGui.QColor("#1f2937"))
                painter.drawText(
                    rect.adjusted(padding_x, padding_y, -padding_x, -padding_y),
                    int(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter),
                    str(text)
                )
                x += col_widths[i]

            return current_y + header_height + 25

        def draw_warning_box(current_y):

            if not warning_text_value.strip():
                return current_y

            current_y += 110

            text_rect = QtCore.QRectF(
                margin_x + 42,
                current_y + 120,
                content_width - 84,
                520
            )

            painter.setFont(warning_font)

            text_option = QtGui.QTextOption()
            text_option.setWrapMode(QtGui.QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
            text_option.setAlignment(Qt.AlignmentFlag.AlignRight)

            text_doc = QtGui.QTextDocument()
            text_doc.setDefaultFont(warning_font)
            text_doc.setTextWidth(text_rect.width())
            text_doc.setPlainText(warning_text_value)

            doc_height = text_doc.size().height()

            box_height = int(doc_height) + 240

            rect = QtCore.QRectF(
                margin_x,
                current_y,
                content_width,
                box_height
            )

            painter.fillRect(rect, warning_bg)

            painter.setPen(QtGui.QPen(warning_border, 2))
            painter.drawRoundedRect(rect, 18, 18)

            painter.setPen(warning_text)
            painter.setFont(warning_title_font)

            painter.drawText(
                QtCore.QRectF(
                    margin_x + 38,
                    current_y + 34,
                    content_width - 76,
                    52
                ),
                int(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter),
                "⚠️ توجه"
            )

            painter.save()

            painter.translate(text_rect.topLeft())
            text_doc.drawContents(painter)

            painter.restore()

            return current_y + box_height + 30

        y = top_margin
        y = draw_top_block(y)
        y = draw_table_header(y)

        for r in range(model.rowCount()):
            if y + row_height > page_height - bottom_margin - 200:
                pdf.newPage()
                y = top_margin
                y = draw_top_block(y)
                y = draw_table_header(y)

            x = margin_x
            row_values = []

            for c in range(model.columnCount()):
                index = model.index(r, c)
                data = model.data(index)
                row_values.append("" if data is None else str(data))

            is_anomaly_row = any("ناهنجاری" in v or "⚠" in v for v in row_values)

            for c in range(model.columnCount()):
                rect = QtCore.QRectF(x, y, col_widths[c], row_height)

                if is_anomaly_row:
                    bg = anomaly_bg
                    text_color = anomaly_text
                else:
                    bg = row_even if r % 2 == 0 else row_odd
                    text_color = normal_text

                painter.fillRect(rect, bg)
                painter.setPen(QtGui.QPen(cell_border))
                painter.drawRect(rect)

                painter.setPen(text_color)
                painter.setFont(cell_font)
                painter.drawText(
                    rect.adjusted(padding_x, padding_y, -padding_x, -padding_y),
                    int(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop),
                    row_values[c]
                )

                x += col_widths[c]

            y += row_height + 34

        y = draw_warning_box(y)

        painter.end()
        print("PDF saved successfully")



    def ai_clicked(self):

          self.app_window.stacked.setCurrentWidget(
        self.app_window.ai_page
    )

# مدیریت تحلیل هوشمند و گزارش AI

class AIAnalysisController:

    def __init__(self, page_widget, app_window):

        self.page = page_widget
        self.app_window = app_window

        self.table = self.page.findChild(QtWidgets.QTextEdit, "ai_output_box")
        self.btn_back = self.page.findChild(QtWidgets.QPushButton, "btn_back")
        self.btn_save = self.page.findChild(QtWidgets.QPushButton, "btn_save")
        self.btn_ai = self.page.findChild(QtWidgets.QPushButton, "btn_ai")

        self._setup_table()
        self._connect_buttons()

        self.wait_label = QtWidgets.QLabel("در حال تحلیل هوشمند و تدوین راهکارهای مدیریتی...", self.page)
        self.wait_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wait_label.setStyleSheet("font-size: 18px; background: rgba(255,255,255,220); padding: 20px; border-radius: 10px;")
        self.wait_label.setGeometry(0, 0, 420, 110)
        self.wait_label.hide()
        self.wait_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)


    def _setup_table(self):

        if isinstance(self.table, QtWidgets.QTableView):

            self.model = QtGui.QStandardItemModel()
            self.table.setModel(self.model)

            header = self.table.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

            self.table.verticalHeader().setVisible(False)
            self.table.setAlternatingRowColors(True)

            self.table.setStyleSheet("""
        QTableView{
            background:#ffffff;
            alternate-background-color:#f5f7fb;
            border:1px solid #e3e6ee;
            font-size:13px;
        }

        QHeaderView::section{
            background:#eef2f7;
            padding:6px;
            border:none;
            font-weight:bold;
        }
        """)

            self.table.verticalHeader().setDefaultSectionSize(28)

            self.table.setSelectionBehavior(
                QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
            )

            self.table.setSelectionMode(
                QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
            )


    def _connect_buttons(self):

        if self.btn_back:
            self.btn_back.clicked.connect(self.back_clicked)

        if self.btn_save:
            self.btn_save.clicked.connect(self.save_clicked)

        if self.btn_ai:
            self.btn_ai.clicked.connect(self.ai_clicked)


    def center_wait_label(self):
        table_geom = self.table.geometry()
        label_w = self.wait_label.width()
        label_h = self.wait_label.height()
        x = table_geom.x() + (table_geom.width() - label_w) // 2
        y = table_geom.y() + (table_geom.height() - label_h) // 2
        self.wait_label.setGeometry(x, y, label_w, label_h)

    # اجرای تحلیل هوشمند با AI
    
    def ai_clicked(self):

        self.app_window.stacked.setCurrentWidget(self.page)

        QtWidgets.QApplication.processEvents()

        self.center_wait_label()
        self.wait_label.show()
        self.wait_label.raise_()
        QtWidgets.QApplication.processEvents()

        try:

            prompt_path = resource_path("ui/ai_prompt.txt")

            
            from ai.prompt_builder import build_ai_prompt

            df = self.app_window.dataframe
            indexes = self.app_window.table.selectionModel().selectedColumns()

            if not indexes:
                raise Exception("ستونی انتخاب نشده")

            col = indexes[0].column()
            col_name = df.columns[col]

            analysis = self.app_window.result_controller.run_analysis(df, col_name)

            prompt_text = build_ai_prompt(col_name, df, analysis)
            
            print("\n================ PROMPT SENT TO AI ================\n")
            print(prompt_text)
            print("\n================ END PROMPT =======================\n")


            with open(prompt_path, "w", encoding="utf-8") as f:
                f.write(prompt_text)


            ai_response = self.app_window.ai_client.analyze(
                prompt_file=prompt_path
            )

            self.display_ai_results(ai_response)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self.page, "خطا در تحلیل", str(e))

        finally:
            self.wait_label.hide()


    # نمایش پاسخ تحلیل هوش مصنوعی
    
    def display_ai_results(self, response):

        self.table.clear()

        if not response:
            return

        self.table.setPlainText(str(response))
    
    # ذخیره گزارش AI به صورت PDF
        
    def export_ai_analysis_pdf(self, text, filename):
        import os

        from PyQt6.QtGui import QTextDocument, QFontDatabase, QFont
        from PyQt6.QtPrintSupport import QPrinter

        font_path = resource_path("ui/Vazir.ttf")

        font_id = QFontDatabase.addApplicationFont(font_path)

        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        else:
            font_family = "Tahoma"

        formatted_text = text.replace("\n", "<br>")

        html = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    direction: rtl;
                    text-align: right;
                    font-family: '{font_family}';
                    font-size: 11pt;
                    line-height: 1.8;
                    padding: 20px;
                }}

                h1 {{
                    text-align: center;
                    font-size: 18pt;
                    margin-bottom: 25px;
                }}
            </style>
        </head>

        <body>
            <h1>گزارش تحلیل هوشمند و راهکارهای مدیریتی</h1>

            {formatted_text}

        </body>
        </html>
        """

        document = QTextDocument()

        font = QFont(font_family, 11)
        document.setDefaultFont(font)

        document.setHtml(html)

        printer = QPrinter()
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(filename)

        document.print(printer)


    def back_clicked(self):

        self.table.clear()
        self.app_window.show_results_page()


    def save_clicked(self):

        path, _ = QFileDialog.getSaveFileName(
            self.page,
            "ذخیره تحلیل هوش مصنوعی",
            "ai_analysis_report.pdf",
            "PDF Files (*.pdf)"
        )

        if not path:
            return

        text = self.table.toPlainText()
        self.export_ai_analysis_pdf(text, path)

        print("AI PDF saved successfully")
