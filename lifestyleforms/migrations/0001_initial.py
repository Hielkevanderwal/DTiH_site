# Generated by Django 4.1.3 on 2022-12-20 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CDSModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "q1",
                    models.IntegerField(
                        verbose_name="Please rate your cigarette addiction on a scale from 0 to 100 with 0 being not addicted and 100 being extremely addicted."
                    ),
                ),
                (
                    "q2",
                    models.IntegerField(
                        verbose_name="On average, how many cigarettes do you smoke per day?"
                    ),
                ),
                (
                    "q3",
                    models.IntegerField(
                        verbose_name="How soon after waking up do you smoke your first cigarette?"
                    ),
                ),
                (
                    "q4",
                    models.CharField(
                        choices=[
                            ("1", "Impossible"),
                            ("2", "Very difficult"),
                            ("3", "Fairly difficult"),
                            ("4", "Fairly easy"),
                            ("5", "Very easy"),
                        ],
                        default=None,
                        max_length=20,
                        null=True,
                        verbose_name="For you, quitting smoking for good would be:",
                    ),
                ),
                (
                    "q5",
                    models.CharField(
                        choices=[
                            ("0", "Totally disagree"),
                            ("1", "Somewhat disagree"),
                            ("2", "Neither agree nor disagree"),
                            ("3", "Somewhat agree"),
                            ("4", "Fully agree"),
                        ],
                        default=None,
                        max_length=20,
                        verbose_name="After a few hours without smoking, I feel an irresistable urge to smoke.",
                    ),
                ),
                (
                    "q6",
                    models.CharField(
                        choices=[
                            ("0", "Totally disagree"),
                            ("1", "Somewhat disagree"),
                            ("2", "Neither agree nor disagree"),
                            ("3", "Somewhat agree"),
                            ("4", "Fully agree"),
                        ],
                        default=None,
                        max_length=20,
                        verbose_name="The idea of not having any cigarettes causes me stress.",
                    ),
                ),
                (
                    "q7",
                    models.CharField(
                        choices=[
                            ("0", "Totally disagree"),
                            ("1", "Somewhat disagree"),
                            ("2", "Neither agree nor disagree"),
                            ("3", "Somewhat agree"),
                            ("4", "Fully agree"),
                        ],
                        default=None,
                        max_length=20,
                        verbose_name="Before going out, I always make sure that I have cigarettes with me.",
                    ),
                ),
                (
                    "q8",
                    models.CharField(
                        choices=[
                            ("0", "Totally disagree"),
                            ("1", "Somewhat disagree"),
                            ("2", "Neither agree nor disagree"),
                            ("3", "Somewhat agree"),
                            ("4", "Fully agree"),
                        ],
                        default=None,
                        max_length=20,
                        verbose_name="I am a prisoner of cigarettes.",
                    ),
                ),
                (
                    "q9",
                    models.CharField(
                        choices=[
                            ("0", "Totally disagree"),
                            ("1", "Somewhat disagree"),
                            ("2", "Neither agree nor disagree"),
                            ("3", "Somewhat agree"),
                            ("4", "Fully agree"),
                        ],
                        default=None,
                        max_length=20,
                        verbose_name="I smoke too much.",
                    ),
                ),
                (
                    "q10",
                    models.CharField(
                        choices=[
                            ("0", "Totally disagree"),
                            ("1", "Somewhat disagree"),
                            ("2", "Neither agree nor disagree"),
                            ("3", "Somewhat agree"),
                            ("4", "Fully agree"),
                        ],
                        default=None,
                        max_length=20,
                        verbose_name="Sometimes I drop everything to go out and buy cigarettes",
                    ),
                ),
                (
                    "q11",
                    models.CharField(
                        choices=[
                            ("0", "Totally disagree"),
                            ("1", "Somewhat disagree"),
                            ("2", "Neither agree nor disagree"),
                            ("3", "Somewhat agree"),
                            ("4", "Fully agree"),
                        ],
                        default=None,
                        max_length=20,
                        verbose_name="I smoke all the time.",
                    ),
                ),
                (
                    "q12",
                    models.CharField(
                        choices=[
                            ("0", "Totally disagree"),
                            ("1", "Somewhat disagree"),
                            ("2", "Neither agree nor disagree"),
                            ("3", "Somewhat agree"),
                            ("4", "Fully agree"),
                        ],
                        default=None,
                        max_length=20,
                        verbose_name="I smoke despite the risks to my health",
                    ),
                ),
                ("score", models.IntegerField(blank=True, editable=False, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cds",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"get_latest_by": "created",},
        ),
        migrations.CreateModel(
            name="BMIModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now=True)),
                ("height", models.FloatField(verbose_name="height")),
                ("mass", models.FloatField(verbose_name="weight")),
                ("bmi", models.FloatField(editable=False)),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bmi",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"get_latest_by": "created",},
        ),
        migrations.CreateModel(
            name="ADSModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "q1",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes sometimes"),
                            ("2", "Yes, usually"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="Do you get belligerent or mean when you drink?",
                    ),
                ),
                (
                    "q2",
                    models.CharField(
                        choices=[
                            ("0", "No, never"),
                            ("1", "Sometimes"),
                            ("2", "Often"),
                            ("3", "Almost every time I drink"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name='Have you had blackouts ("loss of memory" without passing out) as a result of drinking?',
                    ),
                ),
                (
                    "q3",
                    models.CharField(
                        choices=[
                            ("0", "Enough to get high or less"),
                            ("1", "Enough to get drunk"),
                            ("2", "Enough to pass out"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="How much did you drink the last time you drank?",
                    ),
                ),
                (
                    "q4",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "About once a year"),
                            ("2", "Twice a year or more"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="Have you passed out as a result of drinking?",
                    ),
                ),
                (
                    "q5",
                    models.CharField(
                        choices=[("0", "No"), ("1", "Sometimes"), ("2", "Often")],
                        default=None,
                        max_length=50,
                        verbose_name="When you drink, do you stumble about, stagger and weave?",
                    ),
                ),
                (
                    "q6",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you gulp drinks (drink quickly)?",
                    ),
                ),
                (
                    "q7",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes, but only for a few hours"),
                            ("2", "Yes, for one or two days"),
                            ("3", "Yes, for many days"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="As a result of being drunk, has your thinking been fuzzy or unclear?",
                    ),
                ),
                (
                    "q8",
                    models.CharField(
                        choices=[("0", "No"), ("1", "Once"), ("2", "Several times")],
                        default=None,
                        max_length=50,
                        verbose_name="Have you had a convulsion (fit) following a period of drinking?",
                    ),
                ),
                (
                    "q9",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you panic because you fear you may not have a drink when you need it?",
                    ),
                ),
                (
                    "q10",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you sneak drinks or hide bottles?",
                    ),
                ),
                (
                    "q11",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you lose control over what you do when you are drinking? ",
                    ),
                ),
                (
                    "q12",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes, once"),
                            ("2", "Yes, several times"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="As a result of drinking, have you seen things that were not there?",
                    ),
                ),
                (
                    "q13",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes sometimes"),
                            ("2", "Yes, almost every time I drink"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name='Have you had "shakes" when sobering up (hands tremble, shake inside, etc.) as a result of drinking?',
                    ),
                ),
                (
                    "q14",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you usually have a bottle by your bedside?",
                    ),
                ),
                (
                    "q15",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you drink throughout the day?",
                    ),
                ),
                (
                    "q16",
                    models.CharField(
                        choices=[
                            ("0", "Have never had a blackout"),
                            ("1", "Have had blackouts that last less than an hour"),
                            ("2", "Have had blackouts that last for several hours"),
                            ("3", "Have had blackouts that last for a day or more"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="With respect to blackouts (loss of memory):",
                    ),
                ),
                (
                    "q17",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes once"),
                            ("2", "Yes, sereval times"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name='As a result of drinking have you heard "things" that were not there?',
                    ),
                ),
                (
                    "q18",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you often have hangovers on Sunday or Monday mornings?",
                    ),
                ),
                (
                    "q19",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you almost constantly think about drinking and alcohol?",
                    ),
                ),
                (
                    "q20",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you tend to be physically harmful to other people when drinking?",
                    ),
                ),
                (
                    "q21",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes, perhaps once or twice"),
                            ("2", "Yes, often"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="Have you had weird and frightening sensations when drinking?",
                    ),
                ),
                (
                    "q22",
                    models.CharField(
                        choices=[("0", "No"), ("1", "Once"), ("2", "Several times")],
                        default=None,
                        max_length=50,
                        verbose_name='As a result of drinking have you "felt things" crawling on you that were not there (bugs, spiders, etc.)?',
                    ),
                ),
                (
                    "q23",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Sometimes"),
                            ("2", "Almost every time I drink"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="Do you get physically sick (vomit, stomach cramps, etc.) as a result of drinking?",
                    ),
                ),
                (
                    "q24",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Some of the time"),
                            ("2", "Most of the time"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="Do you carry a bottle with you or keep one close at hand?",
                    ),
                ),
                (
                    "q25",
                    models.CharField(
                        choices=[("0", "Never"), ("1", "Once"), ("2", "Several times")],
                        default=None,
                        max_length=50,
                        verbose_name="Have you ever attempted suicide when drinking?",
                    ),
                ),
                (
                    "q26",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes, once"),
                            ("2", "Several times"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="As a result of drinking, have you ever had delirium tremens or DT's (seen, felt, or heard things not really there)?",
                    ),
                ),
                (
                    "q27",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes, once"),
                            ("2", "Yes, several times"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="As a result of drinking have you felt your heart beating rapidly?",
                    ),
                ),
                (
                    "q28",
                    models.CharField(
                        choices=[
                            ("0", "No"),
                            ("1", "Yes, once"),
                            ("2", "Yes, several times"),
                        ],
                        default=None,
                        max_length=50,
                        verbose_name="As a result of drinking have you felt overly hot and sweaty (feverish)?",
                    ),
                ),
                (
                    "q29",
                    models.CharField(
                        choices=[("0", "Yes"), ("1", "No")],
                        default=None,
                        max_length=50,
                        verbose_name="Do you drink during your work day?",
                    ),
                ),
                ("score", models.IntegerField(blank=True, editable=False, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ads",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"get_latest_by": "created",},
        ),
    ]
