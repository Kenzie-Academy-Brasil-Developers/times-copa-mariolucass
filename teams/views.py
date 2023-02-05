from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict
from .models import Team
from .utils import TeamMethods, ResponseMethods


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams_list = []

        teams = Team.objects.all()

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return ResponseMethods.generate_response_success(200, teams_list)

    def post(self, request: Request) -> Response:
        try:
            validated_data: dict = TeamMethods.data_processing(request.data)
        except Exception as e:
            return ResponseMethods.generate_response_error(400, e.message)

        team = Team.objects.create(**validated_data)
        team_dict = model_to_dict(team)

        return ResponseMethods.generate_response_success(201, team_dict)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = TeamMethods.find_team(team_id)
        except Exception as e:
            return ResponseMethods.generate_response_error(404, e.message)

        team_dict = model_to_dict(team)

        return ResponseMethods.generate_response_success(200, team_dict)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = TeamMethods.find_team(team_id)
        except Exception as error:
            return ResponseMethods.generate_response_error(404, error.message)

        for key, value in request.data.items():
            if key != id:
                setattr(team, key, value)

        team.save()
        team_dict = model_to_dict(team)

        return ResponseMethods.generate_response_success(200, team_dict)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = TeamMethods.find_team(team_id)
        except Exception as error:
            return ResponseMethods.generate_response_error(404, error.message)

        team.delete()
        return ResponseMethods.generate_response_success(204)
