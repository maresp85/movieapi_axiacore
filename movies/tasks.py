from background_task import background
from .models import Genre, Movie
import coreapi


@background(schedule=60)
def call_api():
    print("CAll API")
    call_movieapi()

def call_movieapi():
    try:
        token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MTExMmY2Yzk3OTExZTFhOWU5Yjg3ZWU5NDZlNzIyNSIsInN1YiI6IjVmNTNhMDVjODQ4ZWI5MDAzNzVlMzVjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KSAnnKlPSy6RF8VjJCQj8qK8qOEsLCQKzYf9RjU2FCY' # don't put the word 'Token' in front.
        auth = coreapi.auth.TokenAuthentication(token=token)
        client = coreapi.Client(auth=auth)
        popularmovies = client.get('https://api.themoviedb.org/3/movie/popular/')
        for i in popularmovies['results']:
            movie = Movie.objects.create(overview= i['original_title'],
                                         poster_path= i['poster_path'],
                                         original_title= i['original_title'],
                                         original_language= i['original_language'],
                                         title= i['title'],
                                         release_date= i['release_date'])
            for j in i['genre_ids']:
                genre = Genre.objects.get(pk=j)
                movie.genre_id.add(genre)
    except Exception as error:
        logging.debug(error)
