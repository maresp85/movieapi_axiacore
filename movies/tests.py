from django.test import TestCase

from .models import Movie
from .forms import MovieForm

class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(overview="Battle-hardened O’Hara leads a lively mercenary team of soldiers on a daring mission: rescue hostages from their captors in remote Africa. But as the mission goes awry and the team is stranded, O’Hara’s squad must face a bloody, brutal encounter with a gang of rebels.",
                            poster_path="/uOw5JD8IlD546feZ6oxbIjvN66P.jpg",
                            original_title="Rogue",
                            original_language="en",
                            title="Rogue",
                            release_date="2020-08-20",
                            rating=4,
                            genre_id=28)
