import sys
import cv2
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QSlider, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt


class AnnotationTool(QMainWindow):
    def __init__(self):
        super().__init__()

        # Video variables
        self.video_path = None
        self.cap = None
        self.current_frame = 0
        self.total_frames = 0
        self.annotations = []
        self.current_action = None

        # Downscale factor for the video frames (adjust this for performance)
        self.downscale_factor = 0.5

        # Pigeons for which we will create timeline bars
        self.pigeons = ['P_1', 'P_2', 'P_3', 'P_4']
        self.timeline_bars = {}  # Dictionary to store timelines for each pigeon

        # GUI components
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pigeon Behavior Annotation Tool')
        self.setFixedSize(1200, 800)  # Fixed window size to prevent resizing

        # Video display label
        self.video_label = QLabel(self)
        self.video_label.setScaledContents(True)  # Allow scaling
        self.video_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Frame information label
        self.frame_info_label = QLabel("Frame: 0 / 0", self)

        # Pigeon selection
        self.pigeon_selector = QComboBox(self)
        self.pigeon_selector.addItems(self.pigeons)

        # Behavior selection
        self.behavior_selector = QComboBox(self)
        self.behavior_selector.addItems(['eating', 'drinking', 'other', 'walk'])

        # Control buttons
        self.load_button = QPushButton('Load Video', self)
        self.load_button.clicked.connect(self.load_video)

        self.prev_button = QPushButton('Previous Frame', self)
        self.prev_button.clicked.connect(self.prev_frame)

        self.next_button = QPushButton('Next Frame', self)
        self.next_button.clicked.connect(self.next_frame)

        self.start_action_button = QPushButton('Start Action', self)
        self.start_action_button.clicked.connect(self.start_action)

        self.end_action_button = QPushButton('End Action', self)
        self.end_action_button.clicked.connect(self.end_action)

        self.export_button = QPushButton('Export Annotations', self)
        self.export_button.clicked.connect(self.export_annotations)

        # New export button for sorted format
        self.export_sorted_button = QPushButton('Export Sorted Format', self)
        self.export_sorted_button.clicked.connect(self.export_sorted_annotations)

        # Video progress bar
        self.progress_slider = QSlider(Qt.Horizontal, self)
        self.progress_slider.sliderMoved.connect(self.slider_moved)
        self.progress_slider.sliderPressed.connect(self.slider_pressed)
        self.progress_slider.sliderReleased.connect(self.slider_released)

        # Timeline layout for each pigeon
        timeline_layout = QVBoxLayout()
        for pigeon in self.pigeons:
            row_layout = QHBoxLayout()  # Row layout for each timeline with label

            label = QLabel(pigeon, self)  # Label for the pigeon ID
            timeline_bar = QLabel(self)  # Label to represent the timeline
            timeline_bar.setFixedHeight(20)
            timeline_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Set to expand horizontally
            timeline_bar.setStyleSheet("background-color: white; border: 1px solid black;")

            # Store the timeline bar in a dictionary for easy access
            self.timeline_bars[pigeon] = timeline_bar

            # Add to row layout: pigeon label on the left, timeline bar on the right
            row_layout.addWidget(label)
            row_layout.addWidget(timeline_bar)
            timeline_layout.addLayout(row_layout)

        # Layout for controls
        controls_layout = QHBoxLayout()
        controls_layout.addWidget(self.load_button)
        controls_layout.addWidget(self.prev_button)
        controls_layout.addWidget(self.next_button)
        controls_layout.addWidget(self.pigeon_selector)
        controls_layout.addWidget(self.behavior_selector)
        controls_layout.addWidget(self.start_action_button)
        controls_layout.addWidget(self.end_action_button)
        controls_layout.addWidget(self.export_button)
        controls_layout.addWidget(self.export_sorted_button)  # Add the new button to the layout

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.video_label)
        main_layout.addWidget(self.frame_info_label, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.progress_slider)
        main_layout.addLayout(timeline_layout)
        main_layout.addLayout(controls_layout)

        # Set main layout
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def load_video(self):
        self.video_path, _ = QFileDialog.getOpenFileName(self, 'Open Video')
        if self.video_path:
            if self.cap:
                self.cap.release()
            self.cap = cv2.VideoCapture(self.video_path)
            if not self.cap.isOpened():
                print("Error: Cannot open video.")
                return

            self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.progress_slider.setRange(0, self.total_frames - 1)
            self.current_frame = 0
            self.update_frame_info()
            self.show_frame()

    def show_frame(self):
        if not self.cap or not self.cap.isOpened():
            return
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Cannot read frame.")
            return
        frame = cv2.resize(frame, (0, 0), fx=self.downscale_factor, fy=self.downscale_factor)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w = frame.shape[:2]
        qimg = QImage(frame.data, w, h, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))
        self.progress_slider.setValue(self.current_frame)
        self.update_frame_info()
        self.update_action_visualization()

    def update_frame_info(self):
        self.frame_info_label.setText(f"Frame: {self.current_frame} / {self.total_frames}")

    def prev_frame(self):
        if self.current_frame > 0:
            self.current_frame -= 1
            self.show_frame()

    def next_frame(self):
        if self.current_frame < self.total_frames - 1:
            self.current_frame += 1
            self.show_frame()

    def slider_moved(self, position):
        self.current_frame = position
        self.show_frame()

    def slider_pressed(self):
        if self.cap:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)

    def slider_released(self):
        self.show_frame()

    def start_action(self):
        pigeon = self.pigeon_selector.currentText()
        behavior = self.behavior_selector.currentText()
        
        # Ensure any existing action is finalized before starting a new one
        if self.current_action is not None:
            self.end_action()

        self.current_action = {
            'pigeon_id': pigeon,
            'action_label': behavior,
            'start_frame': self.current_frame,
            'end_frame': None
        }
        
        # Update action visualization with both past and current actions visible
        self.update_action_visualization()

    def end_action(self):
        if self.current_action:
            # Save only the start and end of the action for Export Annotations
            self.current_action['end_frame'] = self.current_frame
            # Append the current action as a single row
            self.annotations.append({
                'pigeon_id': self.current_action['pigeon_id'],
                'start_frame': self.current_action['start_frame'],
                'end_frame': self.current_action['end_frame'],
                'action_label': self.current_action['action_label']
            })
            self.current_action = None
            self.update_timeline()  # Finalize timeline for this pigeon

    def export_annotations(self):
        """Export annotations to a default CSV format with start and end frames."""
        if self.annotations:
            # Export in the format: pigeon_id, start_frame, end_frame, action_label
            df = pd.DataFrame(self.annotations)[['pigeon_id', 'start_frame', 'end_frame', 'action_label']]
            df.to_csv('annotations.csv', index=False)
            print("Annotations exported to annotations.csv")

    def export_sorted_annotations(self):
        """Export annotations in sorted format with each frame represented individually."""
        if self.annotations:
            # Expand each action into individual frames with frame_id
            expanded_data = []
            for annotation in self.annotations:
                for frame_id in range(annotation['start_frame'], annotation['end_frame'] + 1):
                    expanded_data.append({
                        'frame_id': frame_id,
                        'pigeon_id': annotation['pigeon_id'],
                        'action_label': annotation['action_label']
                    })

            # Convert to DataFrame, sort by frame_id, and export
            sorted_df = pd.DataFrame(expanded_data).sort_values(by='frame_id').reset_index(drop=True)
            sorted_df.to_csv('annotations_sorted.csv', index=False, mode='w')  # Overwrite the file
            print("Sorted annotations exported to annotations_sorted.csv")

    def update_action_visualization(self):
        # Update the visualization of both current and past actions on the selected pigeon timeline
        if self.current_action:
            pigeon = self.current_action['pigeon_id']
            timeline_bar = self.timeline_bars[pigeon]
            start_frame = self.current_action['start_frame']
            current_frame = self.current_frame

            # Calculate start and current positions on the timeline
            start_x = int(start_frame / self.total_frames * timeline_bar.width())
            end_x = int(current_frame / self.total_frames * timeline_bar.width())
            width = end_x - start_x

            # Create an image for the timeline and draw both past and current actions
            timeline_image = QImage(timeline_bar.width(), timeline_bar.height(), QImage.Format_RGB32)
            timeline_image.fill(Qt.white)  # Background color

            painter = QPainter(timeline_image)

            # Draw all past annotations for this pigeon with the correct colors
            for annotation in self.annotations:
                if annotation['pigeon_id'] == pigeon:
                    past_start_x = int(annotation['start_frame'] / self.total_frames * timeline_bar.width())
                    past_end_x = int(annotation['end_frame'] / self.total_frames * timeline_bar.width())
                    color = QColor("red") if annotation['action_label'] == 'eating' else \
                            QColor("blue") if annotation['action_label'] == 'drinking' else \
                            QColor("green") if annotation['action_label'] == 'other' else \
                            QColor("yellow")
                    painter.fillRect(past_start_x, 0, past_end_x - past_start_x, timeline_bar.height(), color)

            # Draw start marker for the current action
            painter.setPen(QColor("black"))
            painter.drawLine(start_x, 0, start_x, timeline_bar.height())

            # Draw the current action rectangle from start to the current frame
            color = QColor("red") if self.current_action['action_label'] == 'eating' else \
                    QColor("blue") if self.current_action['action_label'] == 'drinking' else \
                    QColor("green") if self.current_action['action_label'] == 'other' else \
                    QColor("yellow")
            painter.fillRect(start_x, 0, width, timeline_bar.height(), color)

            painter.end()
            timeline_bar.setPixmap(QPixmap.fromImage(timeline_image))

    def update_timeline(self):
        # Update the timeline display for all pigeons, showing finalized actions
        for pigeon, timeline_bar in self.timeline_bars.items():
            timeline_image = QImage(timeline_bar.width(), timeline_bar.height(), QImage.Format_RGB32)
            timeline_image.fill(Qt.white)

            painter = QPainter(timeline_image)
            for annotation in self.annotations:
                if annotation['pigeon_id'] == pigeon:
                    start_x = int(annotation['start_frame'] / self.total_frames * timeline_bar.width())
                    end_x = int(annotation['end_frame'] / self.total_frames * timeline_bar.width())
                    width = end_x - start_x
                    color = QColor("red") if annotation['action_label'] == 'eating' else \
                            QColor("blue") if annotation['action_label'] == 'drinking' else \
                            QColor("green") if annotation['action_label'] == 'other' else \
                            QColor("yellow")
                    painter.fillRect(start_x, 0, width, timeline_bar.height(), color)

            painter.end()
            timeline_bar.setPixmap(QPixmap.fromImage(timeline_image))

    def keyPressEvent(self, event):
        """Handle key press events for shortcuts."""
        key = event.key()

        # Navigation shortcuts
        if key == Qt.Key_D:  # Pressing 'D' for Next Frame
            self.next_frame()
        elif key == Qt.Key_S:  # Pressing 'S' for Previous Frame
            self.prev_frame()

        # Pigeon selection shortcuts
        elif key == Qt.Key_1:  # Pressing '1' for P_1
            self.pigeon_selector.setCurrentIndex(0)
        elif key == Qt.Key_2:  # Pressing '2' for P_2
            self.pigeon_selector.setCurrentIndex(1)
        elif key == Qt.Key_3:  # Pressing '3' for P_3
            self.pigeon_selector.setCurrentIndex(2)
        elif key == Qt.Key_4:  # Pressing '4' for P_4
            self.pigeon_selector.setCurrentIndex(3)

def main():
    app = QApplication(sys.argv)
    window = AnnotationTool()
    window.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()