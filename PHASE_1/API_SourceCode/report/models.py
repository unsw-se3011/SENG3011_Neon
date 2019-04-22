from django.urls import reverse 
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.contrib.auth.models import User

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
    img = models.URLField(max_length=1024,blank=True)

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

EVENT_TYPE_MAP = {
    PRESENCE: 'Presence',
    DEATH: 'Death',
    INFECTED: 'Infected',
    HOSPITALISED: 'Hospitalised',
    RECOVERED: 'Recovered',
}


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

    @property
    def event_type_full(self):
        return EVENT_TYPE_MAP[self.e_type]


class Outbreak(models.Model):

    key_term = models.ForeignKey(Disease, on_delete= models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    img = models.URLField(max_length= 1024,blank = True)

    class Meta:
        verbose_name = _("outbreak")
        verbose_name_plural = _("outbreaks")
        # these three must be unique, 
        # otherwise it doesn't make sense 
        unique_together = (
            "key_term",
            "start_date",
            "end_date"
        )

    def get_absolute_url(self):
        return reverse("outbreak_detail", kwargs={"pk": self.pk})
    
    @classmethod
    def static(cls, outbreak_id, event_type = INFECTED):
        # get the outbreak object 
        out = cls.objects.get(pk = outbreak_id)

        # recreate the filter of report event 
        query_set = ReportEvent.objects.filter(
            Q(
                start_date__gte=out.start_date,
                start_date__lte=out.end_date
            ) |
            Q(
                end_date__gte=out.start_date,
                end_date__lte=out.end_date
            ) |
            Q(
                start_date__lte=out.start_date,
                end_date__gte=out.end_date
            )
        )\
        .filter(
            # e_type = event_type
        ).filter(
            Q(report__article__main_text__icontains= out.key_term)|
            Q(report__article__main_text__icontains = out.key_term)|
            Q(report__disease__name__icontains = out.key_term)|
            Q(report__syndrome__name__icontains = out.key_term)
        ).filter(
            # number affect not null filter
            number_affected__isnull=False
        ).order_by('start_date').distinct()

        # organize the data to form the chart 
        day_dict = {} 
        
        return query_set


class Message(models.Model):
    # link to a report 
    report = models.ForeignKey(Report, on_delete = models.CASCADE)
    msg = models.CharField(max_length = 1024)
    user= models.ForeignKey(User, on_delete = models.PROTECT)

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")

    def __str__(self):
        return self.msg

    def get_absolute_url(self):
        return reverse("message_detail", kwargs={"pk": self.pk})

class Bookmark(models.Model):
    """
    Link the bookmarks 
    """
    report = models.ForeignKey(Report, on_delete = models.CASCADE)
    user= models.ForeignKey(User, on_delete = models.PROTECT)


    class Meta:
        verbose_name = _("bookmark")
        verbose_name_plural = _("bookmarks")
        unique_together = ('report', 'user')

    def __str__(self):
        return str(self.user) + " with "+ str(self.report.id)

    def get_absolute_url(self):
        return reverse("bookmark_detail", kwargs={"pk": self.pk})

    @classmethod
    def get_Bookmarked(cls, user):
        return cls.objects.filter(user = user)