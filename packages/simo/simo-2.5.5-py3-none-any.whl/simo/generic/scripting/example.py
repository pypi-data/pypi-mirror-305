import time
import random
from django.utils import timezone
from simo.core.middleware import get_current_instance
from simo.core.models import Component
from simo.users.models import InstanceUser
from simo.generic.scripting.helpers import LocalSun


class Automation:
    REZIMAS_COMPONENT_ID = 130

    def __init__(self):
        self.instance = get_current_instance()
        self.rezimas = Component.objects.get(id=self.REZIMAS_COMPONENT_ID)
        self.sun = LocalSun(self.instance.location)
        self.night_is_on = False

    def check_owner_phones(self, rezimas, instance_users, datetime):
        if not self.night_is_on:
            if not (datetime.hour >= 22 or datetime.hour < 6):
                return

            for iuser in instance_users:
                # skipping users that are not at home
                if not iuser.at_home:
                    continue
                if not iuser.phone_on_charge:
                    # at least one user's phone is not yet on charge
                    return
            self.night_is_on = True
            return 'night'
        else:
            # return new_rezimas diena only if there are still users
            # at home, none of them have their phones on charge
            # and current rezimas is still night
            for iuser in instance_users:
                # skipping users that are not at home
                if not iuser.at_home:
                    continue
                if iuser.phone_on_charge:
                    # at least one user's phone is still on charge
                    return
                else:
                    self.night_is_on = False
            if not self.night_is_on and rezimas.value == 'night':
                return 'day'

    def run(self):
        while True:
            instance_users = InstanceUser.objects.filter(
                is_active=True, role__is_owner=True
            )
            self.rezimas.refresh_from_db()
            new_rezimas = self.check_owner_phones(
                self.rezimas, instance_users, timezone.localtime()
            )
            if new_rezimas:
                self.rezimas.send(new_rezimas)

            # randomize script load
            time.sleep(random.randint(20, 40))


    def test(self):
        pass
