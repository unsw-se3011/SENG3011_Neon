from report.models import * 
out = Outbreak.objects.all()
for o in out:
    if len(Outbreak.static(o.id)) < 3:
        o.delete()
