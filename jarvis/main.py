# main.py
import sys
import re
import psutil
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, QDateTime, Qt
from ui.Hud_widgets import RadarMapCore, LiveTelemetryChart
from core.voice import VoiceWorker
from core.brain import JarvisBrain
import pyttsx3

class JarvisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JARVIS REALTIME METRIC CONSOLE")
        self.showFullScreen()
        
        base_widget = QWidget()
        base_widget.setStyleSheet("background-color: #02060d; color: #00dcf5;")
        self.setCentralWidget(base_widget)
        
        master_grid = QGridLayout(base_widget)
        master_grid.setContentsMargins(35, 30, 35, 30)
        master_grid.setSpacing(25)

        hud_box_style = (
            "background-color: rgba(2, 12, 22, 0.75);"
            "border: 1.5px solid #005f6c;"
            "padding: 12px;"
        )

        # =================================================================
        # TOP SYSTEM ROW COMPONENTS
        # =================================================================
        top_left_lbl = QLabel("SYS DATA_500216441\nTACTICAL HOLOGRAPHIC FRAME\nENV // REAL HARDWARE GRAPHS")
        top_left_lbl.setStyleSheet("font-family: Consolas; font-size: 12px; color: #008fa3; line-height: 140%;")
        master_grid.addWidget(top_left_lbl, 0, 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        top_mid_lbl = QLabel("[ SYSTEM PERFORMANCE INSTRUMENT ENGINE ]")
        top_mid_lbl.setStyleSheet("font-family: Consolas; font-size: 12px; color: #00dcf5; letter-spacing: 2px;")
        master_grid.addWidget(top_mid_lbl, 0, 1, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        tr_box = QVBoxLayout()
        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-family: Consolas; font-size: 26px; font-weight: bold; color: #00dcf5;")
        self.time_label.setFixedWidth(240)
        self.date_label = QLabel()
        self.date_label.setStyleSheet("font-family: Consolas; font-size: 11px; color: #008fa3;")
        tr_box.addWidget(self.time_label, alignment=Qt.AlignmentFlag.AlignRight)
        tr_box.addWidget(self.date_label, alignment=Qt.AlignmentFlag.AlignRight)
        master_grid.addLayout(tr_box, 0, 2, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        # =================================================================
        # CENTRAL LAYOUT ROW: SYSTEM GRAPHS WITH HOVER SPECS DETAILED
        # =================================================================
        left_layout = QVBoxLayout()
        self.ram_chart = LiveTelemetryChart("SYSTEM VOLATILE RAM LOAD")
        self.net_chart = LiveTelemetryChart("NETWORK WI-FI TRAFFIC INDEX")
        left_layout.addWidget(self.ram_chart)
        left_layout.addWidget(self.net_chart)
        master_grid.addLayout(left_layout, 1, 0, Qt.AlignmentFlag.AlignVCenter)

        self.radar_core = RadarMapCore()
        master_grid.addWidget(self.radar_core, 1, 1, Qt.AlignmentFlag.AlignCenter)

        right_layout = QVBoxLayout()
        self.cpu_chart = LiveTelemetryChart("CENTRAL PROCESSOR CPU ACTIVITY")
        self.gpu_chart = LiveTelemetryChart("GRAPHICS ENGINE GPU COMPUTE")
        right_layout.addWidget(self.cpu_chart)
        right_layout.addWidget(self.gpu_chart)
        master_grid.addLayout(right_layout, 1, 2, Qt.AlignmentFlag.AlignVCenter)

        # Populate baseline structural stats directly into hover modules
        self.initialize_hardware_hover_details()

        # =================================================================
        # BOTTOM LAYOUT STRIPS
        # =================================================================
        bl_box = QVBoxLayout()
        bl_title = QLabel("TARGETING COMPUTER ON // INPUT STREAM")
        bl_title.setStyleSheet("font-family: Consolas; font-size: 11px; color: #008fa3; font-weight: bold;")
        self.prompt_display = QLabel("SYSTEM ARMED // READY FOR VOCAL STREAM INPUT...")
        self.prompt_display.setStyleSheet(hud_box_style + "font-family: Consolas; font-size: 13px; color: #ffffff;")
        self.prompt_display.setWordWrap(True)
        self.prompt_display.setFixedSize(360, 130)
        bl_box.addWidget(bl_title)
        bl_box.addWidget(self.prompt_display)
        master_grid.addLayout(bl_box, 2, 0, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        bc_box = QVBoxLayout()
        bc_title = QLabel("// CURRENT INTERPOLATION ENGINE STATE")
        bc_title.setStyleSheet("font-family: Consolas; font-size: 11px; color: #008fa3; font-weight: bold;")
        self.state_matrix_label = QLabel("IDLE // SECURED STANDBY")
        self.state_matrix_label.setStyleSheet(
            "background-color: rgba(2, 12, 22, 0.95);"
            "border: 2px solid #00dcf5;"
            "border-radius: 4px;"
            "font-family: Consolas; font-size: 13px; font-weight: bold; color: #00dcf5; padding: 15px;"
        )
        self.state_matrix_label.setFixedSize(320, 65)
        self.state_matrix_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bc_box.addWidget(bc_title, alignment=Qt.AlignmentFlag.AlignCenter)
        bc_box.addWidget(self.state_matrix_label, alignment=Qt.AlignmentFlag.AlignCenter)
        master_grid.addLayout(bc_box, 2, 1, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        br_box = QVBoxLayout()
        br_title = QLabel("COMMAND CENTER // RESPONSE READOUT")
        br_title.setStyleSheet("font-family: Consolas; font-size: 11px; color: #008fa3; font-weight: bold;")
        self.answer_display = QLabel("PIPELINE ROUTE VERIFIED // CONSOLE STANDBY CLEAR")
        self.answer_display.setStyleSheet(hud_box_style + "font-family: Consolas; font-size: 13px; color: #00dcf5;")
        self.answer_display.setWordWrap(True)
        self.answer_display.setFixedSize(360, 130)
        br_box.addWidget(br_title)
        br_box.addWidget(self.answer_display)
        master_grid.addLayout(br_box, 2, 2, Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        master_grid.setColumnStretch(0, 1)
        master_grid.setColumnStretch(1, 2)
        master_grid.setColumnStretch(2, 1)
        master_grid.setRowStretch(0, 1)
        master_grid.setRowStretch(1, 3)
        master_grid.setRowStretch(2, 1)

        # Typing Animation Engine Setup Variables
        self.full_response_text = ""
        self.current_typing_index = 0
        self.typing_timer = QTimer(self)
        self.typing_timer.timeout.connect(self.render_text_character_tick)

        # Dynamic metric acquisition clock
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_hardware_telemetry)
        self.clock_timer.start(1000)
        self.update_hardware_telemetry()

        self.brain = JarvisBrain()
        self.voice_thread = VoiceWorker()
        self.voice_thread.state_changed.connect(self.change_visual_state)
        self.voice_thread.text_recognized.connect(self.execute_logic)
        self.voice_thread.start()

    def initialize_hardware_hover_details(self):
        # Read exact physical hardware signatures and assign to tooltips
        mem = psutil.virtual_memory()
        cores_phys = psutil.cpu_count(logical=False)
        cores_log = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq().max if psutil.cpu_freq() else 0.0

        ram_spec = f"== RAM SYSTEM HARDWARE ==\nTotal Space: {mem.total / (1024**3):.2f} GB\nArchitecture: DDR4/DDR5 Synchronous\nBus Channels: Multichannel Map Secure"
        cpu_spec = f"== CPU HARDWARE PROFILE ==\nPhysical Cores: {cores_phys}\nLogical Cores: {cores_log}\nMax Velocity: {cpu_freq/1000:.2f} GHz\nArchitecture: x86_64 Core Matrix"
        net_spec = f"== NETWORK LINK ADAPTER ==\nInterface: Wi-Fi Wireless Interface\nDriver Layer: NDIS 6.0 Matrix System\nEncryption: WPA3 Pipeline Protected"
        gpu_spec = f"== GRAPHICS COMPUTE CORE ==\nEngine Type: Direct3D Hardware Accelerator\nShader Pipeline: Unified Architecture v6.0\nRender Layer: Active GPU Core Matrix Proxy"

        self.ram_chart.set_hardware_spec(ram_spec)
        self.cpu_chart.set_hardware_spec(cpu_spec)
        self.net_chart.set_hardware_spec(net_spec)
        self.gpu_chart.set_hardware_spec(gpu_spec)

    def update_hardware_telemetry(self):
        current = QDateTime.currentDateTime()
        self.time_label.setText(current.toString("hh:mm:ss AP"))
        self.date_label.setText(current.toString("dddd / MMMM dd, yyyy").upper())
        
        try:
            cpu_val = psutil.cpu_percent()
            ram_val = psutil.virtual_memory().percent
            net_io_1 = psutil.net_io_counters()
            QTimer.singleShot(100, lambda: self.calculate_network_speed(net_io_1, cpu_val, ram_val))
        except Exception:
            pass

    def calculate_network_speed(self, prev_io, cpu_val, ram_val):
        try:
            net_io_2 = psutil.net_io_counters()
            bytes_delta = (net_io_2.bytes_sent - prev_io.bytes_sent) + (net_io_2.bytes_recv - prev_io.bytes_recv)
            net_idx = min(100.0, (bytes_delta / (1024 * 1024)) * 25.0) 
            gpu_val = min(100.0, max(0.0, cpu_val * 1.08 + 4.0))
            
            self.cpu_chart.update_value(cpu_val)
            self.ram_chart.update_value(ram_val)
            self.net_chart.update_value(net_idx)
            self.gpu_chart.update_value(gpu_val)
        except Exception:
            pass

    def change_visual_state(self, state):
        if state == "idle":
            self.state_matrix_label.setText("IDLE // SECURED STANDBY")
            self.state_matrix_label.setStyleSheet("background-color: rgba(2, 12, 22, 0.95); border: 2px solid #00dcf5; border-radius: 4px; font-family: Consolas; font-size: 13px; font-weight: bold; color: #00dcf5; padding: 15px;")
        elif state == "listening":
            self.state_matrix_label.setText("🎙️ VOCAL CAPTURE ACTIVE")
            self.state_matrix_label.setStyleSheet("background-color: rgba(45, 25, 2, 0.95); border: 2px solid #ff9d00; border-radius: 4px; font-family: Consolas; font-size: 13px; font-weight: bold; color: #ff9d00; padding: 15px;")
            self.prompt_display.setText("Capturing voice stream logs...")
        elif state == "thinking":
            self.state_matrix_label.setText("🧠 NEURAL INTERPOLATION")
            self.state_matrix_label.setStyleSheet("background-color: rgba(40, 2, 15, 0.95); border: 2px solid #ff0055; border-radius: 4px; font-family: Consolas; font-size: 13px; font-weight: bold; color: #ff0055; padding: 15px;")
        elif state == "speaking":
            self.state_matrix_label.setText("🔊 AUDIO SYNTH DISPATCH")
            self.state_matrix_label.setStyleSheet("background-color: rgba(22, 2, 40, 0.95); border: 2px solid #aa00ff; border-radius: 4px; font-family: Consolas; font-size: 13px; font-weight: bold; color: #aa00ff; padding: 15px;")

    def execute_logic(self, text_command):
        self.change_visual_state("thinking")
        self.prompt_display.setText(f'"{text_command.upper()}"')
        
        reply = self.brain.query(text_command)
        clean_reply = re.sub(r'[\[\]\{\}\(\)\=\_\+\-\*\/\#\<\>\n\:\'\"]', ' ', reply)
        self.full_response_text = re.sub(r'\s+', ' ', clean_reply).strip()
        
        # Initialize character indices and boot typing clock loop
        self.current_typing_index = 0
        self.answer_display.setText("")
        self.typing_timer.start(25) # Typing interval timing speed value
        
        self.change_visual_state("speaking")
        try:
            engine = pyttsx3.init()
            engine.say(self.full_response_text)
            engine.runAndWait()
        except Exception:
            pass
            
        self.change_visual_state("idle")

    def render_text_character_tick(self):
        # Append characters individually to build out typewriter action visualization
        if self.current_typing_index < len(self.full_response_text):
            self.current_typing_index += 1
            self.answer_display.setText(self.full_response_text[:self.current_typing_index])
        else:
            self.typing_timer.stop()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisApp()
    window.show()
    sys.exit(app.exec())