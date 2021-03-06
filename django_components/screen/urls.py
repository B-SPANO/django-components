"""
Components urls

These URL are generated on the fly, by readint the Component table.

These components should exist before django start, because urlpatterns are created when starting the server.
If a new component is added, it will not be serve until the server restarts.
"""
import logging

from django.core.exceptions import ViewDoesNotExist
from django.core.management import color_style
from django.db import OperationalError
from django.utils.translation import ugettext as _

from screen.models import Screen


logger = logging.getLogger("django")
style = color_style()

urlpatterns = []  # pylint: disable=invalid-name

try:
    for screen in Screen.objects.all():
        try:
            urlpatterns.append(screen.url_pattern)
        except ViewDoesNotExist as e:
            logger.info(style.WARNING("{}, please check screen labelled '{}'.".format(e, screen.label)))
except OperationalError as e:
    logger.info(style.WARNING(
        "\n===\n" + str(e) + "\n    > " + _("This can be normal (if the db is not set yet, for instance).")))
