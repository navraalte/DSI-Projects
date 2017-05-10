import numpy as np


class DBScan(object):

    def __init__(self, eps, min_samples):
        self.eps = eps
        self.min_samples = min_samples

        self.current_cluster = 0

    def fit(self, X):
        self.X = X
        rows, columns = self.X.shape

        self.visted = {point: 0 for point in range(rows)}
        self.point_cluster = {point: 0 for point in range(rows)}

        for point in range(rows):
            if not self.visted[point]:
                self.visted[point] = 1
                neighbors = self.region_query(point)

                if len(neighbors) < self.min_samples:
                    self.point_cluster[point] = -1
                else:
                    self.current_cluster += 1
                    self.expand_cluster(point, neighbors, self.current_cluster)

    def expand_cluster(self, point, neighbors, cluster):
        self.point_cluster[point] = self.current_cluster

        while neighbors:
            neighbor = neighbors.pop()
            if not self.visted[neighbor]:
                self.visted[neighbor] = 1
                neighbors_neighbors = self.region_query(neighbor)

                if len(neighbors_neighbors) >= self.min_samples:
                    neighbors.extend(neighbors_neighbors)

            if not self.point_cluster[neighbor]:
                self.point_cluster[neighbor] = cluster

    def region_query(self, point):
        dists = np.sum(np.square(self.X[point] - self.X), axis=1) ** .5
        neighbors = list(np.where(dists < self.eps)[0])
        return neighbors
