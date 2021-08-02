from django.db import models
from django.urls import reverse

#import uuid

class User(models.Model):
    """Model representing a user with potentially multiple"""
    """submissions"""

    identifier = models.CharField(primary_key=True, max_length=50)
    
    char_name = models.CharField(max_length=20)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                      help_text='Unique ID for this user')

    def __str__(self):
        """String for representing the User object"""
        """of type Model"""
        return f"{self.char_name}"

class Submission(models.Model):
    """Model representing a submission incorporating multiple"""
    """factor submissions"""

    verbose_name = "Submission"

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                      help_text='Unique ID for this submission')

    identifier = models.CharField(primary_key=True, max_length=50)
    
    which_submission = models.IntegerField()

    user = models.ForeignKey('User', on_delete=models.RESTRICT)

    def __str__(self):
        """String for representing the Submission object"""
        """ of type Model"""
        return f"{self.user}|{self.which_submission}"

class FactorSubmission(models.Model):
    """Model representing a submission for a specific"""
    """factor of a specific challenge"""

    verbose_name = "Factor Submission"

    #id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                      help_text='Unique ID for this submission')
    identifier = models.CharField(primary_key=True, max_length=30)

    submission = models.ForeignKey('Submission', on_delete=models.RESTRICT,
                                   null=True)
    
    challenge_tag = models.ForeignKey('ChallengeTag',
                                      on_delete=models.RESTRICT,
                                      null=True)
    factor_tag = models.ForeignKey('FactorTag', on_delete=models.RESTRICT,
                                   null=True)

    time = models.CharField(max_length=10, null=True)
    response1 = models.CharField(max_length=2000, null=True)
    response2 = models.CharField(max_length=2000, null=True)
    
    def __str__(self):
        """String for representing the FactorSubmission object"""
        """ of type Model"""
        return f"{self.challenge_tag}|{self.factor_tag}"

class SubmissionSnapshot(models.Model):
    """Model representing a snapshot of a user's input"""

    identifier = models.CharField(primary_key=True, max_length=30)

    user = models.ForeignKey('User', on_delete=models.RESTRICT,
                             null=True)
    challenge_tag = models.ForeignKey('ChallengeTag',
                                      on_delete=models.RESTRICT,
                                      null=True)
    
    input_snapshot = models.CharField(max_length=2000, verbose_name="Input Snapshot", null=True)

    time = models.IntegerField()

    box = models.CharField(max_length=2, verbose_name="Which Textarea", null=True)

    def __str__(self):
        """String for representing a SubmissionSnapshot"""
        """ object of type Model"""
        return f"Sub-Snap({self.user})({self.time})"

class ChallengeTag(models.Model):
    """Model representing an identifier for a challenge"""

    
    
    tag = models.CharField(primary_key=True,
                           max_length=20,
                           verbose_name="Challenge Tag")

    def __str__(self):
        """String for representing the ChallengeTag object"""
        """ of type Model"""
        return f"{self.tag}"

class FactorTag(models.Model):
    """Model representing an identifier for a factor of"""
    """ a challenge"""

    verbose_name = "Factor Tag"
    tag = models.CharField(primary_key=True,
                           max_length=20, verbose_name="Factor Tag")

    challenge_tag = models.ForeignKey('ChallengeTag',
                                      on_delete=models.RESTRICT,
                                      null=True)
    
    def __str__(self):
        """String for representing the FactorTag object"""
        return f"{self.tag}|{self.challenge_tag}"

class FinalQuestions(models.Model):
    """Model representing responses to the final questions"""
    """ that follow the challenge"""

    identifier = models.CharField(primary_key=True, max_length=50)
    
    verbose_name = "Final Questions"

    submission = models.ForeignKey('Submission', on_delete=models.RESTRICT)

    answers1 = models.CharField(max_length=1000, null=True)
    answers2 = models.CharField(max_length=1000, null=True)

    def __str__(self):
        """String for representing FinalQuestions object"""
        return f"FinalQs|{self.submission}"
