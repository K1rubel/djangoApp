# used this to see the kind of object model.save was returning
import joblib

model_path = 'predictor/post_quality_model.joblib'  # Adjust to your actual model path
loaded_object = joblib.load(model_path)

print(type(loaded_object))
print(loaded_object.keys())
print(type(loaded_object['scaler']))
# print(loaded_object['model'])
