from datacenter.models import Schoolkid, Mark


def fix_marks(schoolkid: Schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
    bad_marks.update(points=5)    