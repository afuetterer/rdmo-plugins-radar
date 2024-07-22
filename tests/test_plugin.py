import pytest

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rdmo.projects.models import Project


def test_settings():
    assert ("radar", _("from RADAR XML"), "rdmo_radar.imports.RadarImport") in settings.PROJECT_IMPORTS


@pytest.mark.django_db
def test_fixtures_are_available():
    num_users = get_user_model().objects.count()
    assert num_users > 0

    num_projects = Project.objects.count()
    assert num_projects > 0
