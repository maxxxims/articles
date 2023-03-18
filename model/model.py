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


def test(m):
    title = "Hundreds surge across US-Mexico bridge (VIDEO) The incident followed rumors that the border was to be opened to grant political asylum to migrants"
    text = "Taiwanese military leaders have reportedly warned that Chinese forces are preparing for a “total blockade” of the Taiwan Strait to prevent foreign troops from gaining access to the self-governing island in the event of a war. Defense spending this year must focus on the blockade threat, earmarking funds to stockpile spare parts for F-16 fighter jets and other weaponry, the Taiwanese Defense Ministry said on Monday, in a report seeking parliamentary budget approval. Since last year, the ministry has been reviewing its strategic fuel reserves and its capacity to repair equipment, said Reuters, which obtained a copy of the report. The Taiwanese military will also need to replenish its stores of artillery shells and rockets “to strengthen combat continuity,” the ministry said. China’s military has been conducting joint force operations “with an eye to controlling strategic choke points and denying access to foreign forces.” “Recently, the communist military’s exercise and training model has been adjusted from a single military type to joint operations of land, sea, air and rocket forces,” the report added. Tensions over the breakaway republic, which China considers to be part of its territory, have escalated since then-US House Speaker Nancy Pelosi traveled to Taipei last August. Beijing, which had warned that such a visit would encourage Taiwanese separatists and undermine its sovereignty, responded by ramping up military exercises around Taiwan and cutting off defense and climate ties with Washington. The Taiwanese Defense Ministry said its budget for this year should prioritize funding for US-made weapons, including Stinger anti-aircraft missiles and the M142 High Mobility Artillery Rocket System (HIMARS). Chinese President Xi Jinping called on Monday for building China’s military into a “great wall of steel” to protect Beijing’s interests and provide greater stability and security. He has refused to rule out reunifying with Taiwan by force, if necessary. China’s defense spending will rise to $230 billion this year, up 7.2% from 2022’s budget. Then-Chinese Premier Li Keqiang vowed earlier this month to “take resolute steps to oppose Taiwan independence.” A US-China war over Taiwan would result in devastating losses for both sides, according to a recent study by the Center for Strategic and International Studies (CSIS), a Washington think tank. A Chinese invasion of Taiwan would ultimately fail, CSIS said, but US and Japanese forces would lose dozens of warships, hundreds of planes and thousands of troops. Taiwan would be left in ruins, “without electricity and basic services.”"
    a, b = m.predict(text, title)

    return a, b