from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

def train_model(data):

    features = data[["Calories","Protein_g","Carbs_g","Fat_g"]]

    scaler = StandardScaler()

    scaled = scaler.fit_transform(features)

    model = NearestNeighbors(n_neighbors=7)

    model.fit(scaled)

    return model, scaler


def recommend_food(data, model, scaler, calories):

    features = data[["Calories","Protein_g","Carbs_g","Fat_g"]]

    scaled = scaler.transform(features)

    user_input = [[calories,20,50,10]]

    user_scaled = scaler.transform(user_input)

    distances, indices = model.kneighbors(user_scaled)

    return data.iloc[indices[0]]