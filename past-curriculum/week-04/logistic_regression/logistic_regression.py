from __future__ import division
import numpy as np
import numpy.random as rng


class LogisticRegression(object):
    def __init__(self, num_epochs=50, batch_size=64, lrate=0.01):
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.lrate = lrate
        self.loss_history = []
        self.accuracies = []

    def predict_proba(self, X):
        """ calculate probabilities using sigmoid """
        linear_model = X.dot(self.W) + self.b
        prob = 1 / (1 + np.exp(-linear_model))
        return prob

    def predict(self, X, p_thresh=0.5):
        """ predict labels for the classifier """
        proba = self.predict_proba(X)
        # check out the documentation for np.piecewise on the web
        labels = np.piecewise(proba, [proba <= p_thresh, proba > p_thresh], [0, 1])
        return labels

    def loss(self, prob, label):
        """ calculate loss function """
        prob_pos = prob[np.where(label == 1)]
        prob_neg = 1 - prob[np.where(label == 0)]
        return -np.mean(np.log(np.hstack((prob_pos, prob_neg))))

    def accuracy(self, X, y):
        """ calculate the accuracy of the classifier """
        pred_labels = self.predict(X)
        return np.sum(pred_labels == y) / pred_labels.shape[0]

    def fit(self, X, y):
        """ fit the logistic regression using stochastic gradient descent """
        y = np.array(y)
        rows, columns = X.shape
        num_batches = int(np.ceil(rows / self.batch_size))
        batches = np.arange(num_batches + 1) * self.batch_size
        indxs = np.arange(rows)

        self.W = np.zeros(columns)
        self.b = rng.random(1)

        # stochastic gradient descent logic
        for _ in range(self.num_epochs):
            rng.shuffle(indxs)

            for i, j in zip(batches[0:-1], batches[1:]):
                batch_indxs = indxs[i:j]
                x_batch = X[batch_indxs]
                y_batch = y[batch_indxs]
                self.update(x_batch, y_batch)

            # track loss history during training
            self.loss_history.append(self.loss(self.predict_proba(X), y))
            self.accuracies.append(self.accuracy(X, y))

    def update(self, X, y):
        """ logic for updating weight parameters during SGD """
        proba = self.predict_proba(X)
        top_loss = proba - y
        bias_gradient = np.sum(top_loss)
        weight_gradient = (top_loss).T.dot(X)

        # the gradient update
        self.b = self.b - self.lrate * bias_gradient
        self.W = self.W - self.lrate * weight_gradient
