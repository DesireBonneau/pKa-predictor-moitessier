# pka_predictor/predict.py

def predict(input_path, pH=7.4, **kwargs):
    """
    A thin wrapper around your core inference code.
    Replace the contents of this function with how you call
    into your GNN/Model code to produce pKa predictions.
    """
    # e.g.
    from .GNN.gnn_model import load_model, infer
    model = load_model(...)
    return infer(model, input_path, pH=pH)
