from django.db import connection
from django.core.exceptions import ValidationError
from django.conf import settings
from inspect import getframeinfo, stack


def execute(sql):
    ret = False
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
        except Exception as e:
            if settings.DEBUG:
                fl = getframeinfo(stack()[1][0])
                tx = '''<FILE>: {} <LINE>: {} <ERROR>: {} <SQL>: {}'''
                raise ValidationError(tx.format(fl.filename, fl.lineno, str(e), sql))
            else:
                pass
        try:
            columns = [col[0] for col in cursor.description]
            ret = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        except Exception as e:
            try:
                ret = cursor.rowcount
                connection.commit()
            except Exception:
                ret = 0
    return ret
