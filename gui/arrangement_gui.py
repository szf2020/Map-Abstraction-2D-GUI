# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arrangement_gui.ui'
#
# Created: Mon Feb 13 14:55:59 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1548, 1031)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_arrangement = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_arrangement.setGeometry(QtCore.QRect(220, 50, 1321, 931))
        self.graphicsView_arrangement.setObjectName("graphicsView_arrangement")
        self.groupBox_face_manipulation = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_face_manipulation.setGeometry(QtCore.QRect(10, 380, 191, 281))
        self.groupBox_face_manipulation.setObjectName("groupBox_face_manipulation")
        self.pushButton_merge_selected_faces = QtGui.QPushButton(self.groupBox_face_manipulation)
        self.pushButton_merge_selected_faces.setGeometry(QtCore.QRect(0, 150, 181, 30))
        self.pushButton_merge_selected_faces.setObjectName("pushButton_merge_selected_faces")
        self.pushButton_reset_face_selection = QtGui.QPushButton(self.groupBox_face_manipulation)
        self.pushButton_reset_face_selection.setGeometry(QtCore.QRect(0, 100, 180, 30))
        self.pushButton_reset_face_selection.setObjectName("pushButton_reset_face_selection")
        self.textEdit_face_semantic_label = QtGui.QTextEdit(self.groupBox_face_manipulation)
        self.textEdit_face_semantic_label.setGeometry(QtCore.QRect(0, 210, 181, 31))
        self.textEdit_face_semantic_label.setReadOnly(True)
        self.textEdit_face_semantic_label.setObjectName("textEdit_face_semantic_label")
        self.label_20 = QtGui.QLabel(self.groupBox_face_manipulation)
        self.label_20.setGeometry(QtCore.QRect(0, 190, 121, 16))
        self.label_20.setObjectName("label_20")
        self.pushButton_assign_label_to_selected_faces = QtGui.QPushButton(self.groupBox_face_manipulation)
        self.pushButton_assign_label_to_selected_faces.setGeometry(QtCore.QRect(0, 250, 181, 27))
        self.pushButton_assign_label_to_selected_faces.setObjectName("pushButton_assign_label_to_selected_faces")
        self.textEdit_selected_faces_list = QtGui.QTextEdit(self.groupBox_face_manipulation)
        self.textEdit_selected_faces_list.setGeometry(QtCore.QRect(0, 40, 181, 51))
        self.textEdit_selected_faces_list.setReadOnly(True)
        self.textEdit_selected_faces_list.setObjectName("textEdit_selected_faces_list")
        self.line = QtGui.QFrame(self.groupBox_face_manipulation)
        self.line.setGeometry(QtCore.QRect(30, 140, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.groupBox_face_manipulation)
        self.line_2.setGeometry(QtCore.QRect(30, 180, 118, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtGui.QLabel(self.groupBox_face_manipulation)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.label.setObjectName("label")
        self.groupBox_store = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_store.setGeometry(QtCore.QRect(10, 860, 191, 111))
        self.groupBox_store.setObjectName("groupBox_store")
        self.pushButton_save_arrangement_to_IEEE = QtGui.QPushButton(self.groupBox_store)
        self.pushButton_save_arrangement_to_IEEE.setGeometry(QtCore.QRect(10, 70, 161, 27))
        self.pushButton_save_arrangement_to_IEEE.setObjectName("pushButton_save_arrangement_to_IEEE")
        self.pushButton_save_arrangement_to_pickle = QtGui.QPushButton(self.groupBox_store)
        self.pushButton_save_arrangement_to_pickle.setGeometry(QtCore.QRect(10, 30, 161, 27))
        self.pushButton_save_arrangement_to_pickle.setObjectName("pushButton_save_arrangement_to_pickle")
        self.groupBox_arrangement = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_arrangement.setGeometry(QtCore.QRect(10, 120, 191, 221))
        self.groupBox_arrangement.setObjectName("groupBox_arrangement")
        self.pushButton_construct_arrangement = QtGui.QPushButton(self.groupBox_arrangement)
        self.pushButton_construct_arrangement.setGeometry(QtCore.QRect(20, 30, 141, 27))
        self.pushButton_construct_arrangement.setObjectName("pushButton_construct_arrangement")
        self.textEdit_arrangement_num_faces = QtGui.QTextEdit(self.groupBox_arrangement)
        self.textEdit_arrangement_num_faces.setGeometry(QtCore.QRect(130, 70, 41, 31))
        self.textEdit_arrangement_num_faces.setReadOnly(True)
        self.textEdit_arrangement_num_faces.setObjectName("textEdit_arrangement_num_faces")
        self.label_13 = QtGui.QLabel(self.groupBox_arrangement)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtGui.QLabel(self.groupBox_arrangement)
        self.label_14.setGeometry(QtCore.QRect(10, 160, 121, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtGui.QLabel(self.groupBox_arrangement)
        self.label_15.setGeometry(QtCore.QRect(10, 200, 121, 16))
        self.label_15.setObjectName("label_15")
        self.textEdit_arrangement_num_nodes = QtGui.QTextEdit(self.groupBox_arrangement)
        self.textEdit_arrangement_num_nodes.setGeometry(QtCore.QRect(130, 110, 41, 31))
        self.textEdit_arrangement_num_nodes.setReadOnly(True)
        self.textEdit_arrangement_num_nodes.setObjectName("textEdit_arrangement_num_nodes")
        self.textEdit_arrangement_num_edges = QtGui.QTextEdit(self.groupBox_arrangement)
        self.textEdit_arrangement_num_edges.setGeometry(QtCore.QRect(130, 150, 41, 31))
        self.textEdit_arrangement_num_edges.setReadOnly(True)
        self.textEdit_arrangement_num_edges.setObjectName("textEdit_arrangement_num_edges")
        self.textEdit_arrangement_num_subgraphs = QtGui.QTextEdit(self.groupBox_arrangement)
        self.textEdit_arrangement_num_subgraphs.setGeometry(QtCore.QRect(130, 190, 41, 31))
        self.textEdit_arrangement_num_subgraphs.setReadOnly(True)
        self.textEdit_arrangement_num_subgraphs.setObjectName("textEdit_arrangement_num_subgraphs")
        self.label_16 = QtGui.QLabel(self.groupBox_arrangement)
        self.label_16.setGeometry(QtCore.QRect(10, 120, 121, 16))
        self.label_16.setObjectName("label_16")
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(10, 660, 181, 16))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_11 = QtGui.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(10, 840, 191, 16))
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_10 = QtGui.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(200, 10, 20, 971))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.groupBox_dual_graphs = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_dual_graphs.setGeometry(QtCore.QRect(20, 680, 171, 141))
        self.groupBox_dual_graphs.setObjectName("groupBox_dual_graphs")
        self.pushButton_construct_dual_graphs = QtGui.QPushButton(self.groupBox_dual_graphs)
        self.pushButton_construct_dual_graphs.setGeometry(QtCore.QRect(10, 30, 161, 27))
        self.pushButton_construct_dual_graphs.setObjectName("pushButton_construct_dual_graphs")
        self.pushButton_plot_adjecency_graph = QtGui.QPushButton(self.groupBox_dual_graphs)
        self.pushButton_plot_adjecency_graph.setEnabled(False)
        self.pushButton_plot_adjecency_graph.setGeometry(QtCore.QRect(10, 80, 161, 27))
        self.pushButton_plot_adjecency_graph.setObjectName("pushButton_plot_adjecency_graph")
        self.pushButton_plot_connectivity_graph = QtGui.QPushButton(self.groupBox_dual_graphs)
        self.pushButton_plot_connectivity_graph.setEnabled(False)
        self.pushButton_plot_connectivity_graph.setGeometry(QtCore.QRect(10, 110, 161, 27))
        self.pushButton_plot_connectivity_graph.setObjectName("pushButton_plot_connectivity_graph")
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 350, 191, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_load_map = QtGui.QPushButton(self.centralwidget)
        self.pushButton_load_map.setGeometry(QtCore.QRect(10, 10, 191, 27))
        self.pushButton_load_map.setObjectName("pushButton_load_map")
        self.pushButton_load_traits = QtGui.QPushButton(self.centralwidget)
        self.pushButton_load_traits.setGeometry(QtCore.QRect(10, 40, 191, 27))
        self.pushButton_load_traits.setObjectName("pushButton_load_traits")
        self.checkBox_visualize_traits = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_visualize_traits.setEnabled(False)
        self.checkBox_visualize_traits.setGeometry(QtCore.QRect(220, 20, 101, 21))
        self.checkBox_visualize_traits.setChecked(False)
        self.checkBox_visualize_traits.setObjectName("checkBox_visualize_traits")
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 100, 191, 16))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.radioButton_load_traits_overwrite = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_load_traits_overwrite.setGeometry(QtCore.QRect(10, 70, 161, 21))
        self.radioButton_load_traits_overwrite.setChecked(True)
        self.radioButton_load_traits_overwrite.setObjectName("radioButton_load_traits_overwrite")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1548, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_face_manipulation.setTitle(QtGui.QApplication.translate("MainWindow", "Face manipulation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_merge_selected_faces.setText(QtGui.QApplication.translate("MainWindow", "merge selected faces", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reset_face_selection.setText(QtGui.QApplication.translate("MainWindow", "reset face selection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "semantic label:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_assign_label_to_selected_faces.setText(QtGui.QApplication.translate("MainWindow", "assign label to selected faces", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "select faces with l-click", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_store.setTitle(QtGui.QApplication.translate("MainWindow", "store", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save_arrangement_to_IEEE.setText(QtGui.QApplication.translate("MainWindow", "save to IEEE standard", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save_arrangement_to_pickle.setText(QtGui.QApplication.translate("MainWindow", "save to python pickle", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_arrangement.setTitle(QtGui.QApplication.translate("MainWindow", "arrangment", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_construct_arrangement.setText(QtGui.QApplication.translate("MainWindow", "construct arrangement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "number of faces", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "number of edges", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "number of sub-graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "number of nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_dual_graphs.setTitle(QtGui.QApplication.translate("MainWindow", "dual graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_construct_dual_graphs.setText(QtGui.QApplication.translate("MainWindow", "construct dual graphs", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_plot_adjecency_graph.setText(QtGui.QApplication.translate("MainWindow", "plot adjacency", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_plot_connectivity_graph.setText(QtGui.QApplication.translate("MainWindow", "plot connectivity", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_load_map.setText(QtGui.QApplication.translate("MainWindow", "Load Map", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_load_traits.setText(QtGui.QApplication.translate("MainWindow", "load traits from file (yaml/svg)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_visualize_traits.setText(QtGui.QApplication.translate("MainWindow", "visualize traits", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_load_traits_overwrite.setText(QtGui.QApplication.translate("MainWindow", "overwrite trait list", None, QtGui.QApplication.UnicodeUTF8))

