'''Implements KMeans clustering'''

import numpy as np


class KMeans:
    def __init__(self, num_centroids:int, data=None):
        self.num_centroids = num_centroids
        if data:
            self.centroids = self._create_centroids(data)

    def _create_centroids(self, data):
        if not hasattr(data, 'shape'):
            raise TypeError('data must implement shape')
        try:
            centroids = [np.random.rand(1, data.shape[1]) for _ in range(self.num_centroids)]
        except IndexError:
            raise IndexError(f'shape {data.shape} is invalid. Expected at least 2-dimensions')

        return centroids

    def nearest_centroid(self, datum):
        distances = [np.linalg.norm(centroid-datum) for centroid in self.centroids]
        return distances.index(min(distances))

    def _recalculate_centroids(self):
        labels = np.unique(self.lables)
        self.centroids = np.asarray()

    def fit(self, data=None):
        if data:
            self.centroids = self._create_centroids(data)
        if not hasattr(self, 'centroids'):
            raise AttributeError("data must be set either on instantiation or in fit")

