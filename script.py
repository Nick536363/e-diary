from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Subject

def get_pupil_by_name(name: str):
    return Schoolkid.objects.get(full_name__contains=name)


def fix_marks(schoolkid: str):
    pupil = get_pupil_by_name(schoolkid)
    bad_marks = Mark.objects.filter(schoolkid=pupil, points__in=[2,3])
    bad_marks.update(points=5)


def remove_chastisements(schoolkid: str):
    pupil = get_pupil_by_name(schoolkid)
    chasitsements = Chastisement.objects.filter(schoolkid=name)
    chasitsements.delete()