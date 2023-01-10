import math

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from pageGenerator.models import ScoreModel

class BMIModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name = 'bmi')
    created = models.DateTimeField(auto_now=True, editable=False)
    height = models.FloatField(verbose_name="height")
    mass = models.FloatField(verbose_name="weight")
    bmi = models.FloatField(editable=False)

    class Meta:
        get_latest_by = 'created'

    def save(self, *args, **kwargs):
        self.bmi = self.mass / self.height**2
        super(BMIModel, self).save(*args, **kwargs)
        ScoreModel.calculate_score(self.user)


class ADSModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name="ads")
    created = models.DateTimeField(auto_now_add = True, editable=False)

    YN_Choice = (("0", "No"), ("1", "Yes"))

    class Meta:
        get_latest_by = 'created'

    def save(self, *args, **kwargs):
        self.score = 0

        for att in self._meta.get_fields():
            if att.name in ['id', 'user', 'created', 'score']:
                continue
            
            self.score += int(getattr(self,att.name))
        
        super(ADSModel, self).save(*args, **kwargs)
        ScoreModel.calculate_score(self.user)

    q1 = models.CharField(
        verbose_name = "Do you get belligerent or mean when you drink?",
        choices = (
            ("0", "No"),
            ("1", "Yes sometimes"),
            ("2", "Yes, usually")
        ),
        max_length=50,
        default=None,
    )

    q2 = models.CharField(
        verbose_name="Have you had blackouts (\"loss of memory\" without passing out) as a result of drinking?",
        choices=(
            ("0", "No, never"),
            ("1", "Sometimes"),
            ("2", "Often"),
            ("3", "Almost every time I drink")
        ),
        max_length=50,
        default=None,
    )

    q3 = models.CharField(
        verbose_name= "How much did you drink the last time you drank?",
        choices= (
            ("0", "Enough to get high or less"),
            ("1", "Enough to get drunk"),
            ("2", "Enough to pass out")
        ),
        max_length=50,
        default=None,
    )

    q4 = models.CharField(
        verbose_name= "Have you passed out as a result of drinking?",
        choices=(
            ("0", "No"),
            ("1", "About once a year"),
            ("2", "Twice a year or more")
        ),
        max_length=50,
        default=None,
    )

    q5 = models.CharField(
        verbose_name= "When you drink, do you stumble about, stagger and weave?",
        choices= (
            ("0", "No"),
            ("1", "Sometimes"),
            ("2", "Often")
        ),
        max_length=50,
        default=None,
    )

    q6 = models.CharField(
        verbose_name= "Do you gulp drinks (drink quickly)?",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )

    q7 = models.CharField(
        verbose_name="As a result of being drunk, has your thinking been fuzzy or unclear?",
        choices = (
            ("0", "No"),
            ("1","Yes, but only for a few hours"),
            ("2","Yes, for one or two days"),
            ("3", "Yes, for many days")
        ),
        max_length=50,
        default=None,
    )

    q8 = models.CharField(
        verbose_name="Have you had a convulsion (fit) following a period of drinking?",
        choices=(
            ("0", "No"),
            ("1","Once"),
            ("2", "Several times")
        ),
        max_length=50,
        default=None,
    )

    q9 = models.CharField(
        verbose_name="Do you panic because you fear you may not have a drink when you need it?",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )

    q10 = models.CharField(
        verbose_name="Do you sneak drinks or hide bottles?",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )

    q11 = models.CharField(
        verbose_name="Do you lose control over what you do when you are drinking? ",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )

    q12 = models.CharField(
        verbose_name= "As a result of drinking, have you seen things that were not there?",
        choices= (
            ("0", "No"),
            ("1", "Yes, once"),
            ("2","Yes, several times")
        ),
        max_length=50,
        default=None,
    )

    q13 = models.CharField(
        verbose_name="Have you had \"shakes\" when sobering up (hands tremble, shake inside, etc.) as a result of drinking?",
        choices = (
            ("0", "No"),
            ("1", "Yes sometimes"),
            ("2", "Yes, almost every time I drink")
        ),
        max_length=50,
        default=None,
    )

    q14 = models.CharField(
        verbose_name = "Do you usually have a bottle by your bedside?",
        choices = YN_Choice,
        max_length=50,
        default=None,
    )

    q15 = models.CharField(
        verbose_name="Do you drink throughout the day?",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )

    q16 = models.CharField(
        verbose_name="With respect to blackouts (loss of memory):",
        choices=(
            ("0", "Have never had a blackout"),
            ("1","Have had blackouts that last less than an hour"),
            ("2","Have had blackouts that last for several hours"),
            ("3","Have had blackouts that last for a day or more")
        ),
        max_length=50,
        default=None,
    )

    q17 = models.CharField(
        verbose_name = "As a result of drinking have you heard \"things\" that were not there?",
        choices=(
            ("0","No"),
            ("1","Yes once"),
            ("2","Yes, sereval times")
        ),
        max_length=50,
        default=None,
    )

    q18 = models.CharField(
        verbose_name = "Do you often have hangovers on Sunday or Monday mornings?",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )

    q19 = models.CharField(
        verbose_name="Do you almost constantly think about drinking and alcohol?",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )

    q20 = models.CharField(
        verbose_name="Do you tend to be physically harmful to other people when drinking?",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )

    q21 = models.CharField(
        verbose_name = "Have you had weird and frightening sensations when drinking?",
        choices=(
            ("0", "No"),
            ("1", "Yes, perhaps once or twice"),
            ("2", "Yes, often")
        ),
        max_length=50,
        default=None,
    )

    q22 = models.CharField(
        verbose_name="As a result of drinking have you \"felt things\" crawling on you that were not there (bugs, spiders, etc.)?",
        choices=(
            ("0", "No"),
            ("1", "Once"),
            ("2", "Several times")
        ),
        max_length=50,
        default=None,
    )

    q23 = models.CharField(
        verbose_name="Do you get physically sick (vomit, stomach cramps, etc.) as a result of drinking?",
        choices=(
            ("0", "No"),
            ("1", "Sometimes"),
            ("2","Almost every time I drink")
        ),
        max_length=50,
        default=None,
    )

    q24 = models.CharField(
        verbose_name="Do you carry a bottle with you or keep one close at hand?",
        choices=(
            ("0", "No"),
            ("1","Some of the time"),
            ("2","Most of the time")
        ),
        max_length=50,
        default=None,
    )

    q25 = models.CharField(
        verbose_name="Have you ever attempted suicide when drinking?", 
        choices=(
            ("0","Never"),
            ("1","Once"),
            ("2","Several times")
        ),
        max_length=50,
        default=None,
    )

    q26 = models.CharField(
        verbose_name="As a result of drinking, have you ever had delirium tremens or DT's (seen, felt, or heard things not really there)?",
        choices=(
            ("0","No"),
            ("1","Yes, once"),
            ("2","Several times")
        ),
        max_length=50,
        default=None,
    )

    q27 = models.CharField(
        verbose_name="As a result of drinking have you felt your heart beating rapidly?",
        choices=(
            ("0","No"),
            ("1","Yes, once"),
            ("2", "Yes, several times")
        ),
        max_length=50,
        default=None,
    )

    q28 = models.CharField(
        verbose_name="As a result of drinking have you felt overly hot and sweaty (feverish)?",
        choices=(
            ("0","No"),
            ("1", "Yes, once"),
            ("2","Yes, several times")
        ),
        max_length=50,
        default=None,
    )

    q29 = models.CharField(
        verbose_name="Do you drink during your work day?",
        choices=YN_Choice,
        max_length=50,
        default=None,
    )  

    score = models.IntegerField(null=True,blank=True,editable=False)

class CDSModel(models.Model):
    Disagree_Choice = (("1", "Totally disagree"), ("2", "Somewhat disagree"), ("3", "Neither agree nor disagree"), ("4", "Somewhat agree"), ("5", "Fully agree"))

    class Meta:
        get_latest_by = 'created'

    def validate_between_0_100(value):
        if value < 0 or value > 100:
            raise ValueError(
                _('%(value)s is not between 0 and 100'),
                params = {'value': value},
            )

    def save(self, *args, **kwargs):
        self.score = 0

        for att in self._meta.get_fields():
            if att.name in ['id', 'user', 'created', 'score','q1','q2','q3']:
                continue
            
            self.score += int(getattr(self,att.name))

        q1_score = math.ceil(getattr(self, 'q1')/5)
        if q1_score < 1:
            self.score += 1
        elif q1_score > 5:
            self.score += 5
        else:
            self.score += q1_score

        q2_score = getattr(self, 'q2')
        if q2_score <=5:
            self.score += 1
        elif q2_score <= 10:
            self.score += 2
        elif q2_score <= 20:
            self.score += 3
        elif q2_score <= 29:
            self.score += 4
        else:
            self.score += 5

        q3_score = getattr(self, 'q3')
        if q3_score <= 5:
            self.score += 1
        elif q3_score <=15:
            self.score += 2
        elif q3_score <=30:
            self.score += 3
        elif q3_score <= 60:
            self.score += 4
        else:
            self.score += 5

        super(CDSModel, self).save(*args, **kwargs)
        ScoreModel.calculate_score(self.user)

    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='cds')
    created = models.DateTimeField(auto_now_add = True, editable=False)
    
    q1 = models.IntegerField(
        verbose_name= "Please rate your cigarette addiction on a scale from 0 to 100 with 0 being not addicted and 100 being extremely addicted.",
        # validators=[validate_between_0_100]
    )      

    q2 = models.IntegerField(
        verbose_name="On average, how many cigarettes do you smoke per day?",
        # validators=[validate_between_0_100]
    )

    q3 = models.IntegerField(
        verbose_name="How soon after waking up do you smoke your first cigarette?",
        # validators=[validate_between_0_100]
    )

    q4 = models.CharField(
        null=True,
        max_length=20,
        verbose_name="For you, quitting smoking for good would be:", 
        choices=(
            ("5","Impossible"),
            ("4","Very difficult"),
            ("3","Fairly difficult"),
            ("2","Fairly easy"),
            ("1","Very easy")
        ),
        default = None,
    )

    q5 = models.CharField(
        max_length=20,
        verbose_name="After a few hours without smoking, I feel an irresistable urge to smoke.",
        choices = Disagree_Choice,
        default = None,
    )

    q6 = models.CharField(
        max_length=20,
        verbose_name="The idea of not having any cigarettes causes me stress.",
        choices = Disagree_Choice,
        default = None,
    )

    q7 = models.CharField(
        max_length=20,
        verbose_name="Before going out, I always make sure that I have cigarettes with me.",
        choices = Disagree_Choice,
        default = None,
    )

    q8 = models.CharField(
        max_length=20,
        verbose_name="I am a prisoner of cigarettes.",
        choices = Disagree_Choice,
        default = None,
    )

    q9 = models.CharField(
        max_length=20,
        verbose_name="I smoke too much.",
        choices = Disagree_Choice,
        default = None,
    )

    q10 = models.CharField(
        max_length=20,
        verbose_name="Sometimes I drop everything to go out and buy cigarettes",
        choices = Disagree_Choice,
        default = None,
    )

    q11 = models.CharField(
        max_length=20,
        verbose_name="I smoke all the time.",
        choices = Disagree_Choice,
        default = None,
    )

    q12 = models.CharField(
        max_length=20,
        verbose_name="I smoke despite the risks to my health",
        choices = Disagree_Choice,
        default = None,
    )

    score = models.IntegerField(null=True,blank=True,editable=False)
