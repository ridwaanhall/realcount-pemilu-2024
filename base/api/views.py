import requests
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .Ridwaanhall import DATABASE_API, DATABASE

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/names/',
        'GET /api/sengketa/',
        'GET /api/wilayah/<str:wilayah_tingkat2>/',
        'GET /api/wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>',
        'GET /api/wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>/<str:wilayah_tingkat4>',
        'GET /api/wilayah/<str:wilayah_tingkat2>/<str:wilayah_tingkat3>/<str:wilayah_tingkat4>/<str:wilayah_tingkat5>',
        'GET /api/votes/',
        'GET /api/votes/<str:votes_tingkat2>',
        'GET /api/votes/<str:votes_tingkat2>/<str:votes_tingkat3>',
        'GET /api/votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>',
        'GET /api/votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>/<str:votes_tingkat5>',
        'GET /api/votes/<str:votes_tingkat2>/<str:votes_tingkat3>/<str:votes_tingkat4>/<str:votes_tingkat5>/<str:votes_tingkat6>',
        'GET /api/level-api/<str:area_code_lv2>/',
        'GET /api/level-api/<str:area_code_lv2>/<str:area_code_lv3>/',
        'GET /api/level-api/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/',
        'GET /api/level-api/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/<str:area_code_lv5>/',
        'GET /api/level-api/<str:area_code_lv2>/<str:area_code_lv3>/<str:area_code_lv4>/<str:area_code_lv5>/<str:area_code_lv6>/',
        
    ]
    return Response(routes)


class Names(APIView):
    def get(self, request, format=None):
        url = DATABASE + 'pemilu/ppwp.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Sengketa(APIView):
    def get(self, request, format=None):
        url = DATABASE + 'pemilu/ds/ppwp.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WilayahTingkat2(APIView):
    def get(self, request, wilayah_tingkat2, format=None):
        url = DATABASE + f'wilayah/pemilu/ppwp/{wilayah_tingkat2}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                

class WilayahTingkat3(APIView):
    def get(self, request, wilayah_tingkat2, wilayah_tingkat3, format=None):
        url = DATABASE + f'wilayah/pemilu/ppwp/{wilayah_tingkat2}/{wilayah_tingkat3}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WilayahTingkat4(APIView):
    def get(self, request, wilayah_tingkat2, wilayah_tingkat3, wilayah_tingkat4, format=None):
        url = DATABASE + f'wilayah/pemilu/ppwp/{wilayah_tingkat2}/{wilayah_tingkat3}/{wilayah_tingkat4}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WilayahTingkat5(APIView):
    def get(self, request, wilayah_tingkat2, wilayah_tingkat3, wilayah_tingkat4, wilayah_tingkat5, format=None):
        url = DATABASE + f'wilayah/pemilu/ppwp/{wilayah_tingkat2}/{wilayah_tingkat3}/{wilayah_tingkat4}/{wilayah_tingkat5}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VotesTingkat1(APIView):
    def get(self, request, format=None):
        url = DATABASE + 'pemilu/hhcw/ppwp.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat2(APIView):
    def get(self, request, votes_tingkat2, format=None):
        url = DATABASE + f'pemilu/hhcw/ppwp/{votes_tingkat2}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat3(APIView):
    def get(self, request, votes_tingkat2, votes_tingkat3, format=None):
        url = DATABASE + f'pemilu/hhcw/ppwp/{votes_tingkat2}/{votes_tingkat3}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat4(APIView):
    def get(self, request, votes_tingkat2, votes_tingkat3, votes_tingkat4, format=None):
        url = DATABASE + f'pemilu/hhcw/ppwp/{votes_tingkat2}/{votes_tingkat3}/{votes_tingkat4}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat5(APIView):
    def get(self, request, votes_tingkat2, votes_tingkat3, votes_tingkat4, votes_tingkat5, format=None):
        url = DATABASE + f'pemilu/hhcw/ppwp/{votes_tingkat2}/{votes_tingkat3}/{votes_tingkat4}/{votes_tingkat5}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat6(APIView):
    def get(self, request, votes_tingkat2, votes_tingkat3, votes_tingkat4, votes_tingkat5, votes_tingkat6, format=None):
        url = DATABASE + f'pemilu/hhcw/ppwp/{votes_tingkat2}/{votes_tingkat3}/{votes_tingkat4}/{votes_tingkat5}/{votes_tingkat6}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class Level1API(APIView):
    def get(self, request, format=None):
        names_url = DATABASE_API+ "api/names/"
        votes_lv1_url = DATABASE_API+ "api/votes/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"

        names_response = requests.get(names_url)
        names_data = names_response.json()

        votes_response = requests.get(votes_lv1_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_lv1_url)
        wilayah_data = wilayah_response.json()

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        
        total_data = {}
        for key, value in names_data.items():
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": votes_data["chart"][key],
                "votes_formatted": "{:,}".format(votes_data["chart"][key]),
                "percentage": votes_data["chart"][key] / total_votes * 100,
                "percentage_formatted": "{:.2f}%".format(votes_data["chart"][key] / total_votes * 100),
            }
            

        last_update_timestamp = datetime.strptime(votes_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        total_child_data = {}
        for key, value in votes_data["table"].items():
            area_code_lv2 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            total_child_data[key] = {
                "area_code_lv2": area_code_lv2,
                "area_id": area_id,
                "area_name": area_name,
                "area_progress": value["persen"],
                "area_progress_formatted": "{:.2f}%".format(value["persen"]),
                "level": level,
                "100025": value["100025"],
                "100025_formatted": "{:,}".format(value["100025"]),
                "100025_percentage": (value["100025"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100025_percentage_formatted": "{:.2f}%".format((value["100025"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "100026": value["100026"],
                "100026_formatted": "{:,}".format(value["100026"]),
                "100026_percentage": (value["100026"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100026_percentage_formatted": "{:.2f}%".format((value["100026"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "100027": value["100027"],
                "100027_formatted": "{:,}".format(value["100027"]),
                "100027_percentage": (value["100027"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100027_percentage_formatted": "{:.2f}%".format((value["100027"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "total_area_votes": value["100025"] + value["100026"] + value["100027"],
                "total_area_votes_formatted": "{:,}".format(value["100025"] + value["100026"] + value["100027"])
            }
            
        total_progress_tps = votes_data["progres"]["total"]
        progress_tps = votes_data["progres"]["progres"]

        progress_data = {
            "total_tps": total_progress_tps,
            "total_tps_formatted": "{:,}".format(total_progress_tps),
            "progres_tps": progress_tps,
            "progres_tps_formatted": "{:,}".format(progress_tps),
            "percentage_tps": (progress_tps / total_progress_tps) * 100,
            "percentage_tps_formatted": "{:.2f}%".format((progress_tps / total_progress_tps) * 100),
        }
        
        highest_votes = max(values for key, values in votes_data["chart"].items() if key != "persen")
        
        for key, values in votes_data["chart"].items():
            if values == highest_votes:
                whose_highest = key
                if key == "100025":
                    whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                elif key == "100026":
                    whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                elif key == "100027":
                    whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                else:
                    whose_highest = key
        
        percentage_tps = (progress_tps / total_progress_tps) * 100
        
        votes_data_100025 = votes_data["chart"]["100025"]
        votes_data_100026 = votes_data["chart"]["100026"]
        votes_data_100027 = votes_data["chart"]["100027"]
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
        percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
        percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        
        html_progres_tps = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_tps }%' aria-valuenow='{ percentage_tps }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"
        
        html_progres = {
            "html_progres_tps": html_progres_tps,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        response_data = {
            "last_update": last_update_formatted,
            "level_pemilu": "National",
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "html_progres": html_progres,
            "progress_data": progress_data,
            "total_data": total_data,
            "total_child_data": total_child_data
        }

        return Response(response_data)
    
    
class Level2API(APIView):
    def get(self, request, area_code_lv2, format=None):
        names_url = DATABASE_API+ "api/names/"
        votes_lv1_url = DATABASE_API+ "api/votes/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"
        votes_lv2_url = DATABASE_API+ f"api/votes/{area_code_lv2}/"
        wilayah_lv2_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/"


        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()

        votes_response = requests.get(votes_lv2_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_lv2_url)
        wilayah_data = wilayah_response.json()

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        
        total_data = {}
        for key, value in names_data.items():
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": votes_data["chart"][key],
                "votes_formatted": "{:,}".format(votes_data["chart"][key]),
                "percentage": votes_data["chart"][key] / total_votes * 100,
                "percentage_formatted": "{:.2f}%".format(votes_data["chart"][key] / total_votes * 100),
            }
            

        last_update_timestamp = datetime.strptime(votes_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        total_child_data = {}
        for key, value in votes_data["table"].items():
            area_code_lv3 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            
            total_votes = value.get("100025", 0) + value.get("100026", 0) + value.get("100027", 0)
            
            if total_votes != 0:
                total_child_data[key] = {
                    "code_lv2": area_code_lv2,
                    "area_code_lv3": area_code_lv3,
                    "area_id": area_id,
                    "area_name": area_name,
                    "area_progress": value.get("persen", 0),
                    "area_progress_formatted": "{:.2f}%".format(value.get("persen", 0)),
                    "level": level,
                    "100025": value.get("100025", 0),
                    "100025_formatted": "{:,}".format(value.get("100025", 0)),
                    "100025_percentage": (value.get("100025", 0) / total_votes) * 100,
                    "100025_percentage_formatted": "{:.2f}%".format((value.get("100025", 0) / total_votes) * 100),
                    "100026": value.get("100026", 0),
                    "100026_formatted": "{:,}".format(value.get("100026", 0)),
                    "100026_percentage": (value.get("100026", 0) / total_votes) * 100,
                    "100026_percentage_formatted": "{:.2f}%".format((value.get("100026", 0) / total_votes) * 100),
                    "100027": value.get("100027", 0),
                    "100027_formatted": "{:,}".format(value.get("100027", 0)),
                    "100027_percentage": (value.get("100027", 0) / total_votes) * 100,
                    "100027_percentage_formatted": "{:.2f}%".format((value.get("100027", 0) / total_votes) * 100),
                    "total_area_votes": total_votes,
                    "total_area_votes_formatted": "{:,}".format(total_votes)
                }
            else:
                total_child_data[key] = {
                    "code_lv2": area_code_lv2,
                    "area_code_lv3": area_code_lv3,
                    "area_id": area_id,
                    "area_name": area_name,
                    "area_progress": value.get("persen", 0),
                    "area_progress_formatted": "{:.2f}%".format(value.get("persen", 0)),
                    "level": level,
                    "100025": value.get("100025", 0),
                    "100025_formatted": "{:,}".format(value.get("100025", 0)),
                    "100025_percentage": 0,
                    "100025_percentage_formatted": "0.00%",
                    "100026": value.get("100026", 0),
                    "100026_formatted": "{:,}".format(value.get("100026", 0)),
                    "100026_percentage": 0,
                    "100026_percentage_formatted": "0.00%",
                    "100027": value.get("100027", 0),
                    "100027_formatted": "{:,}".format(value.get("100027", 0)),
                    "100027_percentage": 0,
                    "100027_percentage_formatted": "0.00%",
                    "total_area_votes": 0,
                    "total_area_votes_formatted": "0"
                }

        total_progress_tps = votes_data["progres"]["total"]
        progress_tps = votes_data["progres"]["progres"]

        progress_data = {
            "total_tps": total_progress_tps,
            "total_tps_formatted": "{:,}".format(total_progress_tps),
            "progres_tps": progress_tps,
            "progres_tps_formatted": "{:,}".format(progress_tps),
            "percentage_tps": (progress_tps / total_progress_tps) * 100,
            "percentage_tps_formatted": "{:.2f}%".format((progress_tps / total_progress_tps) * 100),
        }
        
        highest_votes = max(values for key, values in votes_data["chart"].items() if key != "persen")
        
        for key, values in votes_data["chart"].items():
            if values == highest_votes:
                whose_highest = key
                if key == "100025":
                    whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                elif key == "100026":
                    whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                elif key == "100027":
                    whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                else:
                    whose_highest = key
        
        percentage_tps = (progress_tps / total_progress_tps) * 100
        
        votes_data_100025 = votes_data["chart"]["100025"]
        votes_data_100026 = votes_data["chart"]["100026"]
        votes_data_100027 = votes_data["chart"]["100027"]
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
        percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
        percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        
        html_progres_tps = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_tps }%' aria-valuenow='{ percentage_tps }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"
        
        html_progres = {
            "html_progres_tps": html_progres_tps,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break
        
        response_data = {
            "last_update": last_update_formatted,
            "area_name_lv2": area_name_lv2,
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "html_progres": html_progres,
            "progress_data": progress_data,
            "total_data": total_data,
            "total_child_data": total_child_data
        }

        return Response(response_data)
    
    
class Level3API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, format=None):
        names_url = DATABASE_API+ "api/names/"
        votes_lv1_url = DATABASE_API+ "api/votes/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"
        votes_lv2_url = DATABASE_API+ f"api/votes/{area_code_lv2}/"
        wilayah_lv2_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/"
        votes_lv3_url = DATABASE_API+ f"api/votes/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv3_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        
        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()
        
        wilayah_lv2_response = requests.get(wilayah_lv2_url)
        wilayah_lv2_data = wilayah_lv2_response.json()

        votes_response = requests.get(votes_lv3_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_lv3_url)
        wilayah_data = wilayah_response.json()

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
                
        total_data = {}
        for key, value in names_data.items():
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": votes_data["chart"][key],
                "votes_formatted": "{:,}".format(votes_data["chart"][key]),
                "percentage": votes_data["chart"][key] / total_votes * 100,
                "percentage_formatted": "{:.2f}%".format(votes_data["chart"][key] / total_votes * 100),
            }

        last_update_timestamp = datetime.strptime(votes_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        total_child_data = {}
        for key, value in votes_data["table"].items():
            area_code_lv4 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
            
            total_child_data[key] = {
                "code_lv2": area_code_lv2,
                "area_code_lv3": area_code_lv3,
                "area_code_lv4": area_code_lv4,
                "area_id": area_id,
                "area_name": area_name,
                "area_progress": value.get("persen", 0),
                "area_progress_formatted": "{:.2f}%".format(value.get("persen", 0)),
                "level": level,
                "100025": value.get("100025", 0),
                "100025_formatted": "{:,}".format(value.get("100025", 0)),
                "100025_percentage": (value.get("100025", 0) / total_votes) * 100 if total_votes != 0 else 0,
                "100025_percentage_formatted": "{:.2f}%".format((value.get("100025", 0) / total_votes) * 100) if total_votes != 0 else "0.00%",
                "100026": value.get("100026", 0),
                "100026_formatted": "{:,}".format(value.get("100026", 0)),
                "100026_percentage": (value.get("100026", 0) / total_votes) * 100 if total_votes != 0 else 0,
                "100026_percentage_formatted": "{:.2f}%".format((value.get("100026", 0) / total_votes) * 100) if total_votes != 0 else "0.00%",
                "100027": value.get("100027", 0),
                "100027_formatted": "{:,}".format(value.get("100027", 0)),
                "100027_percentage": (value.get("100027", 0) / total_votes) * 100 if total_votes != 0 else 0,
                "100027_percentage_formatted": "{:.2f}%".format((value.get("100027", 0) / total_votes) * 100) if total_votes != 0 else "0.00%",
                "total_area_votes": total_votes,
                "total_area_votes_formatted": "{:,}".format(total_votes)
            }
            
        total_progress_tps = votes_data["progres"]["total"]
        progress_tps = votes_data["progres"]["progres"]

        progress_data = {
            "total_tps": total_progress_tps,
            "total_tps_formatted": "{:,}".format(total_progress_tps),
            "progres_tps": progress_tps,
            "progres_tps_formatted": "{:,}".format(progress_tps),
            "percentage_tps": (progress_tps / total_progress_tps) * 100,
            "percentage_tps_formatted": "{:.2f}%".format((progress_tps / total_progress_tps) * 100),
        }
        
        highest_votes = max(values for key, values in votes_data["chart"].items() if key != "persen")
        
        for key, values in votes_data["chart"].items():
            if values == highest_votes:
                whose_highest = key
                if key == "100025":
                    whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                elif key == "100026":
                    whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                elif key == "100027":
                    whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                else:
                    whose_highest = key
        
        percentage_tps = (progress_tps / total_progress_tps) * 100
        
        votes_data_100025 = votes_data["chart"]["100025"]
        votes_data_100026 = votes_data["chart"]["100026"]
        votes_data_100027 = votes_data["chart"]["100027"]
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
        percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
        percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        
        html_progres_tps = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_tps }%' aria-valuenow='{ percentage_tps }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"
        
        html_progres = {
            "html_progres_tps": html_progres_tps,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break

        area_name_lv3 = None
        for item in wilayah_lv2_data:
            if item["kode"] == area_code_lv3:
                area_name_lv3 = item["nama"]
                break

        response_data = {
            "last_update": last_update_formatted,
            "area_code_lv2": area_code_lv2,
            "area_name_lv2": area_name_lv2,
            "area_code_lv3": area_code_lv3,
            "area_name_lv3": area_name_lv3,
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "html_progres": html_progres,
            "progress_data": progress_data,
            "total_data": total_data,
            "total_child_data": total_child_data
        }

        return Response(response_data)
    
    
class Level4API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, area_code_lv4, format=None):
        names_url = DATABASE_API+ "api/names/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"
        wilayah_lv2_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/"
        wilayah_lv3_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv4_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        votes_lv4_url = DATABASE_API+ f"api/votes/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        
        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()
        
        wilayah_lv2_response = requests.get(wilayah_lv2_url)
        wilayah_lv2_data = wilayah_lv2_response.json()
        
        wilayah_lv3_response = requests.get(wilayah_lv3_url)
        wilayah_lv3_data = wilayah_lv3_response.json()

        votes_response = requests.get(votes_lv4_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_lv4_url)
        wilayah_data = wilayah_response.json()

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen") if votes_data["chart"] is not None else 0
        
        total_data = {}
        for key, value in names_data.items():
            votes = votes_data["chart"][key] if votes_data["chart"] is not None and key in votes_data["chart"] else 0
            percentage = votes / total_votes * 100 if total_votes != 0 else 0
            
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": votes,
                "votes_formatted": "{:,}".format(votes),
                "percentage": percentage,
                "percentage_formatted": "{:.2f}%".format(percentage),
            }
            

        last_update_timestamp = datetime.strptime(votes_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        total_child_data = {}
        for key, value in votes_data["table"].items():
            area_code_lv5 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            
            area_progress = value.get("persen", 0.0)
            
            total_votes_denominator = value.get("100025", 0) + value.get("100026", 0) + value.get("100027", 0)

            if total_votes_denominator != 0:
                total_child_data[key] = {
                    "code_lv2": area_code_lv2,
                    "area_code_lv3": area_code_lv3,
                    "area_code_lv4": area_code_lv4,
                    "area_code_lv5": area_code_lv5,
                    "area_id": area_id,
                    "area_name": area_name,
                    "area_progress": area_progress,
                    "area_progress_formatted": "{:.2f}%".format(area_progress),
                    "level": level,
                    "100025": value.get("100025", 0),
                    "100025_formatted": "{:,}".format(value.get("100025", 0)),
                    "100025_percentage": (value.get("100025", 0) / total_votes_denominator) * 100,
                    "100025_percentage_formatted": "{:.2f}%".format((value.get("100025", 0) / total_votes_denominator) * 100),
                    "100026": value.get("100026", 0),
                    "100026_formatted": "{:,}".format(value.get("100026", 0)),
                    "100026_percentage": (value.get("100026", 0) / total_votes_denominator) * 100,
                    "100026_percentage_formatted": "{:.2f}%".format((value.get("100026", 0) / total_votes_denominator) * 100),
                    "100027": value.get("100027", 0),
                    "100027_formatted": "{:,}".format(value.get("100027", 0)),
                    "100027_percentage": (value.get("100027", 0) / total_votes_denominator) * 100,
                    "100027_percentage_formatted": "{:.2f}%".format((value.get("100027", 0) / total_votes_denominator) * 100),
                    "total_area_votes": total_votes_denominator,
                    "total_area_votes_formatted": "{:,}".format(total_votes_denominator)
                }
            else:
                total_child_data[key] = {
                    "code_lv2": area_code_lv2,
                    "area_code_lv3": area_code_lv3,
                    "area_code_lv4": area_code_lv4,
                    "area_code_lv5": area_code_lv5,
                    "area_id": area_id,
                    "area_name": area_name,
                    "area_progress": area_progress,
                    "area_progress_formatted": "{:.2f}%".format(area_progress),
                    "level": level,
                    "100025": value.get("100025", 0),
                    "100025_formatted": "{:,}".format(value.get("100025", 0)),
                    "100025_percentage": 0,
                    "100025_percentage_formatted": "0.00%",
                    "100026": value.get("100026", 0),
                    "100026_formatted": "{:,}".format(value.get("100026", 0)),
                    "100026_percentage": 0,
                    "100026_percentage_formatted": "0.00%",
                    "100027": value.get("100027", 0),
                    "100027_formatted": "{:,}".format(value.get("100027", 0)),
                    "100027_percentage": 0,
                    "100027_percentage_formatted": "0.00%",
                    "total_area_votes": 0,
                    "total_area_votes_formatted": "0"
                }
            
        total_progress_tps = votes_data["progres"]["total"]
        progress_tps = votes_data["progres"]["progres"]

        if total_progress_tps is not None:
            progress_data = {
                "total_tps": total_progress_tps,
                "total_tps_formatted": "{:,}".format(total_progress_tps),
                "progres_tps": progress_tps,
                "progres_tps_formatted": "{:,}".format(progress_tps),
                "percentage_tps": (progress_tps / total_progress_tps) * 100,
                "percentage_tps_formatted": "{:.2f}%".format((progress_tps / total_progress_tps) * 100),
            }
        else:
            progress_data = {
                "total_tps": 0,
                "total_tps_formatted": "0",
                "progres_tps": progress_tps,
                "progres_tps_formatted": "0",
                "percentage_tps": 0,
                "percentage_tps_formatted": "0.00%",
            }
        
        if votes_data["chart"] is not None:
            highest_votes = max(values for key, values in votes_data["chart"].items() if key != "persen")
        else:
            highest_votes = 0

        if votes_data["chart"] is not None:
            for key, values in votes_data["chart"].items():
                if values == highest_votes:
                    whose_highest = key
                    if key == "100025":
                        whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                    elif key == "100026":
                        whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                    elif key == "100027":
                        whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                    else:
                        whose_highest = key
        else:
            whose_highest = None

        
        if total_progress_tps is not None and progress_tps is not None:
            percentage_tps = (progress_tps / total_progress_tps) * 100
        else:
            percentage_tps = 0
        
        if votes_data["chart"] is not None:
            votes_data_100025 = votes_data["chart"].get("100025")
            votes_data_100026 = votes_data["chart"].get("100026")
            votes_data_100027 = votes_data["chart"].get("100027")
        else:
            votes_data_100025 = 0
            votes_data_100026 = 0
            votes_data_100027 = 0
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        if total_votes_data != 0:
            percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
            percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
            percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        else:
            percentage_votes_data_100025 = 0
            percentage_votes_data_100026 = 0
            percentage_votes_data_100027 = 0
        
        html_progres_tps = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_tps }%' aria-valuenow='{ percentage_tps }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"
        
        html_progres = {
            "html_progres_tps": html_progres_tps,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break

        area_name_lv3 = None
        for item in wilayah_lv2_data:
            if item["kode"] == area_code_lv3:
                area_name_lv3 = item["nama"]
                break
            
        area_name_lv4 = None
        for item in wilayah_lv3_data:
            if item["kode"] == area_code_lv4:
                area_name_lv4 = item["nama"]
                break

        response_data = {
            "last_update": last_update_formatted,
            "area_code_lv2": area_code_lv2,
            "area_name_lv2": area_name_lv2,
            "area_code_lv3": area_code_lv3,
            "area_name_lv3": area_name_lv3,
            "area_code_lv4": area_code_lv4,
            "area_name_lv4": area_name_lv4,
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "html_progres": html_progres,
            "progress_data": progress_data,
            "total_data": total_data,
            "total_child_data": total_child_data
        }

        return Response(response_data)
    
    
class Level5API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, area_code_lv4, area_code_lv5, format=None):
        names_url = DATABASE_API+ "api/names/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"
        wilayah_lv2_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/"
        wilayah_lv3_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv4_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        wilayah_lv5_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/"
        votes_lv5_url = DATABASE_API+ f"api/votes/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/"
        
        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()
        
        wilayah_lv2_response = requests.get(wilayah_lv2_url)
        wilayah_lv2_data = wilayah_lv2_response.json()
        
        wilayah_lv3_response = requests.get(wilayah_lv3_url)
        wilayah_lv3_data = wilayah_lv3_response.json()
        
        wilayah_lv4_response = requests.get(wilayah_lv4_url)
        wilayah_lv4_data = wilayah_lv4_response.json()

        votes_response = requests.get(votes_lv5_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_lv5_url)
        wilayah_data = wilayah_response.json()

        if votes_data["chart"] is not None:
            total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        else:
            total_votes = 0

        
        total_data = {}
        for key, value in names_data.items():
            votes = votes_data["chart"][key] if votes_data["chart"] is not None and key in votes_data["chart"] else 0
            percentage = votes / total_votes * 100 if total_votes != 0 else 0
            
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": votes,
                "votes_formatted": "{:,}".format(votes),
                "percentage": percentage,
                "percentage_formatted": "{:.2f}%".format(percentage),
            }
            

        last_update_timestamp = datetime.strptime(votes_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        total_child_data = {}
        for key, value in votes_data["table"].items():
            area_code_lv6 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)

            votes_100025 = value.get("100025", 0)
            votes_100026 = value.get("100026", 0)
            votes_100027 = value.get("100027", 0)

            total_child_data[key] = {
                "code_lv2": area_code_lv2,
                "area_code_lv3": area_code_lv3,
                "area_code_lv4": area_code_lv4,
                "area_code_lv5": area_code_lv5,
                "area_code_lv6": area_code_lv6,
                "area_id": area_id,
                "area_name": area_name,
                "area_progress": value["persen"],
                "area_progress_formatted": "{:.2f}%".format(value["persen"]),
                "level": level,
                "100025": votes_100025,
                "100025_formatted": "{:,}".format(votes_100025),
                "100025_percentage": (votes_100025 / (votes_100025 + votes_100026 + votes_100027)) * 100 if (votes_100025 + votes_100026 + votes_100027) != 0 else 0,
                "100025_percentage_formatted": "{:.2f}%".format((votes_100025 / (votes_100025 + votes_100026 + votes_100027)) * 100) if (votes_100025 + votes_100026 + votes_100027) != 0 else 0,
                "100026": votes_100026,
                "100026_formatted": "{:,}".format(votes_100026),
                "100026_percentage": (votes_100026 / (votes_100025 + votes_100026 + votes_100027)) * 100 if (votes_100025 + votes_100026 + votes_100027) != 0 else 0,
                "100026_percentage_formatted": "{:.2f}%".format((votes_100026 / (votes_100025 + votes_100026 + votes_100027)) * 100) if (votes_100025 + votes_100026 + votes_100027) != 0 else 0,
                "100027": votes_100027,
                "100027_formatted": "{:,}".format(votes_100027),
                "100027_percentage": (votes_100027 / (votes_100025 + votes_100026 + votes_100027)) * 100 if (votes_100025 + votes_100026 + votes_100027) != 0 else 0,
                "100027_percentage_formatted": "{:.2f}%".format((votes_100027 / (votes_100025 + votes_100026 + votes_100027)) * 100) if (votes_100025 + votes_100026 + votes_100027) != 0 else 0,
                "total_area_votes": votes_100025 + votes_100026 + votes_100027,
                "total_area_votes_formatted": "{:,}".format(votes_100025 + votes_100026 + votes_100027)
            }
            
        total_progress_tps = votes_data["progres"]["total"]
        progress_tps = votes_data["progres"]["progres"]

        if total_progress_tps is not None:
            progress_data = {
                "total_tps": total_progress_tps,
                "total_tps_formatted": "{:,}".format(total_progress_tps),
                "progres_tps": progress_tps,
                "progres_tps_formatted": "{:,}".format(progress_tps),
                "percentage_tps": (progress_tps / total_progress_tps) * 100,
                "percentage_tps_formatted": "{:.2f}%".format((progress_tps / total_progress_tps) * 100),
            }
        else:
            progress_data = {
                "total_tps": 0,
                "total_tps_formatted": "0",
                "progres_tps": progress_tps,
                "progres_tps_formatted": "0",
                "percentage_tps": 0,
                "percentage_tps_formatted": "0.00%",
            }
        
        if votes_data["chart"] is not None:
            highest_votes = max(values for key, values in votes_data["chart"].items() if key != "persen")
        else:
            highest_votes = 0

        if votes_data["chart"] is not None:
            for key, values in votes_data["chart"].items():
                if values == highest_votes:
                    whose_highest = key
                    if key == "100025":
                        whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                    elif key == "100026":
                        whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                    elif key == "100027":
                        whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                    else:
                        whose_highest = key
        else:
            whose_highest = None

        
        if total_progress_tps is not None and progress_tps is not None:
            percentage_tps = (progress_tps / total_progress_tps) * 100
        else:
            percentage_tps = 0
        
        if votes_data["chart"] is not None:
            votes_data_100025 = votes_data["chart"].get("100025")
            votes_data_100026 = votes_data["chart"].get("100026")
            votes_data_100027 = votes_data["chart"].get("100027")
        else:
            votes_data_100025 = 0
            votes_data_100026 = 0
            votes_data_100027 = 0
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        if total_votes_data != 0:
            percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
            percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
            percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        else:
            percentage_votes_data_100025 = 0
            percentage_votes_data_100026 = 0
            percentage_votes_data_100027 = 0
        
        html_progres_tps = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_tps }%' aria-valuenow='{ percentage_tps }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"
        
        html_progres = {
            "html_progres_tps": html_progres_tps,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break

        area_name_lv3 = None
        for item in wilayah_lv2_data:
            if item["kode"] == area_code_lv3:
                area_name_lv3 = item["nama"]
                break
            
        area_name_lv4 = None
        for item in wilayah_lv3_data:
            if item["kode"] == area_code_lv4:
                area_name_lv4 = item["nama"]
                break
        
        area_name_lv5 = None
        for item in wilayah_lv4_data:
            if item["kode"] == area_code_lv5:
                area_name_lv5 = item["nama"]
                break
            
        area_name_lv6 = None
        for item in wilayah_data:
            if item["kode"] == area_code_lv6:
                area_name_lv6 = item["nama"]
                break

        response_data = {
            "last_update": last_update_formatted,
            "area_code_lv2": area_code_lv2,
            "area_name_lv2": area_name_lv2,
            "area_code_lv3": area_code_lv3,
            "area_name_lv3": area_name_lv3,
            "area_code_lv4": area_code_lv4,
            "area_name_lv4": area_name_lv4,
            "area_code_lv5": area_code_lv5,
            "area_name_lv5": area_name_lv5,
            "area_code_lv6": area_code_lv6,
            "area_name_lv6": area_name_lv6,
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "html_progres": html_progres,
            "progress_data": progress_data,
            "total_data": total_data,
            "total_child_data": total_child_data
        }

        return Response(response_data)
    
    
class Level6API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, area_code_lv4, area_code_lv5, area_code_lv6, format=None):
        names_url = DATABASE_API+ "api/names/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"
        wilayah_lv2_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/"
        wilayah_lv3_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv4_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        wilayah_lv5_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/"
        votes_lv6_url = DATABASE_API+ f"api/votes/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/{area_code_lv6}"
        
        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()
        
        wilayah_lv2_response = requests.get(wilayah_lv2_url)
        wilayah_lv2_data = wilayah_lv2_response.json()
        
        wilayah_lv3_response = requests.get(wilayah_lv3_url)
        wilayah_lv3_data = wilayah_lv3_response.json()
        
        wilayah_lv4_response = requests.get(wilayah_lv4_url)
        wilayah_lv4_data = wilayah_lv4_response.json()

        votes_response = requests.get(votes_lv6_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_lv5_url)
        wilayah_data = wilayah_response.json()

        if votes_data["chart"] is not None:
            total_votes = sum(values for key, values in votes_data["chart"].items() if key != "null")
        else:
            total_votes = 0

        total_data = {}
        for key, value in names_data.items():
            votes = votes_data["chart"][key] if votes_data["chart"] is not None and key in votes_data["chart"] else 0
            percentage = votes / total_votes * 100 if total_votes != 0 else 0
            
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": votes,
                "votes_formatted": "{:,}".format(votes),
                "percentage": percentage,
                "percentage_formatted": "{:.2f}%".format(percentage),
            }

        last_update_timestamp = datetime.strptime(votes_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")
                
        if votes_data["chart"] is not None:
            highest_votes = max(values for key, values in votes_data["chart"].items() if key != "null")
        else:
            highest_votes = 0
        
        if votes_data["chart"] is not None:
            for key, values in votes_data["chart"].items():
                if values == highest_votes:
                    whose_highest = key
                    if key == "100025":
                        whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                    elif key == "100026":
                        whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                    elif key == "100027":
                        whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                    else:
                        whose_highest = key
        else:
            whose_highest = None
                
        if votes_data["chart"] is not None:
            votes_data_100025 = votes_data["chart"].get("100025")
            votes_data_100026 = votes_data["chart"].get("100026")
            votes_data_100027 = votes_data["chart"].get("100027")
        else:
            votes_data_100025 = 0
            votes_data_100026 = 0
            votes_data_100027 = 0
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        if total_votes_data != 0:
            percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
            percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
            percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        else:
            percentage_votes_data_100025 = 0
            percentage_votes_data_100026 = 0
            percentage_votes_data_100027 = 0

        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"

        html_progres = {
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break

        area_name_lv3 = None
        for item in wilayah_lv2_data:
            if item["kode"] == area_code_lv3:
                area_name_lv3 = item["nama"]
                break
            
        area_name_lv4 = None
        for item in wilayah_lv3_data:
            if item["kode"] == area_code_lv4:
                area_name_lv4 = item["nama"]
                break
        
        area_name_lv5 = None
        for item in wilayah_lv4_data:
            if item["kode"] == area_code_lv5:
                area_name_lv5 = item["nama"]
                break
            
        area_name_lv6 = None
        for item in wilayah_data:
            if item["kode"] == area_code_lv6:
                area_name_lv6 = item["nama"]
                break
        
        html_images = []
        if votes_data and "images" in votes_data:
            for i, image_url in enumerate(votes_data["images"], start=1):
                if image_url:
                    html_images.append(f'<div class="swiper-slide" style="background-image: url({image_url})">Slide {i}</div>')
        else:
            # Handle the case when "images" key is missing or empty
            html_images = ['<div class="swiper-slide">No images available</div>']
            
        administrasi = votes_data.get("administrasi", {})
        images = votes_data.get("images", [])

        if administrasi is not None:
            suara_sah = administrasi.get("suara_sah")
            suara_tidak_sah = administrasi.get("suara_tidak_sah")
            suara_total = administrasi.get("suara_total")
        else:
            suara_sah = 0
            suara_tidak_sah = 0
            suara_total = 0
        
        if suara_sah + suara_tidak_sah == suara_total:
            status_suara = "Votes (suara) - correct count"
        else:
            status_suara = "Votes (suara) - wrong count"

        if administrasi is not None:
            pemilih_dpt_jumlah = administrasi.get("pemilih_dpt_j")
            pemilih_dpt_laki = administrasi.get("pemilih_dpt_l")
            pemilih_dpt_perempuan = administrasi.get("pemilih_dpt_p")
        else:
            pemilih_dpt_jumlah = 0
            pemilih_dpt_laki = 0
            pemilih_dpt_perempuan = 0

        if pemilih_dpt_jumlah == pemilih_dpt_laki + pemilih_dpt_perempuan:
            status_pemilih_dpt = "Pemilih DPT - correct count"
        else:
            status_pemilih_dpt = "Pemilih DPT - wrong count"

        if administrasi is not None:
            pengguna_dpt_jumlah = administrasi.get("pengguna_dpt_j")
            pengguna_dpt_laki = administrasi.get("pengguna_dpt_l")
            pengguna_dpt_perempuan = administrasi.get("pengguna_dpt_p")
        else:
            pengguna_dpt_jumlah = 0
            pengguna_dpt_laki = 0
            pengguna_dpt_perempuan = 0

        
        if pengguna_dpt_jumlah == pengguna_dpt_laki + pengguna_dpt_perempuan:
            status_pengguna_dpt = "Pengguna DPT - correct count"
        else:
            status_pengguna_dpt = "Pengguna DPT - wrong count"
            
        if administrasi is not None:
            pengguna_dptb_jumlah = administrasi.get("pengguna_dptb_j")
            pengguna_dptb_laki = administrasi.get("pengguna_dptb_l")
            pengguna_dptb_perempuan = administrasi.get("pengguna_dptb_p")
        else:
            pengguna_dptb_jumlah = 0
            pengguna_dptb_laki = 0
            pengguna_dptb_perempuan = 0

        
        if pengguna_dptb_jumlah == pengguna_dptb_laki + pengguna_dptb_perempuan:
            status_pengguna_dptb = "Pengguna DPTB - correct count"
        else:
            status_pengguna_dptb = "Pengguna DPTB - wrong count"
            
        if administrasi is not None:
            pengguna_total_jumlah = administrasi.get("pengguna_total_j")
            pengguna_total_laki = administrasi.get("pengguna_total_l")
            pengguna_total_perempuan = administrasi.get("pengguna_total_p")
        else:
            # Assign default values of 0 when administrasi is None
            pengguna_total_jumlah = 0
            pengguna_total_laki = 0
            pengguna_total_perempuan = 0

        if pengguna_total_jumlah == pengguna_total_laki + pengguna_total_perempuan:
            status_pengguna_total = "Pengguna Total - correct count"
        else:
            status_pengguna_total = "Pengguna Total - wrong count"

        if administrasi is not None:
            pengguna_non_dpt_jumlah = administrasi.get("pengguna_non_dpt_j")
            pengguna_non_dpt_laki = administrasi.get("pengguna_non_dpt_l")
            pengguna_non_dpt_perempuan = administrasi.get("pengguna_non_dpt_p")
        else:
            pengguna_non_dpt_jumlah = 0
            pengguna_non_dpt_laki = 0
            pengguna_non_dpt_perempuan = 0

        if pengguna_non_dpt_jumlah == pengguna_non_dpt_laki + pengguna_non_dpt_perempuan:
            status_pengguna_non_dpt = "Pengguna Non DPT - correct count"
        else:
            status_pengguna_non_dpt = "Pengguna Non DPT - wrong count"

        if pengguna_total_jumlah == suara_sah + suara_tidak_sah:
            valid = "valid"
        else:
            valid = "invalid"

        modified_administrasi = {
            "valid": valid,
            "status_suara": status_suara,
            "status_pemilih_dpt": status_pemilih_dpt,
            "status_pengguna_dpt": status_pengguna_dpt,
            "status_pengguna_dptb": status_pengguna_dptb,
            "status_pengguna_total": status_pengguna_total,
            "status_pengguna_non_dpt": status_pengguna_non_dpt,

            "suara_sah_formated": f"{suara_sah:,}",
            "suara_tidak_sah_formated": f"{suara_tidak_sah:,}",
            "suara_total_formated": f"{suara_total:,}",
            "pemilih_dpt_jumlah_formated": f"{pemilih_dpt_jumlah:,}",
            "pemilih_dpt_laki_formated": f"{pemilih_dpt_laki:,}",
            "pemilih_dpt_perempuan_formated": f"{pemilih_dpt_perempuan:,}",
            "pengguna_dpt_jumlah_formated": f"{pengguna_dpt_jumlah:,}",
            "pengguna_dpt_laki_formated": f"{pengguna_dpt_laki:,}",
            "pengguna_dpt_perempuan_formated": f"{pengguna_dpt_perempuan:,}",
            "pengguna_dptb_jumlah_formated": f"{pengguna_dptb_jumlah:,}",
            "pengguna_dptb_laki_formated": f"{pengguna_dptb_laki:,}",
            "pengguna_dptb_perempuan_formated": f"{pengguna_dptb_perempuan:,}",
            "pengguna_total_jumlah_formated": f"{pengguna_total_jumlah:,}",
            "pengguna_total_laki_formated": f"{pengguna_total_laki:,}",
            "pengguna_total_perempuan_formated": f"{pengguna_total_perempuan:,}",
            "pengguna_non_dpt_jumlah_formated": f"{pengguna_non_dpt_jumlah:,}",
            "pengguna_non_dpt_laki_formated": f"{pengguna_non_dpt_laki:,}",
            "pengguna_non_dpt_perempuan_formated": f"{pengguna_non_dpt_perempuan:,}",
        }

        response_data = {
            "last_update": last_update_formatted,
            "area_code_lv2": area_code_lv2,
            "area_name_lv2": area_name_lv2,
            "area_code_lv3": area_code_lv3,
            "area_name_lv3": area_name_lv3,
            "area_code_lv4": area_code_lv4,
            "area_name_lv4": area_name_lv4,
            "area_code_lv5": area_code_lv5,
            "area_name_lv5": area_name_lv5,
            "area_code_lv6": area_code_lv6,
            "area_name_lv6": area_name_lv6,
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "html_progres": html_progres,
            "total_data": total_data,
            "images": images,
            "administrasi": modified_administrasi, 
        }

        return Response(response_data)


class HasilRekapTingkat1(APIView):
    def get(self, request, format=None):
        url = DATABASE + 'pemilu/hr/ppwp.json'

        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class HasilRekapTingkat2(APIView):
    def get(self, request, area_code_lv2, format=None):
        url = DATABASE + f'pemilu/hr/ppwp/{area_code_lv2}.json'

        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HasilRekapTingkat3(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, format=None):
        url = DATABASE + f'pemilu/hr/ppwp/{area_code_lv2}/{area_code_lv3}.json'

        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class HasilRekap1API(APIView):
    def get(self, request, format=None):
        names_url = DATABASE_API+ "api/names/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"
        rekap_hasil = DATABASE_API+ f"api/rekap/"

        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()

        rekap_hasil_response = requests.get(rekap_hasil)
        rekap_hasil_data = rekap_hasil_response.json()

        total_votes = sum(values for key, values in rekap_hasil_data["chart"].items() if key != "persen")
        
        total_data = {}
        for key, value in names_data.items():
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": rekap_hasil_data["chart"][key],
                "votes_formatted": "{:,}".format(rekap_hasil_data["chart"][key]),
                "percentage": rekap_hasil_data["chart"][key] / total_votes * 100,
                "percentage_formatted": "{:.2f}%".format(rekap_hasil_data["chart"][key] / total_votes * 100),
            }
            
        last_update_timestamp = datetime.strptime(rekap_hasil_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        total_child_data = {}
        for key, value in rekap_hasil_data["table"].items():
            area_code_lv1 = next((item["kode"] for item in wilayah_lv1_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_lv1_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_lv1_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_lv1_data if item["kode"] == key), None)
            total_child_data[key] = {
                "area_code_lv1": area_code_lv1,
                "area_id": area_id,
                "area_name": area_name,
                # "area_progress": value["persen"],
                # "area_progress_formatted": "{:.2f}%".format(value["persen"]),
                "level": level,
                "100025": value["100025"],
                "100025_formatted": "{:,}".format(value["100025"]),
                "100025_percentage": (value["100025"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100025_percentage_formatted": "{:.2f}%".format((value["100025"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "100026": value["100026"],
                "100026_formatted": "{:,}".format(value["100026"]),
                "100026_percentage": (value["100026"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100026_percentage_formatted": "{:.2f}%".format((value["100026"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "100027": value["100027"],
                "100027_formatted": "{:,}".format(value["100027"]),
                "100027_percentage": (value["100027"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100027_percentage_formatted": "{:.2f}%".format((value["100027"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "total_area_votes": value["100025"] + value["100026"] + value["100027"],
                "total_area_votes_formatted": "{:,}".format(value["100025"] + value["100026"] + value["100027"])
            }
            
            if key in rekap_hasil_data["progress_d_child"]:
                persen_da = rekap_hasil_data["progress_d_child"][key]["da"]["persen"]
                jml_wilayah_da = rekap_hasil_data["progress_d_child"][key]["da"]["jml_wilayah"]
                jml_wilayah_publikasi_da = rekap_hasil_data["progress_d_child"][key]["da"]["jml_wilayah_publikasi"]
                
                if jml_wilayah_publikasi_da != 0:
                    percentage_da = (jml_wilayah_publikasi_da / jml_wilayah_da) * 100
                else:
                    percentage_da = 0
                
                persen_db = rekap_hasil_data["progress_d_child"][key]["db"]["persen"]
                jml_wilayah_db = rekap_hasil_data["progress_d_child"][key]["db"]["jml_wilayah"]
                jml_wilayah_publikasi_db = rekap_hasil_data["progress_d_child"][key]["db"]["jml_wilayah_publikasi"]

                if jml_wilayah_publikasi_db != 0:
                    percentage_db = (jml_wilayah_publikasi_db / jml_wilayah_db) * 100
                else:
                    percentage_db = 0
                
                persen_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["persen"]
                jml_wilayah_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["jml_wilayah"]
                jml_wilayah_publikasi_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["jml_wilayah_publikasi"]
                
                if jml_wilayah_publikasi_dc != 0:
                    percentage_dc = (jml_wilayah_publikasi_dc / jml_wilayah_dc) * 100
                else:
                    percentage_dc = 0
                
                total_child_data[key].update({
                    "persen_hasil_kec": persen_da,
                    "percentage_kec": percentage_da,
                    "jml_wilayah_hasil_kec": jml_wilayah_da,
                    "jml_wilayah_publikasi_hasil_kec": jml_wilayah_publikasi_da,
                    "hasil_kec_formatted": f"{jml_wilayah_da:,} dari {jml_wilayah_publikasi_da:,} ({percentage_da:.2f}%)",
                    "percentage_kec_formatted": f"{percentage_da:.2f}%",
                    
                    "persen_hasil_kab_kota": persen_db,
                    "percentage_kab_kota": percentage_db,
                    "jml_wilayah_hasil_kab_kota": jml_wilayah_db,
                    "jml_wilayah_publikasi_hasil_kab_kota": jml_wilayah_publikasi_db,
                    "hasil_kab_kota_formatted": f"{jml_wilayah_db:,} dari {jml_wilayah_publikasi_db:,} ({percentage_db:.2f}%)",
                    "percentage_kab_kota_formatted": f"{percentage_db:.2f}%",
                    
                    "persen_hasil_prov": persen_dc,
                    "percentage_prov": percentage_dc,
                    "jml_wilayah_hasil_prov": jml_wilayah_dc,
                    "jml_wilayah_publikasi_hasil_prov": jml_wilayah_publikasi_dc,
                    "hasil_prov_formatted": f"{jml_wilayah_dc:,} dari {jml_wilayah_publikasi_dc:,} ({percentage_dc:.2f}%)",
                    "percentage_prov_formatted": f"{percentage_dc:.2f}%",
                })
            
        # total_progress_tps = rekap_hasil_data["progres"]["total"]
        # progress_tps = rekap_hasil_data["progres"]["progres"]

        # progress_data = {
        #     "total_tps": total_progress_tps,
        #     "total_tps_formatted": "{:,}".format(total_progress_tps),
        #     "progres_tps": progress_tps,
        #     "progres_tps_formatted": "{:,}".format(progress_tps),
        #     "percentage_tps": (progress_tps / total_progress_tps) * 100,
        #     "percentage_tps_formatted": "{:.2f}%".format((progress_tps / total_progress_tps) * 100),
        # }
        
        highest_votes = max(values for key, values in rekap_hasil_data["chart"].items())
        
        url_formd = rekap_hasil_data["url_formd"]
        
        for key, values in rekap_hasil_data["chart"].items():
            if values == highest_votes:
                whose_highest = key
                if key == "100025":
                    whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                elif key == "100026":
                    whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                elif key == "100027":
                    whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                else:
                    whose_highest = key
        
        # percentage_tps = (progress_tps / total_progress_tps) * 100
        
        votes_data_100025 = rekap_hasil_data["chart"]["100025"]
        votes_data_100026 = rekap_hasil_data["chart"]["100026"]
        votes_data_100027 = rekap_hasil_data["chart"]["100027"]
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
        percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
        percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        
        progress_d = rekap_hasil_data.get("progress_d", {})
        persen = progress_d.get("da", {}).get("persen")
        jml_wilayah = progress_d.get("da", {}).get("jml_wilayah")
        jml_wilayah_publikasi = progress_d.get("da", {}).get("jml_wilayah_publikasi")
        
        percentage_wilayah_d = (jml_wilayah_publikasi / jml_wilayah) * 100
        
        html_progres_wilayah = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_wilayah_d }%' aria-valuenow='{ percentage_wilayah_d }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"
        
        progress_data = {
            "persen": persen,
            "jml_wilayah": jml_wilayah,
            "jml_wilayah_publikasi": jml_wilayah_publikasi,
            "percentage_wilayah_d": "{:.2f}%".format(percentage_wilayah_d),
        }
        
        html_progres = {
            "html_progres_wilayah": html_progres_wilayah,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        response_data = {
            "last_update": last_update_formatted,
            "level_pemilu": "NASIONAL",
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "url_formd": rekap_hasil_data.get("url_formd", [])[0],
            "html_progres": html_progres,
            "progress_data": progress_data,
            "total_data": total_data,
            "total_child_data": total_child_data
        }

        return Response(response_data)
    
    
class HasilRekap2API(APIView):
    def get(self, request, area_code_lv2, format=None):
        names_url = DATABASE_API+ "api/names/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"
        wilayah_lv2_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/"
        rekap_hasil = DATABASE_API+ f"api/rekap/{area_code_lv2}/"

        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()
        
        wilayah_lv2_response = requests.get(wilayah_lv2_url)
        wilayah_lv2_data = wilayah_lv2_response.json()

        rekap_hasil_response = requests.get(rekap_hasil)
        rekap_hasil_data = rekap_hasil_response.json()

        total_votes = sum(values for key, values in rekap_hasil_data["chart"].items() if key != "persen")
        
        total_data = {}
        for key, value in names_data.items():
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": rekap_hasil_data["chart"][key],
                "votes_formatted": "{:,}".format(rekap_hasil_data["chart"][key]),
                "percentage": rekap_hasil_data["chart"][key] / total_votes * 100,
                "percentage_formatted": "{:.2f}%".format(rekap_hasil_data["chart"][key] / total_votes * 100),
            }
            
        last_update_timestamp = datetime.strptime(rekap_hasil_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        total_child_data = {}
        for key, value in rekap_hasil_data["table"].items():
            area_code_lv3 = next((item["kode"] for item in wilayah_lv2_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_lv2_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_lv2_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_lv2_data if item["kode"] == key), None)
            total_child_data[key] = {
                "code_lv2": area_code_lv2,
                "area_code_lv3": area_code_lv3,
                "area_id": area_id,
                "area_name": area_name,
                # "area_progress": value["persen"],
                # "area_progress_formatted": "{:.2f}%".format(value["persen"]),
                "level": level,
                "100025": value["100025"],
                "100025_formatted": "{:,}".format(value["100025"]),
                "100025_percentage": (value["100025"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100025_percentage_formatted": "{:.2f}%".format((value["100025"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "100026": value["100026"],
                "100026_formatted": "{:,}".format(value["100026"]),
                "100026_percentage": (value["100026"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100026_percentage_formatted": "{:.2f}%".format((value["100026"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "100027": value["100027"],
                "100027_formatted": "{:,}".format(value["100027"]),
                "100027_percentage": (value["100027"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100027_percentage_formatted": "{:.2f}%".format((value["100027"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "total_area_votes": value["100025"] + value["100026"] + value["100027"],
                "total_area_votes_formatted": "{:,}".format(value["100025"] + value["100026"] + value["100027"])
            }
            
            if key in rekap_hasil_data["progress_d_child"]:
                persen_da = rekap_hasil_data["progress_d_child"][key]["da"]["persen"]
                jml_wilayah_da = rekap_hasil_data["progress_d_child"][key]["da"]["jml_wilayah"]
                jml_wilayah_publikasi_da = rekap_hasil_data["progress_d_child"][key]["da"]["jml_wilayah_publikasi"]
                
                if jml_wilayah_publikasi_da != 0:
                    percentage_da = (jml_wilayah_publikasi_da / jml_wilayah_da) * 100
                else:
                    percentage_da = 0
                
                persen_db = rekap_hasil_data["progress_d_child"][key]["db"]["persen"]
                jml_wilayah_db = rekap_hasil_data["progress_d_child"][key]["db"]["jml_wilayah"]
                jml_wilayah_publikasi_db = rekap_hasil_data["progress_d_child"][key]["db"]["jml_wilayah_publikasi"]

                if jml_wilayah_publikasi_db != 0:
                    percentage_db = (jml_wilayah_publikasi_db / jml_wilayah_db) * 100
                else:
                    percentage_db = 0
                
                # persen_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["persen"]
                # jml_wilayah_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["jml_wilayah"]
                # jml_wilayah_publikasi_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["jml_wilayah_publikasi"]
                
                # if jml_wilayah_publikasi_dc != 0:
                #     percentage_dc = (jml_wilayah_publikasi_dc / jml_wilayah_dc) * 100
                # else:
                #     percentage_dc = 0
                
                total_child_data[key].update({
                    "persen_hasil_kec": persen_da,
                    "percentage_kec": percentage_da,
                    "jml_wilayah_hasil_kec": jml_wilayah_da,
                    "jml_wilayah_publikasi_hasil_kec": jml_wilayah_publikasi_da,
                    "hasil_kec_formatted": f"{jml_wilayah_da:,} dari {jml_wilayah_publikasi_da:,} ({percentage_da:.2f}%)",
                    "percentage_kec_formatted": f"{percentage_da:.2f}%",
                    
                    "persen_hasil_kab_kota": persen_db,
                    "percentage_kab_kota": percentage_db,
                    "jml_wilayah_hasil_kab_kota": jml_wilayah_db,
                    "jml_wilayah_publikasi_hasil_kab_kota": jml_wilayah_publikasi_db,
                    "hasil_kab_kota_formatted": f"{jml_wilayah_db:,} dari {jml_wilayah_publikasi_db:,} ({percentage_db:.2f}%)",
                    "percentage_kab_kota_formatted": f"{percentage_db:.2f}%",
                    
                    # "persen_hasil_prov": persen_dc,
                    # "percentage_prov": percentage_dc,
                    # "jml_wilayah_hasil_prov": jml_wilayah_dc,
                    # "jml_wilayah_publikasi_hasil_prov": jml_wilayah_publikasi_dc,
                    # "hasil_prov_formatted": f"{jml_wilayah_dc:,} dari {jml_wilayah_publikasi_dc:,} ({percentage_dc:.2f}%)",
                    # "percentage_prov_formatted": f"{percentage_dc:.2f}%",
                })
            
        # total_progress_tps = rekap_hasil_data["progres"]["total"]
        # progress_tps = rekap_hasil_data["progres"]["progres"]

        # progress_data = {
        #     "total_tps": total_progress_tps,
        #     "total_tps_formatted": "{:,}".format(total_progress_tps),
        #     "progres_tps": progress_tps,
        #     "progres_tps_formatted": "{:,}".format(progress_tps),
        #     "percentage_tps": (progress_tps / total_progress_tps) * 100,
        #     "percentage_tps_formatted": "{:.2f}%".format((progress_tps / total_progress_tps) * 100),
        # }
        
        highest_votes = max(values for key, values in rekap_hasil_data["chart"].items())
        
        url_formd = rekap_hasil_data["url_formd"]
        
        for key, values in rekap_hasil_data["chart"].items():
            if values == highest_votes:
                whose_highest = key
                if key == "100025":
                    whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                elif key == "100026":
                    whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                elif key == "100027":
                    whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                else:
                    whose_highest = key
        
        # percentage_tps = (progress_tps / total_progress_tps) * 100
        
        votes_data_100025 = rekap_hasil_data["chart"]["100025"]
        votes_data_100026 = rekap_hasil_data["chart"]["100026"]
        votes_data_100027 = rekap_hasil_data["chart"]["100027"]
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
        percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
        percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        
        progress_d = rekap_hasil_data.get("progress_d", {})
        persen = progress_d.get("da", {}).get("persen")
        jml_wilayah = progress_d.get("da", {}).get("jml_wilayah")
        jml_wilayah_publikasi = progress_d.get("da", {}).get("jml_wilayah_publikasi")
        
        percentage_wilayah_d = (jml_wilayah_publikasi / jml_wilayah) * 100
        
        html_progres_wilayah = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_wilayah_d }%' aria-valuenow='{ percentage_wilayah_d }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"
        
        progress_data = {
            "persen": persen,
            "jml_wilayah": jml_wilayah,
            "jml_wilayah_publikasi": jml_wilayah_publikasi,
            "percentage_wilayah_d": "{:.2f}%".format(percentage_wilayah_d),
        }
        
        html_progres = {
            "html_progres_wilayah": html_progres_wilayah,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break
        
        response_data = {
            "last_update": last_update_formatted,
            "level_pemilu": "NASIONAL",
            "area_code_lv2": area_code_lv2,
            "area_name_lv2": area_name_lv2,
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "url_formd": rekap_hasil_data.get("url_formd", [])[0],
            "html_progres": html_progres,
            "progress_data": progress_data,
            "total_data": total_data,
            "total_child_data": total_child_data
        }

        return Response(response_data)
    
    
class HasilRekap3API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, format=None):
        names_url = DATABASE_API+ "api/names/"
        wilayah_lv1_url = DATABASE_API+ "api/wilayah/0/"
        wilayah_lv2_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/"
        wilayah_lv3_url = DATABASE_API+ f"api/wilayah/{area_code_lv2}/{area_code_lv3}"
        
        rekap_hasil = DATABASE_API+ f"api/rekap/{area_code_lv2}/{area_code_lv3}"

        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()
        
        wilayah_lv2_response = requests.get(wilayah_lv2_url)
        wilayah_lv2_data = wilayah_lv2_response.json()
        
        wilayah_lv3_response = requests.get(wilayah_lv3_url)
        wilayah_lv3_data = wilayah_lv3_response.json()

        rekap_hasil_response = requests.get(rekap_hasil)
        rekap_hasil_data = rekap_hasil_response.json()

        total_votes = sum(values for key, values in rekap_hasil_data["chart"].items() if key != "persen")
        
        total_data = {}
        for key, value in names_data.items():
            total_data[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": rekap_hasil_data["chart"][key],
                "votes_formatted": "{:,}".format(rekap_hasil_data["chart"][key]),
                "percentage": rekap_hasil_data["chart"][key] / total_votes * 100,
                "percentage_formatted": "{:.2f}%".format(rekap_hasil_data["chart"][key] / total_votes * 100),
            }
            
        last_update_timestamp = datetime.strptime(rekap_hasil_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        total_child_data = {}
        for key, value in rekap_hasil_data["table"].items():
            area_code_lv4 = next((item["kode"] for item in wilayah_lv3_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_lv3_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_lv3_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_lv3_data if item["kode"] == key), None)
            total_child_data[key] = {
                "code_lv2": area_code_lv2,
                "area_code_lv3": area_code_lv3,
                "area_code_lv4": area_code_lv4,
                "area_id": area_id,
                "area_name": area_name,
                # "area_progress": value["persen"],
                # "area_progress_formatted": "{:.2f}%".format(value["persen"]),
                "level": level,
                "100025": value["100025"],
                "100025_formatted": "{:,}".format(value["100025"]),
                "100025_percentage": (value["100025"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100025_percentage_formatted": "{:.2f}%".format((value["100025"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "100026": value["100026"],
                "100026_formatted": "{:,}".format(value["100026"]),
                "100026_percentage": (value["100026"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100026_percentage_formatted": "{:.2f}%".format((value["100026"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "100027": value["100027"],
                "100027_formatted": "{:,}".format(value["100027"]),
                "100027_percentage": (value["100027"] / (value["100025"] + value["100026"] + value["100027"])) * 100,
                "100027_percentage_formatted": "{:.2f}%".format((value["100027"] / (value["100025"] + value["100026"] + value["100027"])) * 100),
                "total_area_votes": value["100025"] + value["100026"] + value["100027"],
                "total_area_votes_formatted": "{:,}".format(value["100025"] + value["100026"] + value["100027"])
            }
            
            if key in rekap_hasil_data["progress_d_child"]:
                persen_da = rekap_hasil_data["progress_d_child"][key]["da"]["persen"]
                jml_wilayah_da = rekap_hasil_data["progress_d_child"][key]["da"]["jml_wilayah"]
                jml_wilayah_publikasi_da = rekap_hasil_data["progress_d_child"][key]["da"]["jml_wilayah_publikasi"]
                
                if jml_wilayah_publikasi_da != 0:
                    percentage_da = (jml_wilayah_publikasi_da / jml_wilayah_da) * 100
                else:
                    percentage_da = 0
                
                # persen_db = rekap_hasil_data["progress_d_child"][key]["db"]["persen"]
                # jml_wilayah_db = rekap_hasil_data["progress_d_child"][key]["db"]["jml_wilayah"]
                # jml_wilayah_publikasi_db = rekap_hasil_data["progress_d_child"][key]["db"]["jml_wilayah_publikasi"]

                # if jml_wilayah_publikasi_db != 0:
                #     percentage_db = (jml_wilayah_publikasi_db / jml_wilayah_db) * 100
                # else:
                #     percentage_db = 0
                
                # persen_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["persen"]
                # jml_wilayah_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["jml_wilayah"]
                # jml_wilayah_publikasi_dc = rekap_hasil_data["progress_d_child"][key]["dc"]["jml_wilayah_publikasi"]
                
                # if jml_wilayah_publikasi_dc != 0:
                #     percentage_dc = (jml_wilayah_publikasi_dc / jml_wilayah_dc) * 100
                # else:
                #     percentage_dc = 0
                
                total_child_data[key].update({
                    "persen_hasil_kec": persen_da,
                    "percentage_kec": percentage_da,
                    "jml_wilayah_hasil_kec": jml_wilayah_da,
                    "jml_wilayah_publikasi_hasil_kec": jml_wilayah_publikasi_da,
                    "hasil_kec_formatted": f"{jml_wilayah_da:,} dari {jml_wilayah_publikasi_da:,} ({percentage_da:.2f}%)",
                    "percentage_kec_formatted": f"{percentage_da:.2f}%",
                    
                    # "persen_hasil_kab_kota": persen_db,
                    # "percentage_kab_kota": percentage_db,
                    # "jml_wilayah_hasil_kab_kota": jml_wilayah_db,
                    # "jml_wilayah_publikasi_hasil_kab_kota": jml_wilayah_publikasi_db,
                    # "hasil_kab_kota_formatted": f"{jml_wilayah_db:,} dari {jml_wilayah_publikasi_db:,} ({percentage_db:.2f}%)",
                    # "percentage_kab_kota_formatted": f"{percentage_db:.2f}%",
                    
                    # "persen_hasil_prov": persen_dc,
                    # "percentage_prov": percentage_dc,
                    # "jml_wilayah_hasil_prov": jml_wilayah_dc,
                    # "jml_wilayah_publikasi_hasil_prov": jml_wilayah_publikasi_dc,
                    # "hasil_prov_formatted": f"{jml_wilayah_dc:,} dari {jml_wilayah_publikasi_dc:,} ({percentage_dc:.2f}%)",
                    # "percentage_prov_formatted": f"{percentage_dc:.2f}%",
                })
            
        # total_progress_tps = rekap_hasil_data["progres"]["total"]
        # progress_tps = rekap_hasil_data["progres"]["progres"]

        # progress_data = {
        #     "total_tps": total_progress_tps,
        #     "total_tps_formatted": "{:,}".format(total_progress_tps),
        #     "progres_tps": progress_tps,
        #     "progres_tps_formatted": "{:,}".format(progress_tps),
        #     "percentage_tps": (progress_tps / total_progress_tps) * 100,
        #     "percentage_tps_formatted": "{:.2f}%".format((progress_tps / total_progress_tps) * 100),
        # }
        
        highest_votes = max(values for key, values in rekap_hasil_data["chart"].items())
        
        url_formd = rekap_hasil_data["url_formd"]
        
        for key, values in rekap_hasil_data["chart"].items():
            if values == highest_votes:
                whose_highest = key
                if key == "100025":
                    whose_highest = f"H. Anies Rasyid Baswedan, Ph.D. with {highest_votes:,} votes"
                elif key == "100026":
                    whose_highest = f"H. Prabowo Subianto with {highest_votes:,} votes"
                elif key == "100027":
                    whose_highest = f"H. Ganjar Pranowo, S.H., M.I.P. with {highest_votes:,} votes"
                else:
                    whose_highest = key
        
        # percentage_tps = (progress_tps / total_progress_tps) * 100
        
        votes_data_100025 = rekap_hasil_data["chart"]["100025"]
        votes_data_100026 = rekap_hasil_data["chart"]["100026"]
        votes_data_100027 = rekap_hasil_data["chart"]["100027"]
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027
        
        percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
        percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
        percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100
        
        progress_d = rekap_hasil_data.get("progress_d", {})
        persen = progress_d.get("da", {}).get("persen")
        jml_wilayah = progress_d.get("da", {}).get("jml_wilayah")
        jml_wilayah_publikasi = progress_d.get("da", {}).get("jml_wilayah_publikasi")
        
        percentage_wilayah_d = (jml_wilayah_publikasi / jml_wilayah) * 100
        
        html_progres_wilayah = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_wilayah_d }%' aria-valuenow='{ percentage_wilayah_d }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"
        
        progress_data = {
            "persen": persen,
            "jml_wilayah": jml_wilayah,
            "jml_wilayah_publikasi": jml_wilayah_publikasi,
            "percentage_wilayah_d": "{:.2f}%".format(percentage_wilayah_d),
        }
        
        html_progres = {
            "html_progres_wilayah": html_progres_wilayah,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break
            
        area_name_lv3 = None
        for item in wilayah_lv2_data:
            if item["kode"] == area_code_lv3:
                area_name_lv3 = item["nama"]
                break
        
        response_data = {
            "last_update": last_update_formatted,
            "level_pemilu": "NASIONAL",
            "area_code_lv2": area_code_lv2,
            "area_name_lv2": area_name_lv2,
            "area_code_lv3": area_code_lv3,
            "area_name_lv3": area_name_lv3,
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "url_formd": rekap_hasil_data.get("url_formd", [])[0],
            "html_progres": html_progres,
            "progress_data": progress_data,
            "total_data": total_data,
            "total_child_data": total_child_data
        }

        return Response(response_data)