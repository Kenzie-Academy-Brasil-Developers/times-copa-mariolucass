from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(null=True, default=0)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    first_cup = models.DateField(max_length=50, null=True)

    def __repr__(self):
        id_Team = self.id
        name_team = self.name
        fifa_code = self.fifa_code

        return f"<{[id_Team]} {name_team} - {fifa_code}>"
