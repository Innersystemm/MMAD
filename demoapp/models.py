from django.db import models


class SignsVector(models.Model):
    userID = models.IntegerField(default=0)
    sign1 = models.IntegerField(default=0)
    sign2 = models.IntegerField(default=0)
    sign3 = models.IntegerField(default=0)
    sign4 = models.IntegerField(default=0)

    def __str__(self):
        return 'user: {0}; signs=[{1}, {2}, {3}, {4}]'.format(self.userID,
                                                              self.sign1,
                                                              self.sign2,
                                                              self.sign3,
                                                              self.sign4)

    def user(self):
        return self.userID

    def signs(self):
        return [self.sign1, self.sign2, self.sign3, self.sign4]

    def vector(self):
        return [self.sign1, self.sign2, self.sign3, self.sign4, self.userID]
