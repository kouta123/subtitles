import os
import json
from watson_developer_cloud import VisualRecognitionV3

class Watson:
    def __init__(self):
        self.visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_api_key=os.environ['WatsonAPI'])

    def predictImage(self,img):
        classes = self.visual_recognition.classify(
            img,
            accept_language='ja',
            parameters = json.dumps({
                'threshold':0.8,
                'classifier_ids': ["default"]
            }))

        return classes["images"][0]['classifiers'][0]['classes'][0]['class']