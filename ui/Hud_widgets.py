# ui/Hud_widgets.py
import math
from PyQt6.QtWidgets import QWidget, QToolTip
from PyQt6.QtCore import QTimer, Qt, QPointF
from PyQt6.QtGui import QPainter, QPen, QColor, QBrush, QConicalGradient

class RadarMapCore(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(540, 400)
        self.radar_angle = 0.0
        self.color = QColor(0, 220, 245) 
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_sweep)
        self.timer.start(20)

    def update_sweep(self):
        self.radar_angle -= 1.8  
        if self.radar_angle < -360:
            self.radar_angle = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        w, h = self.width(), self.height()
        cx, cy = w / 2.0, h / 2.0
        center = QPointF(cx, cy)
        
        painter.setPen(QPen(QColor(self.color.red(), self.color.green(), self.color.blue(), 20), 2))
        map_scale_x, map_scale_y = w / 800.0, h / 500.0
        land_blocks = [
            (120, 140, 130, 160), (260, 190, 110, 200),
            (430, 130, 190, 150), (460, 250, 90, 130), (660, 310, 95, 75)
        ]
        for bx, by, bw, bh in land_blocks:
            lx, ly = int(bx * map_scale_x), int(by * map_scale_y)
            lw, lh = int(bw * map_scale_x), int(bh * map_scale_y)
            for x in range(lx, lx + lw, 15):
                for y in range(ly, ly + lh, 15):
                    painter.drawPoint(x, y)

        ring_pen = QPen(QColor(self.color.red(), self.color.green(), self.color.blue(), 45), 1)
        painter.setPen(ring_pen)
        radar_radius = min(w, h) * 0.44
        painter.drawEllipse(center, radar_radius, radar_radius)
        painter.drawEllipse(center, radar_radius * 0.70, radar_radius * 0.70)
        painter.drawEllipse(center, radar_radius * 0.40, radar_radius * 0.40)
        
        painter.drawLine(int(cx - radar_radius), int(cy), int(cx + radar_radius), int(cy))
        painter.drawLine(int(cx), int(cy - radar_radius), int(cx), int(cy + radar_radius))

        cone_grad = QConicalGradient(center, self.radar_angle)
        cone_grad.setColorAt(0.0, QColor(self.color.red(), self.color.green(), self.color.blue(), 90))
        cone_grad.setColorAt(0.12, QColor(self.color.red(), self.color.green(), self.color.blue(), 25))
        cone_grad.setColorAt(0.35, QColor(self.color.red(), self.color.green(), self.color.blue(), 5))
        cone_grad.setColorAt(1.0, QColor(0, 0, 0, 0))
        
        painter.setBrush(QBrush(cone_grad))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(center, radar_radius, radar_radius)


class LiveTelemetryChart(QWidget):
    def __init__(self, title="METRIC INDEX", parent=None):
        super().__init__(parent)
        self.setMinimumSize(260, 145)
        self.title = title
        self.history = [0.0] * 30  
        self.cyan = QColor(0, 220, 245)
        self.dark_line = QColor(0, 95, 108, 100)
        self.spec_details = "Awaiting system handshake..."
        
        # Enable active mouse monitoring tracking architecture inside widget
        self.setMouseTracking(True)
        
        # Apply dark tactical blueprint styling profile directly to widget tooltip framework
        QToolTip.setFont(painter_font := self.font())
        self.setStyleSheet("""
            QToolTip {
                background-color: #011626;
                color: #00dcf5;
                border: 2px solid #005f6c;
                font-family: 'Consolas';
                font-size: 11px;
                padding: 6px;
            }
        """)

    def set_hardware_spec(self, text):
        self.spec_details = text

    def enterEvent(self, event):
        # Trigger hover action matrix tooltip display on bounds entry
        QToolTip.showText(self.mapToGlobal(QPointF(10, 10).toPoint()), self.spec_details, self)
        super().enterEvent(event)

    def mouseMoveEvent(self, event):
        # Maintain tracking coordinates as cursor moves across chart
        QToolTip.showText(self.mapToGlobal(event.position().toPoint()), self.spec_details, self)
        super().mouseMoveEvent(event)

    def update_value(self, new_val):
        self.history.pop(0)
        self.history.append(float(new_val))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        w, h = self.width(), self.height()
        
        painter.setPen(QPen(self.dark_line, 1.5))
        painter.setBrush(QBrush(QColor(2, 12, 22, 180)))
        painter.drawRect(0, 0, w - 1, h - 1)
        
        painter.setPen(QPen(QColor(self.cyan.red(), self.cyan.green(), self.cyan.blue(), 15), 1))
        for x in range(0, w, 20):
            painter.drawLine(x, 0, x, h)
        for y in range(0, h, 20):
            painter.drawLine(0, y, w, y)
            
        painter.setPen(QPen(self.cyan, 1))
        painter.drawText(10, 22, f"// {self.title}: {self.history[-1]:.1f}%")
        
        painter.setPen(QPen(self.cyan, 2))
        points_count = len(self.history)
        x_step = w / (points_count - 1)
        
        for i in range(points_count - 1):
            y1 = h - 15 - ((self.history[i] / 100.0) * (h - 40))
            y2 = h - 15 - ((self.history[i+1] / 100.0) * (h - 40))
            x1 = i * x_step
            x2 = (i + 1) * x_step
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))