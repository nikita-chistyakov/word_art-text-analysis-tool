from sklearn.cluster import KMeans

def cluster_text(comments, n_clusters=3):
    vectorizer = TfidfVectorizer(preprocessor=preprocess_text)
    X = vectorizer.fit_transform(comments)
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(X)
    return model.labels_
