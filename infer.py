from ultralytics import YOLO
import sys
import os

def run_inference(image_path, model_path="models/best.pt"):
    if not os.path.exists(image_path):
        print(f"❌ Error: Could not find image or video at '{image_path}'")
        return
        
    if not os.path.exists(model_path):
        print(f"❌ Error: Model not found at '{model_path}'. Check your 'models' folder!")
        return

    print(f"🧠 Loading YOLO model from {model_path}...")
    try:
        model = YOLO(model_path)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    print(f"🔍 Running inference on {image_path}...")
    
    # Run prediction and save the output image/video automatically
    results = model.predict(source=image_path, save=True, conf=0.5)
    
    print("\n✅ Inference complete!")
    print(f"📁 Protected results saved to the generated folder: {results[0].save_dir}")

if __name__ == "__main__":
    print("--- YOLOvx Testing Script ---")
    if len(sys.argv) < 2:
        print("Usage Instructions:")
        print("  python infer.py <path_to_image_or_video> [optional_path_to_model]")
        print("\nExample:")
        print("  python infer.py sample_car.jpg")
    else:
        # Grab image path from terminal
        img = sys.argv[1]
        
        # Grab model path if they provided one, otherwise default to best.pt
        mod = sys.argv[2] if len(sys.argv) > 2 else "models/best.pt"
        
        run_inference(img, mod)
