from django.db import models

YEAR = "Y"
MONTH = "M"
DAY = "D"
HOUR = "H"
MINUTE = "I"
SECOND = "S"
ACCURATE = "A"


fuzz_choice = (
    (YEAR, "Year"),
    (MONTH, 'Month'),
    (DAY, 'Day'),
    (HOUR, 'Hour'),
    (MINUTE, 'Minute'),
    (SECOND, 'Second'),
    (ACCURATE, 'Accurate'),
)


class Article(models.Model):
    url = models.URLField(unique=True)
    headline = models.CharField(max_length=512, default='')
    date_of_publication = models.DateTimeField()
    # publish fuzz field
    p_fuzz = models.CharField(
        max_length=1, choices=fuzz_choice)
    main_text = models.TextField()
    img = models.URLField(blank=True)

    def __str__(self):
        return self.headline


class Syndrome(models.Model):
    name = models.CharField(max_length=200, primary_key=True)


class Disease(models.Model):
    """
    Record the disease name, and it's syndrom
    """

    name = models.CharField(max_length=200, primary_key=True)
    syndromes = models.ManyToManyField(Syndrome, blank=True)

    def __str__(self):
        # to support the disease name shown
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=512)
    continent = models.CharField(max_length=512, blank=True, default="")
    country = models.CharField(max_length=512, blank=True, default="")
    state = models.CharField(max_length=512, blank=True, default="")
    city = models.CharField(max_length=512, blank=True, default="")
    lat = models.DecimalField(
        max_digits=24, decimal_places=20, null=True, blank=True)
    lng = models.DecimalField(
        max_digits=24, decimal_places=20, null=True, blank=True)


class Report(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    disease = models.ManyToManyField(Disease, blank=True)
    syndrome = models.ManyToManyField(Syndrome, blank=True)
    # this may need to change
    comment = models.TextField(blank=True)


PRESENCE = "P"
DEATH = "D"
INFECTED = "I"
HOSPITALISED = "H"
RECOVERED = "R"

EVENT_TYPE_CHOICE = (
    (PRESENCE, 'Presence'),
    (DEATH, 'Death'),
    (INFECTED, 'Infected'),
    (HOSPITALISED, 'Hospitalised'),
    (RECOVERED, 'Recovered'),
)


class ReportEvent(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    e_type = models.CharField(max_length=1, choices=EVENT_TYPE_CHOICE)
    # start of the date time
    start_date = models.DateTimeField()
    sd_fuzz = models.CharField(max_length=1, choices=fuzz_choice)
    # end of date time
    end_date = models.DateTimeField()
    ed_fuzz = models.CharField(max_length=1, choices=fuzz_choice)
    number_affected = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(
        Location, models.PROTECT, blank=True, null=True)
