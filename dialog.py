# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QFileDialog
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PySide6.QtWidgets import (QHBoxLayout,  QPushButton, QVBoxLayout)
from PySide6.QtCore import (Qt, Slot, QDir, QRectF)
from PySide6.QtCharts import QChart, QValueAxis, QLineSeries,QChartView
from PySide6.QtGui import QPixmap, QColor

from DiyPixmapItem import DiyPixmapItem

import pdb
import numpy as np

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Dialog

_ORI_IMG_VIEW_NAME = "ori_img"
_FITTED_CHART_VIEW_NAME = "fitted_chart"
_AXIS_X_MAX = "x_max"
_AXIS_X_MIN = "x_min"
_AXIS_Y_MAX = "y_max"
_AXIS_Y_MIN = "y_min"
_X_STR = "X"
_Y_STR = "Y"
_DATA_V = "data_v"
_BTN_STR = "btn"
_EDIT_STR = "edit"
_CMT_STR = "comment"
_CTRL_STR = "ctrl"
_IDX_0_STR = "idx_0"
_IDX_1_STR = "idx_1"
_MIN_POINTS_NUM = 2
_CIRCLE_MARK_R = 5

def calculate_on_poly(cofts, x):
    k = len(cofts) - 1
    x_pws = [pow(x, i) for i in range(k+1)]
    result = np.sum(np.multiply(x_pws, cofts))
    return result

class Dialog(QDialog):
    """
    Four states:
        1: empty,
        2: contains only original image,
        3: contains both img and fitted chart,
        4: contains only curve form imported data.
    """
    _DISPLAY_STATE_EMPTY = 1
    _DISPLAY_STATE_ORI_IMG = 2
    _DISPLAY_STATE_IMG_AND_CHART = 3
    _DISPLAY_STATE_IMPORTED_CHART = 4

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.display_state = Dialog._DISPLAY_STATE_EMPTY

        self.img_scene = None
        self.ui.img_view = None
        self.ui.img_btn_layout = None
        self.ui.img_op_layout = None
        self.ui.begin_add_point_btn = None
        self.ui.remove_all_point_btn = None
        self.ui.zoom_out_btn = None
        self.ui.zoom_in_btn = None
        self.ui.zoom_restore_btn = None
        self.zoom_step = 0.1
        self.zoom_min_scale = 0.1
        self.zoom_max_scale = 2.0
        self.cur_zoom_scale = 1

        self.ori_cursor = self.cursor()
        self.cofts = []

        self.chart = None
        self.ui.chart_view = None

        self.ui.figure_layout = QHBoxLayout() #contains img layouts and chart view.
        self.ui.topLevelLayout.addLayout(self.ui.figure_layout)

        self.axis_set_flag = {_AXIS_X_MIN: False, _AXIS_X_MAX: False,
                              _AXIS_Y_MIN: False, _AXIS_Y_MAX: False, }
        self.axis_datum = {
            _AXIS_X_MIN : {_X_STR: 0, _Y_STR: 0, _DATA_V: 0,
                           _BTN_STR: self.ui.xAxisMinBtn,
                           _EDIT_STR: {_X_STR: self.ui.xAxisMinImgPxX,
                                       _Y_STR: self.ui.xAxisMinImgPxY,
                                       _DATA_V: self.ui.xAxisMinDataValue},
                          },
            _AXIS_X_MAX : {_X_STR: 0, _Y_STR: 0, _DATA_V: 0,
                           _BTN_STR: self.ui.xAxisMaxBtn,
                           _EDIT_STR: {_X_STR: self.ui.xAxisMaxImgPxX,
                                       _Y_STR: self.ui.xAxisMaxImgPxY,
                                       _DATA_V: self.ui.xAxisMaxDataValue},
                          },
            _AXIS_Y_MIN : {_X_STR: 0, _Y_STR: 0, _DATA_V: 0,
                           _BTN_STR: self.ui.yAxisMinBtn,
                           _EDIT_STR: {_X_STR: self.ui.yAxisMinImgPxX,
                                       _Y_STR: self.ui.yAxisMinImgPxY,
                                       _DATA_V: self.ui.yAxisMinDataValue},
                           },
            _AXIS_Y_MAX : {_X_STR: 0, _Y_STR: 0, _DATA_V: 0,
                           _BTN_STR: self.ui.yAxisMaxBtn,
                           _EDIT_STR: {_X_STR: self.ui.yAxisMaxImgPxX,
                                       _Y_STR: self.ui.yAxisMaxImgPxY,
                                       _DATA_V: self.ui.yAxisMaxDataValue},
                           },
        }

        """
        _X_STR: 0, _Y_STR: 0,
        _DATA_V: { _X_STR: 0, _Y_STR: 0}
        """
        self.selected_points = []
        self.selecting = False
        self.s_p_marks = []

        self.axis_editor_ctrls = [
            {_CTRL_STR: self.ui.yAxisMaxImgPxX,
             _CMT_STR: self.ui.yAxisMaxBtn.text() + "," + self.ui.yAxisMaxImgPxX_Lbl.text(),
             _IDX_0_STR: _AXIS_Y_MAX, _IDX_1_STR: _X_STR},
            {_CTRL_STR: self.ui.yAxisMaxImgPxY,
             _CMT_STR: self.ui.yAxisMaxBtn.text() + "," + self.ui.yAxisMaxImgPxY_Lbl.text(),
             _IDX_0_STR: _AXIS_Y_MAX, _IDX_1_STR: _Y_STR},
            {_CTRL_STR: self.ui.yAxisMaxDataValue,
             _CMT_STR: self.ui.yAxisMaxBtn.text() + "," + self.ui.yAxisMaxDataValue_Lbl.text(),
             _IDX_0_STR: _AXIS_Y_MAX, _IDX_1_STR: _DATA_V},

            {_CTRL_STR: self.ui.yAxisMinImgPxX,
             _CMT_STR: self.ui.yAxisMinBtn.text() + "," + self.ui.yAxisMinImgPxX_Lbl.text(),
             _IDX_0_STR: _AXIS_Y_MIN, _IDX_1_STR: _X_STR},
            {_CTRL_STR: self.ui.yAxisMinImgPxY,
             _CMT_STR: self.ui.yAxisMinBtn.text() + "," + self.ui.yAxisMinImgPxY_Lbl.text(),
             _IDX_0_STR: _AXIS_Y_MIN, _IDX_1_STR: _Y_STR},
            {_CTRL_STR: self.ui.yAxisMinDataValue,
             _CMT_STR: self.ui.yAxisMinBtn.text() + "," + self.ui.yAxisMinDataValue_Lbl.text(),
             _IDX_0_STR: _AXIS_Y_MIN, _IDX_1_STR: _DATA_V},

            {_CTRL_STR: self.ui.xAxisMaxImgPxX,
             _CMT_STR: self.ui.xAxisMaxBtn.text() + "," + self.ui.xAxisMaxImgPxX_Lbl.text(),
             _IDX_0_STR: _AXIS_X_MAX, _IDX_1_STR: _X_STR},
            {_CTRL_STR: self.ui.xAxisMaxImgPxY,
             _CMT_STR: self.ui.xAxisMaxBtn.text() + "," + self.ui.xAxisMaxImgPxY_Lbl.text(),
             _IDX_0_STR: _AXIS_X_MAX, _IDX_1_STR: _Y_STR},
            {_CTRL_STR: self.ui.xAxisMaxDataValue,
             _CMT_STR: self.ui.xAxisMaxBtn.text() + "," + self.ui.xAxisMaxDataValue_Lbl.text(),
             _IDX_0_STR: _AXIS_X_MAX, _IDX_1_STR: _DATA_V},

            {_CTRL_STR: self.ui.xAxisMinImgPxX,
             _CMT_STR: self.ui.xAxisMinBtn.text() + "," + self.ui.xAxisMinImgPxX_Lbl.text(),
             _IDX_0_STR: _AXIS_X_MIN, _IDX_1_STR: _X_STR},
            {_CTRL_STR: self.ui.xAxisMinImgPxY,
             _CMT_STR: self.ui.xAxisMinBtn.text() + "," + self.ui.xAxisMinImgPxY_Lbl.text(),
             _IDX_0_STR: _AXIS_X_MIN, _IDX_1_STR: _Y_STR},
            {_CTRL_STR: self.ui.xAxisMinDataValue,
             _CMT_STR: self.ui.xAxisMinBtn.text() + "," + self.ui.xAxisMinDataValue_Lbl.text(),
             _IDX_0_STR: _AXIS_X_MIN, _IDX_1_STR: _DATA_V},
        ]

    def clear_axis_set_flag(self):
        for k in self.axis_set_flag.keys():
            self.axis_set_flag[k] = False

    def check_axis_dataum(self):
        #note: y axis increase from top to botom
        if ((self.axis_datum[_AXIS_X_MAX][_X_STR] <= self.axis_datum[_AXIS_X_MIN][_X_STR])
              or (self.axis_datum[_AXIS_X_MAX][_DATA_V] <= self.axis_datum[_AXIS_X_MIN][_DATA_V])
              or (self.axis_datum[_AXIS_Y_MAX][_Y_STR] >= self.axis_datum[_AXIS_Y_MIN][_Y_STR])
              or (self.axis_datum[_AXIS_Y_MAX][_DATA_V] <= self.axis_datum[_AXIS_Y_MIN][_DATA_V])):
            return False
        else:
            return True

    def set_axis_editor_ctrls_enabled(self, e):
        for ctrl in self.axis_editor_ctrls:
            ctrl[_CTRL_STR].setEnabled(e)

    @Slot()
    def select_img_btn_clicked(self):
        ori_img_fpn = QFileDialog.getOpenFileName(self, "请选择图片文件",
                                                    QDir.currentPath(),
                                                    "img (*.bmp *.jpg *.png *.tif)")[0]
        if("" == ori_img_fpn):
            return
        pixmap = QPixmap(ori_img_fpn)
        pm_item = DiyPixmapItem(self, pixmap)
        self.img_scene = QGraphicsScene()
        self.img_scene.addItem(pm_item)
        view = QGraphicsView(self.img_scene, self)
        self.add_views_to_figure_layout((_ORI_IMG_VIEW_NAME, view))
        self.ui.img_view = view
        self.cur_zoom_scale = 1
        self.ui.img_view.show()
        self.display_state = Dialog._DISPLAY_STATE_ORI_IMG

    def s_p_mark_on_img(self, x, y):
        if self.img_scene != None:
            mark = QGraphicsEllipseItem(x - _CIRCLE_MARK_R, y - _CIRCLE_MARK_R,
                                        _CIRCLE_MARK_R * 2, _CIRCLE_MARK_R * 2)
            mark.setPen(QColor(255, 0, 0))
            mark.setBrush(QColor(255, 0, 0))
            self.img_scene.addItem(mark)
            self.s_p_marks.append(mark)

    def remove_mark_on_img(self, x, y):
        check_w = _CIRCLE_MARK_R * 2
        rect = QRectF(x - check_w, y - check_w, check_w * 2, check_w * 2)
        covered_m = self.img_scene.items(rect, Qt.ContainsItemShape)
        m_cnt = len(covered_m)
        if m_cnt > 0:
            for j in range(len(covered_m)):
                for i in range(len(self.s_p_marks) - 1, -1, -1):
                    if self.s_p_marks[i] is covered_m[j]:
                        self.s_p_marks.pop(i)
                        self.selected_points.pop(i)
                        self.img_scene.removeItem(covered_m[j])
                        break

    def clear_marks_on_img(self):
        for i in self.s_p_marks:
            self.img_scene.removeItem(i)
        self.s_p_marks.clear()
        self.ui.selectedPtsNumDispLbl.setText("")

    @Slot(float, float, int)
    def mouse_click_on_img(self, x, y, btns):
        for k in self.axis_set_flag.keys():
            if self.axis_set_flag[k]:
                self.axis_datum[k][_X_STR] = x
                self.axis_datum[k][_Y_STR] = y

                self.axis_datum[k][_BTN_STR].setEnabled(True)
                self.axis_datum[k][_EDIT_STR][_X_STR].setText(str("{:.2f}".format(x)))
                self.axis_datum[k][_EDIT_STR][_Y_STR].setText(str("{:.2f}".format(y)))

                d_str = self.axis_datum[k][_EDIT_STR][_DATA_V].text()
                if len(d_str) == 0:
                    self.axis_datum[k][_DATA_V] = 0
                    self.axis_datum[k][_EDIT_STR][_DATA_V].setText("0")

                self.axis_set_flag[k] = False
                self.setCursor(self.ori_cursor)
                #break
        #pdb.set_trace()
        if self.selecting:
            if Qt.LeftButton == btns:
                point = dict()
                point[_X_STR] = x;  point[_Y_STR] = y
                point[_DATA_V] = dict()
                min_d = self.axis_datum[_AXIS_X_MIN]
                max_d = self.axis_datum[_AXIS_X_MAX]
                point[_DATA_V][_X_STR] = ((x - min_d[_X_STR])/(max_d[_X_STR] - min_d[_X_STR])) * (max_d[_DATA_V] - min_d[_DATA_V]) + min_d[_DATA_V]
                min_d = self.axis_datum[_AXIS_Y_MIN] #note: y axis increase from top to botom
                max_d = self.axis_datum[_AXIS_Y_MAX]
                point[_DATA_V][_Y_STR] = ((y - min_d[_Y_STR])/(max_d[_Y_STR] - min_d[_Y_STR])) * (max_d[_DATA_V] - min_d[_DATA_V]) + min_d[_DATA_V]
                self.selected_points.append(point)
                self.s_p_mark_on_img(x, y)
            else:
                self.remove_mark_on_img(x, y)
            p_n = len(self.selected_points)
            self.ui.selectedPtsNumDispLbl.setText(str(p_n))

    @Slot()
    def save_selected_points(self):
        p_f = open("./selected_points.txt", "w")
        """
        First, save axis datum;
        """
        for ctrl in self.axis_editor_ctrls:
            print(ctrl[_CMT_STR] + ":" + str(self.axis_datum[ctrl[_IDX_0_STR]][ctrl[_IDX_1_STR]]),
                  file = p_f)

        print("------------------", file = p_f)
        """
        Then, save selected points.
        """
        for p in self.selected_points:
            l = "{0},{1},{2},{3}".format(p[_X_STR], p[_Y_STR],
                                         p[_DATA_V][_X_STR], p[_DATA_V][_Y_STR])
            print(l, file = p_f)
        p_f.close()

    @Slot()
    def y_axis_max_btn_clicked(self):
        self.clear_axis_set_flag()
        self.axis_set_flag[_AXIS_Y_MAX] = True
        self.ui.yAxisMaxBtn.setEnabled(False)
        self.setCursor(Qt.CrossCursor)

    @Slot()
    def y_axis_min_btn_clicked(self):
        self.clear_axis_set_flag()
        self.axis_set_flag[_AXIS_Y_MIN] = True
        self.ui.yAxisMinBtn.setEnabled(False)
        self.setCursor(Qt.CrossCursor)

        if (len(self.axis_datum[_AXIS_X_MIN][_EDIT_STR][_X_STR].text()) == 0 and
             len(self.axis_datum[_AXIS_X_MIN][_EDIT_STR][_Y_STR].text()) == 0):
            self.axis_set_flag[_AXIS_X_MIN] = True

    @Slot()
    def x_axis_max_btn_clicked(self):
        self.clear_axis_set_flag()
        self.axis_set_flag[_AXIS_X_MAX] = True
        self.ui.xAxisMaxBtn.setEnabled(False)
        self.setCursor(Qt.CrossCursor)

    @Slot()
    def x_axis_min_btn_clicked(self):
        self.clear_axis_set_flag()
        self.axis_set_flag[_AXIS_X_MIN] = True
        self.ui.xAxisMinBtn.setEnabled(False)
        self.setCursor(Qt.CrossCursor)

        if (len(self.axis_datum[_AXIS_Y_MIN][_EDIT_STR][_X_STR].text()) == 0 and
             len(self.axis_datum[_AXIS_Y_MIN][_EDIT_STR][_Y_STR].text()) == 0):
            self.axis_set_flag[_AXIS_Y_MIN] = True

    @Slot()
    def clear_axis_datum(self):
        for ctrl in self.axis_editor_ctrls:
            ctrl[_CTRL_STR].setText("")
        for k in self.axis_datum:
            self.axis_datum[k][_X_STR] = self.axis_datum[k][_Y_STR] = 0
            self.axis_datum[k][_DATA_V] = 0

    @Slot()
    def select_points(self):
        if not(self.selecting):
            c = self.check_axis_dataum()
            if not c:
                QMessageBox.critical(None, "!!!", "请输入正确的坐标轴信息！")
                return
        self.selecting = not(self.selecting)
        if self.selecting:
            self.clear_axis_set_flag()
            self.set_axis_editor_ctrls_enabled(False)
            self.ui.begin_add_point_btn.setText("结束选点")
            self.setCursor(Qt.CrossCursor)
        else:
            self.set_axis_editor_ctrls_enabled(True)
            self.ui.begin_add_point_btn.setText("开始选点")
            self.setCursor(self.ori_cursor)

    @Slot()
    def delete_all_selected_points(self):
        self.clear_marks_on_img()
        self.selected_points.clear()

    @Slot()
    def zoom_out_btn_clicked(self):
        if self.ui.img_view != None:
            if self.cur_zoom_scale < self.zoom_max_scale:
                self.ui.img_view.resetTransform()
                self.cur_zoom_scale = self.cur_zoom_scale + self.zoom_step
                self.ui.img_view.scale(self.cur_zoom_scale, self.cur_zoom_scale)

    @Slot()
    def zoom_in_btn_clicked(self):
        if self.ui.img_view != None:
            if self.cur_zoom_scale > self.zoom_min_scale:
                self.ui.img_view.resetTransform()
                self.cur_zoom_scale = self.cur_zoom_scale - self.zoom_step
                self.ui.img_view.scale(self.cur_zoom_scale, self.cur_zoom_scale)

    @Slot()
    def zoom_restore_btn_clicked(self):
        if self.ui.img_view != None:
            self.cur_zoom_scale = 1
            self.ui.img_view.resetTransform()

    @Slot()
    def count_data_accord_fitting(self):
        if len(self.cofts) < _MIN_POINTS_NUM:
            QMessageBox.critical(None, "!!!", "选点数量过少，最少为{}个".format(_MIN_POINTS_NUM))
            return True
        x = self.ui.count_x_Edit.text()
        try:
            x = float(x)
        except ValueError:
            QMessageBox.critical(None, "!!!", "请输入数字")
            return True
        else:
            result = calculate_on_poly(self.cofts, x)
            self.ui.counted_y_Edit.setText(str(result))
            self.ui.counted_y_Edit.setCursorPosition(0)
            return True

    @Slot()
    def fitting_btn_clicked(self):
        err_msg = "请输入正整数格式的多项式次数，并小于选择的点数"
        k = self.ui.polyIdxEdit.text()
        try:
            k = int(k)
        except ValueError:
            QMessageBox.critical(None, "!!!", err_msg)
        else:
            n = len(self.selected_points)
            if k >= n:
                QMessageBox.critical(None, "!!!", err_msg)
                return
            self.cofts = self.gen_fitting_cofts(k)
            self.gen_fitted_curve_view()
            self.display_state = self._DISPLAY_STATE_IMG_AND_CHART

    def gen_fitted_curve_view(self):
        x_start = self.axis_datum[_AXIS_X_MIN][_DATA_V]
        x_end = self.axis_datum[_AXIS_X_MAX][_DATA_V]

        line_series = QLineSeries()
        x = x_start
        while x <= x_end:
            y = calculate_on_poly(self.cofts, x)
            line_series.append(x, y)
            x += 1

        x_axis = QValueAxis()
        x_axis.setRange(x_start, x_end * 1.1)
        x_axis.setTickCount(int(x_end - x_start + 1))
        y_axis = QValueAxis()
        y_axis.setRange(self.axis_datum[_AXIS_Y_MIN][_DATA_V],
                        self.axis_datum[_AXIS_Y_MAX][_DATA_V] * 1.05)
        chart = QChart()
        chart.addAxis(x_axis, Qt.AlignBottom)
        chart.addAxis(y_axis, Qt.AlignLeft)

        chart.addSeries(line_series)
        line_series.attachAxis(x_axis)
        line_series.attachAxis(y_axis)

        chart_view = QChartView(chart, self)
        self.add_views_to_figure_layout((_FITTED_CHART_VIEW_NAME, chart_view), replace = False)
        chart_view.show()
        self.ui.chart_view = chart_view
        self.chart = chart

    def gen_fitting_cofts(self, k):
        """
        Refer to the matrix:
        https://www.cnblogs.com/nhyq-wyj/p/14898517.html#:~:text=%20%E6%9C%80%E5%B0%8F%E4%BA%8C%E4%B9%98%E6%B3%95%E5%A4%9A%E9%A1%B9%E5%BC%8F%E6%9B%B2%E7%BA%BF%E6%8B%9F%E5%90%88%EF%BC%8C%E6%A0%B9%E6%8D%AE%E7%BB%99%E5%AE%9A%E7%9A%84m%E4%B8%AA%E7%82%B9%2C%E5%B9%B6%E4%B8%8D%E8%A6%81%E6%B1%82%E8%BF%99%E6%9D%A1%E6%9B%B2%E7%BA%BF%E7%B2%BE%E7%A1%AE%E5%9C%B0%E7%BB%8F%E8%BF%87%E8%BF%99%E4%BA%9B%E7%82%B9%EF%BC%8C%E8%80%8C%E6%98%AF%E6%9B%B2%E7%BA%BFy%3Df%28x%29%E7%9A%84%E8%BF%91%E4%BC%BC%E6%9B%B2%E7%BA%BFy%3D%20%CF%86%28x%29%E3%80%82,%E5%8E%9F%E7%90%86%20%E7%BB%99%E5%AE%9A%E6%95%B0%E6%8D%AE%E7%82%B9pi%28xi%2Cyi%29%EF%BC%8C%E5%85%B6%E4%B8%ADi%3D1%2C2%2C%E2%80%A6%2Cm%E3%80%82%E6%B1%82%E8%BF%91%E4%BC%BC%E6%9B%B2%E7%BA%BFy%3D%20%CF%86%28x%29%E3%80%82%E5%B9%B6%E4%B8%94%E4%BD%BF%E5%BE%97%E8%BF%91%E4%BC%BC%E6%9B%B2%E7%BA%BF%E4%B8%8Ey%3Df%28x%29%E7%9A%84%E5%81%8F%E5%B7%AE%E6%9C%80%E5%B0%8F%E3%80%82%E8%BF%91%E4%BC%BC%E6%9B%B2%E7%BA%BF%E5%9C%A8%E7%82%B9pi%E5%A4%84%E7%9A%84%E5%81%8F%E5%B7%AE%CE%B4i%3D%20%CF%86%28xi
        """
        n = len(self.selected_points)
        x_1d_arr = []
        x_1d_arr.append(n)

        x_one_idx_item = [self.selected_points[i][_DATA_V][_X_STR] for i in range(n)]
        y_one_idx_item = [self.selected_points[i][_DATA_V][_Y_STR] for i in range(n)]
        y_arr = []
        y_arr.append(np.sum(y_one_idx_item))
        p_xs = [1 for i in range(n)]
        for i in range(1, 2 * k + 1):
            p_xs = np.multiply(p_xs, x_one_idx_item)
            x_1d_arr.append(np.sum(p_xs))
            if i <= k:
                p_ys = np.multiply(p_xs, y_one_idx_item)
                y_arr.append(np.sum(p_ys))

        x_arr = []
        for i in range(k + 1):
            x_arr.append(x_1d_arr[i:i+k+1])

        cofts = np.linalg.solve(x_arr, y_arr)
        #pdb.set_trace()
        return cofts

    def add_views_to_figure_layout(self, *views, replace = False):
        """
        views is a list, each item is a tuple pair: (name, view). Currently, there
        are the following valid parameters:
            1) (_ORI_IMG_VIEW_NAME, ori_img_view)
            2) (_FITTED_CHART_VIEW_NAME, fitted_chart)
        """
        for v in views:
            graph_view = v[1]
            if _ORI_IMG_VIEW_NAME == v[0]:
                if self.display_state == Dialog._DISPLAY_STATE_EMPTY:
                    self.ui.img_op_layout = QVBoxLayout()

                    h_box_layout = QHBoxLayout()
                    self.ui.begin_add_point_btn = QPushButton()
                    self.ui.begin_add_point_btn.setText("开始选点")
                    self.ui.begin_add_point_btn.clicked.connect(self.select_points)
                    h_box_layout.addWidget(self.ui.begin_add_point_btn)

                    self.ui.remove_all_point_btn = QPushButton()
                    self.ui.remove_all_point_btn.setText("删除所有已选择的点")
                    self.ui.remove_all_point_btn.clicked.connect(self.delete_all_selected_points)
                    h_box_layout.addWidget(self.ui.remove_all_point_btn)

                    self.ui.zoom_out_btn = QPushButton()
                    self.ui.zoom_out_btn.setText("放大")
                    self.ui.zoom_out_btn.clicked.connect(self.zoom_out_btn_clicked)
                    h_box_layout.addWidget(self.ui.zoom_out_btn)

                    self.ui.zoom_in_btn = QPushButton()
                    self.ui.zoom_in_btn.setText("缩小")
                    self.ui.zoom_in_btn.clicked.connect(self.zoom_in_btn_clicked)
                    h_box_layout.addWidget(self.ui.zoom_in_btn)

                    self.ui.zoom_restore_btn = QPushButton()
                    self.ui.zoom_restore_btn.setText("恢复")
                    self.ui.zoom_restore_btn.clicked.connect(self.zoom_restore_btn_clicked)
                    h_box_layout.addWidget(self.ui.zoom_restore_btn)

                    self.ui.img_btn_layout = h_box_layout

                    self.ui.img_op_layout.addLayout(h_box_layout)

                    self.ui.img_op_layout.addWidget(graph_view)

                    self.ui.figure_layout.addLayout(self.ui.img_op_layout)
                elif self.display_state == Dialog._DISPLAY_STATE_ORI_IMG:
                    self.ui.img_op_layout.removeWidget(self.ui.img_view)
                    self.ui.img_op_layout.addWidget(graph_view)

            elif _FITTED_CHART_VIEW_NAME == v[0]:
                if replace:
                    self.ui.img_btn_layout.removeWidget(self.ui.begin_add_point_btn)
                    self.ui.img_btn_layout.removeWidget(self.ui.remove_all_point_btn)
                    self.ui.img_btn_layout.removeWidget(self.ui.zoom_out_btn)
                    self.ui.img_btn_layout.removeWidget(self.ui.zoom_in_btn)
                    self.ui.img_btn_layout.removeWidget(self.ui.zoom_restore_btn)
                    self.ui.img_op_layout.removeItem(self.ui.img_btn_layout)
                    self.ui.img_op_layout.removeWidget(self.ui.img_view)
                    self.ui.begin_add_point_btn.setVisible(False)
                    self.ui.remove_all_point_btn.setVisible(False)
                    self.ui.zoom_out_btn.setVisible(False)
                    self.ui.zoom_in_btn.setVisible(False)
                    self.ui.zoom_restore_btn.setVisible(False)
                    self.ui.img_view.setVisible(False)

                    self.ui.figure_layout.removeItem(self.ui.img_op_layout)
                self.ui.figure_layout.addWidget(graph_view)

#Begin editor slot###########################################
    @Slot()
    def x_axis_min_pxX_finished(self):
        try:
            v = float(self.ui.xAxisMinImgPxX.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_X_MIN][_X_STR] = v

    @Slot()
    def x_axis_min_pxY_finished(self):
        try:
            v = float(self.ui.xAxisMinImgPxY.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_X_MIN][_Y_STR] = v

    @Slot()
    def x_axis_min_dv_finished(self):
        try:
            v = float(self.ui.xAxisMinDataValue.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_X_MIN][_DATA_V] = v

    @Slot()
    def x_axis_max_pxX_finished(self):
        try:
            v = float(self.ui.xAxisMaxImgPxX.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_X_MAX][_X_STR] = v

    @Slot()
    def x_axis_max_pxY_finished(self):
        try:
            v = float(self.ui.xAxisMaxImgPxY.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_X_MAX][_Y_STR] = v

    @Slot()
    def x_axis_max_dv_finished(self):
        try:
            v = float(self.ui.xAxisMaxDataValue.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_X_MAX][_DATA_V] = v



    @Slot()
    def y_axis_min_pxX_finished(self):
        try:
            v = float(self.ui.yAxisMinImgPxX.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_Y_MIN][_X_STR] = v

    @Slot()
    def y_axis_min_pxY_finished(self):
        try:
            v = float(self.ui.yAxisMinImgPxY.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_Y_MIN][_Y_STR] = v

    @Slot()
    def y_axis_min_dv_finished(self):
        try:
            v = float(self.ui.yAxisMinDataValue.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_Y_MIN][_DATA_V] = v

    @Slot()
    def y_axis_max_pxX_finished(self):
        try:
            v = float(self.ui.yAxisMaxImgPxX.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_Y_MAX][_X_STR] = v

    @Slot()
    def y_axis_max_pxY_finished(self):
        try:
            v = float(self.ui.yAxisMaxImgPxY.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_Y_MAX][_Y_STR] = v

    @Slot()
    def y_axis_max_dv_finished(self):
        try:
            v = float(self.ui.yAxisMaxDataValue.text())
        except ValueError:
            QMessageBox.critical(None, "!!!", "输入必须为数字")
        else:
            self.axis_datum[_AXIS_Y_MAX][_DATA_V] = v
#End editor slot###########################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
