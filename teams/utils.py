from .exceptions import NegativeTitlesError, ImpossibleTitlesError, InvalidYearCupError, TeamNotFoundError
from rest_framework.views import Response, status
from .models import Team


class TeamMethods:
    def find_team(team_id: int) -> Team:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            raise TeamNotFoundError("Team not found")

        return team

    def data_processing(team: dict):
        first_cup_in_dict: str = team["first_cup"][:4]
        first_cup: int = int(first_cup_in_dict)
        titles_in_dict: str = team["titles"]
        titles: int = int(titles_in_dict)

        last_cup: int = 2022

        cup_is_not_on_period: bool = (first_cup - 1930) % 4 != 0

        disputed_cups: int = (last_cup - first_cup) / 4

        if titles < 0:
            raise NegativeTitlesError("titles cannot be negative")

        if first_cup < 1930 or cup_is_not_on_period:
            raise InvalidYearCupError("there was no world cup this year")

        if titles > disputed_cups:
            raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

        return team


class ResponseMethods:
    def generate_response_success(status_code, variant="Not exists"):
        match status_code:
            case 200:
                status_code = status.HTTP_200_OK
            case 201:
                status_code = status.HTTP_201_CREATED
            case 204:
                status_code = status.HTTP_204_NO_CONTENT
                return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(variant, status_code)

    def generate_response_error(status_code, message: str):
        match status_code:
            case 400:
                status_code = status.HTTP_400_BAD_REQUEST
                dict = {"error": message}
            case 404:
                status_code = status.HTTP_404_NOT_FOUND
                dict = {"message": message}
            case 409:
                status_code = status.HTTP_409_CONFLICT
                dict = {"error": message}

        return Response(dict, status=status_code)
