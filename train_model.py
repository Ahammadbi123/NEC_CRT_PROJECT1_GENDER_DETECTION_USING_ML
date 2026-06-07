import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
import joblib
import os

def extract_features(name):
    name = str(name).lower().strip()
    return {
        'last_1': name[-1],
        'last_2': name[-2:],
        'last_3': name[-3:],
        'last_4': name[-4:],
        'first_2': name[:2],
        'first_3': name[:3],
        'vowels': sum(1 for c in name if c in 'aeiou'),
        'length': len(name)
    }

# Load Big CSV
df = pd.read_csv('dataset.csv')
X_list = [extract_features(n) for n in df['name']]
dv = DictVectorizer()
X = dv.fit_transform(X_list)
y = df['gender']

# High-Power ML Training
model = RandomForestClassifier(n_estimators=500, max_depth=None, random_state=42)
model.fit(X, y)

# Save
if not os.path.exists('model'): os.makedirs('model')
joblib.dump(model, 'model/expert_model.pkl')
joblib.dump(dv, 'model/vectorizer.pkl')

print("🚀 ML Model trained on Big Data successfully!")