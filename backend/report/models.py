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
    url = models.URLField(primary_key=True)
    headline = models.CharField(max_length=512, default='')
    publish = models.DateTimeField()
    # publish fuzz field
    p_fuzz = models.CharField(
        max_length=1, choices=fuzz_choice)
    main_text = models.TextField()


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
    lat = models.DecimalField(max_digits=24, decimal_places=20)
    lng = models.DecimalField(max_digits=24, decimal_places=20)


class Report(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    disease = models.ManyToManyField(Disease, blank=True)
    syndrome = models.ManyToManyField(Syndrome, blank=True)
    # this may need to change
    comment = models.TextField(blank=True)


class ReportEvent(models.Model):
    report_type = models.CharField(max_length=200)
    # start of the date time
    start_date = models.DateTimeField()
    sd_fuzz = models.CharField(max_length=1, choices=fuzz_choice)
    # end of date time
    end_date = models.DateTimeField()
    ed_fuzz = models.CharField(max_length=1, choices=fuzz_choice)
    number_effecet = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, models.PROTECT)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
