import joblib
from django.shortcuts import render
from .forms import PredictionForm

# Load the trained model
MODEL_PATH = 'predictor/post_quality_model.joblib'
model = joblib.load(MODEL_PATH)['model']
scaler = joblib.load(MODEL_PATH)['scaler']

def predict_view(request):
    prediction = None
    error_message = None
    
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get input data from form
            user_reputation = form.cleaned_data['user_reputation']
            taker_mpxr_delta = form.cleaned_data['taker_mpxr_delta']
            
            try:
                # Prepare data for model prediction
                input_data = [[user_reputation, taker_mpxr_delta]]
                scaled_input = scaler.transform(input_data)
                prediction = round(model.predict(scaled_input)[0], 2)
                
            except Exception as e:
                error_message = f"Error in prediction: {str(e)}"
        else:
            error_message = "Invalid input. Please enter valid numbers."
    else:
        form = PredictionForm()
    
    # Render template with form and prediction result
    return render(request, 'predict.html', {
        'form': form,
        'prediction': prediction,
        'error_message': error_message,
    })
