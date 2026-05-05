from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Super heroes data
        heroes = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel},
            {'name': 'Captain America', 'email': 'captain@marvel.com', 'team': marvel},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'team': marvel},
            {'name': 'Hulk', 'email': 'hulk@marvel.com', 'team': marvel},
            {'name': 'Black Widow', 'email': 'blackwidow@marvel.com', 'team': marvel},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': dc},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc},
            {'name': 'Flash', 'email': 'flash@dc.com', 'team': dc},
            {'name': 'Aquaman', 'email': 'aquaman@dc.com', 'team': dc},
        ]

        users = []
        for hero in heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                team=hero['team']
            )
            users.append(user)
            hero['team'].members.add(user)

        # Activities
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga']
        for user in users:
            for _ in range(random.randint(5, 10)):
                Activity.objects.create(
                    user=user,
                    activity_type=random.choice(activity_types),
                    duration=random.randint(30, 120),
                    date=datetime.now() - timedelta(days=random.randint(0, 30))
                )

        # Leaderboard
        for user in users:
            Leaderboard.objects.create(
                user=user,
                score=random.randint(100, 1000)
            )

        # Workouts
        workout_names = ['Upper Body', 'Lower Body', 'Cardio Blast', 'Strength Training']
        exercises = [
            'Push-ups: 3 sets of 10',
            'Squats: 3 sets of 15',
            'Bench Press: 3 sets of 8',
            'Deadlifts: 3 sets of 6',
            'Planks: 3 sets of 30s'
        ]
        for user in users:
            for _ in range(random.randint(2, 5)):
                Workout.objects.create(
                    user=user,
                    name=random.choice(workout_names),
                    exercises='\n'.join(random.sample(exercises, 3))
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))