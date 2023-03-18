from catboost import CatBoostClassifier
import numpy as np
import pandas as pd
from model.scripts import Preprocessing


class CLASSIFIER:
    def __init__(self, path_to_model, path_to_csv) -> None:
        self.model = CatBoostClassifier()
        self.model.load_model(path_to_model)
        self.df = pd.read_csv(path_to_csv)

    def predict(self, text, title):
        test = Preprocessing(text, title)
        y_pred = self.model.predict(test)
        y_proba_cb = self.model.predict_proba(test)
        target_names = ['center', 'left', 'right']
        return target_names[y_pred[0][0]], np.max(y_proba_cb)

    def predict_media(self, name):
        if name in list(self.df['link']):
            ans = self.df.loc[self.df['link'] == name]
            if type(list(ans["Bias Rating"])[0]) == float:
                return None
            else:
                return list(ans["Bias Rating"])[0].lower()
        else:
            return None
        
    def find_in_table(self, name):
        d = {}
        if name in list(self.df['link']):
            ans = self.df.loc[self.df['link'] == name]
            for n in ans.columns[1:-2]:
                if type(list(ans[f'{n}'])[0]) != float:
                    d[n] = list(ans[f'{n}'])[0].lower()
            return d
        else:
            return None