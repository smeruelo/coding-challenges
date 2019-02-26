# https://exercism.io/my/solutions/688b6682a4b64539913093760d92c1c8


class HighScores(object):
    """Collection of high scores."""

    def __init__(self, scores):
        self._scores = scores

    @property
    def scores(self):
        return self._scores

    def latest(self):
        """Returns the latest score."""
        try:
            return self.scores[-1]
        except IndexError:
            raise Exception("There are no scores.")

    def personal_best(self):
        """Returns the highest score."""
        try:
            return sorted(self.scores, reverse=True)[0]
        except IndexError:
            raise Exception("There are no scores.")

    def personal_top_three(self):
        """Returns the three highest scores."""
        top_three = sorted(self.scores, reverse=True)[:3]
        if top_three:
            return top_three
        else:
            raise Exception("There are no scores.")
