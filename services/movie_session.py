from django.db.models import QuerySet

from db.models import CinemaHall, Movie, MovieSession


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        movie=Movie.objects.get(id=movie_id),
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id)
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = MovieSession.objects.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    updated_movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        updated_movie_session.show_time = show_time
    if movie_id:
        updated_movie_session.movie_id = movie_id
    if cinema_hall_id:
        updated_movie_session.cinema_hall_id = cinema_hall_id
    updated_movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()