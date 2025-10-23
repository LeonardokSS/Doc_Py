from ultralytics import YOLO
import cv2
import time
from collections import Counter

MODEL_PATH = "yolov8n.pt"
SAVE_OUTPUT = True
OUTPUT_FILE = "video.avi"
CAMERA_INDEX = 0



model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(CAMERA_INDEX)
if not cap.isOpened():
    raise RuntimeError("Não foi possível abrir a câmera.")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_input = cap.get(cv2.CAP_PROP_FPS) or 30.0

if SAVE_OUTPUT:
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(OUTPUT_FILE, fourcc, fps_input, (width, height))

prev_time = 0.0
frame_count = 0
total_time = 0.0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame não recebido — encerrando.")
        break

    start = time.time()
    results = model(frame)
    annotated = frame.copy()
    detections = results[0]

    boxes = detections.boxes.xyxy.tolist() if detections.boxes is not None else []
    scores = detections.boxes.conf.tolist() if detections.boxes is not None else []
    classes = detections.boxes.cls.tolist() if detections.boxes is not None else []
    names = [model.names[int(c)] for c in classes] if classes else []

    counts = Counter()
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box)
        score = scores[i]
        label = names[i]
        counts[label] += 1
        cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
        text = f"{label} {score:.2f}"
        cv2.putText(annotated, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    y0 = 20
    for k, v in counts.items():
        cv2.putText(annotated, f"{k}: {v}", (10, y0), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        y0 += 25

    end = time.time()
    elapsed = end - start
    total_time += elapsed
    frame_count += 1
    fps = 1.0 / elapsed if elapsed > 0 else 0.0
    cv2.putText(annotated, f"FPS: {fps:.1f}", (width - 120, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("YOLOv8 - Detector", annotated)
    if SAVE_OUTPUT:
        out.write(annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
if SAVE_OUTPUT:
    out.release()
cv2.destroyAllWindows()

if frame_count > 0:
    print(f"Frames processados: {frame_count}, Tempo total: {total_time:.2f}s, FPS médio: {frame_count/total_time:.2f}")
