from ..Firmware.target_detector import TargetDetector

# Constants
CAMERA_INDEX: int = 0


TargetDetector(camera_index=CAMERA_INDEX, debug_mode=True).detect_targets()
