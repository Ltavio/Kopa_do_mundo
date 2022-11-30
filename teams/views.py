from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict
import ipdb


class TeamViews(APIView):
    def post(self, request: Request) -> Response:
        team = Team.objects.create(**request.data)

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        # ipdb.set_trace()
        list_teams = []
        for team in teams:
            teams_dict = model_to_dict(team)
            list_teams.append(teams_dict)

        return Response(list_teams, status.HTTP_200_OK)


class TeamDetailsViews(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
