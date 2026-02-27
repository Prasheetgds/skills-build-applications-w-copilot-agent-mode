
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')

        # Add users to teams
        marvel.members.add(ironman)
        dc.members.add(batman)

        # Create activities
        Activity.objects.create(user=ironman, activity_type='flight', duration=60)
        Activity.objects.create(user=batman, activity_type='training', duration=90)

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=95)

        # Create workouts
        repulsor = Workout.objects.create(name='Repulsor Blast', description='Ironman arm workout')
        batmobile = Workout.objects.create(name='Batmobile Chase', description='Batman cardio workout')
        repulsor.users.add(ironman)
        batmobile.users.add(batman)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
