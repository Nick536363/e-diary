from datacenter.models import Schoolkid, Mark, Chastisement, Lesson


def fix_marks(schoolkid: Schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
    bad_marks.update(points=5)


def remove_chastisements(schoolkid: Schoolkid):
    chasitsements = Chastisement.objects.filter(schoolkid=schoolkid)
    chasitsements.delete()