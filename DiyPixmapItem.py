# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QGraphicsPixmapItem)
from PySide6.QtCore import Signal, qDebug, QObject

class DiyPixmapItem(QObject, QGraphicsPixmapItem):
    mouse_click_sig = Signal(float, float, int)
    def constructor(self, event_widget):
        self.e_widget = event_widget
        self.mouse_click_sig.connect(self.e_widget.mouse_click_on_img)

    def __init__(self, event_widget, pixmap = None, parent = None):
        QObject.__init__(self)
        if None == pixmap:
            QGraphicsPixmapItem.__init__(self, parent)
        else:
            QGraphicsPixmapItem.__init__(self, pixmap, parent)
        self.constructor(event_widget)

    def mousePressEvent(self, event):
        self.mouse_click_sig.emit(event.pos().x(), event.pos().y(), event.buttons())
        qDebug("mouse press (item) x, y: " + str(event.pos().x()) + ", " + str(event.pos().y()))
        qDebug("mouse press (scene) x, y: " + str(event.scenePos().x()) + ", " + str(event.scenePos().y()))
        qDebug("mouse press (screen) x, y: " + str(event.screenPos().x()) + ", " + str(event.screenPos().y()))

