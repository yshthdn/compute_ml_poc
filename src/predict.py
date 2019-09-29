from models import ConfidenceLevel


def predict_confidence(model_id):
    confidence_level = ConfidenceLevel.HIGH
    return confidence_level

def get_rule_id(model_id):
    return model_id