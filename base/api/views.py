import requests
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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
    ]
    return Response(routes)


class Names(APIView):
    def get(self, request, format=None):
        url = 'https://sirekap-obj-data.kpu.go.id/pemilu/ppwp.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Sengketa(APIView):
    def get(self, request, format=None):
        url = 'https://sirekap-obj-data.kpu.go.id/pemilu/ds/ppwp.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WilayahTingkat2(APIView):
    def get(self, request, wilayah_tingkat2, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{wilayah_tingkat2}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                

class WilayahTingkat3(APIView):
    def get(self, request, wilayah_tingkat2, wilayah_tingkat3, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{wilayah_tingkat2}/{wilayah_tingkat3}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WilayahTingkat4(APIView):
    def get(self, request, wilayah_tingkat2, wilayah_tingkat3, wilayah_tingkat4, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{wilayah_tingkat2}/{wilayah_tingkat3}/{wilayah_tingkat4}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WilayahTingkat5(APIView):
    def get(self, request, wilayah_tingkat2, wilayah_tingkat3, wilayah_tingkat4, wilayah_tingkat5, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/wilayah/pemilu/ppwp/{wilayah_tingkat2}/{wilayah_tingkat3}/{wilayah_tingkat4}/{wilayah_tingkat5}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VotesTingkat1(APIView):
    def get(self, request, format=None):
        url = 'https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat2(APIView):
    def get(self, request, votes_tingkat2, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp/{votes_tingkat2}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat3(APIView):
    def get(self, request, votes_tingkat2, votes_tingkat3, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp/{votes_tingkat2}/{votes_tingkat3}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat4(APIView):
    def get(self, request, votes_tingkat2, votes_tingkat3, votes_tingkat4, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp/{votes_tingkat2}/{votes_tingkat3}/{votes_tingkat4}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat5(APIView):
    def get(self, request, votes_tingkat2, votes_tingkat3, votes_tingkat4, votes_tingkat5, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp/{votes_tingkat2}/{votes_tingkat3}/{votes_tingkat4}/{votes_tingkat5}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class VotesTingkat6(APIView):
    def get(self, request, votes_tingkat2, votes_tingkat3, votes_tingkat4, votes_tingkat5, votes_tingkat6, format=None):
        url = f'https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp/{votes_tingkat2}/{votes_tingkat3}/{votes_tingkat4}/{votes_tingkat5}/{votes_tingkat6}.json'
        
        try:
            response = requests.get(url)
            data = response.json()
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class HomeAPI(APIView):
    def get(self, request, format=None):
        names_url = "http://127.0.0.1:8000/api/names/"
        votes_url = "http://127.0.0.1:8000/api/votes/"
        wilayah_url = "http://127.0.0.1:8000/api/wilayah/0/"

        names_response = requests.get(names_url)
        names_data = names_response.json()

        votes_response = requests.get(votes_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_url)
        wilayah_data = wilayah_response.json()

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        
        level_1 = {}
        for key, value in names_data.items():
            level_1[key] = {
                "unique_number": str(value["nomor_urut"]).zfill(2),  # Padding with zeros
                "capres_name": value["nama"].split(" - ")[0].strip(),
                "cawapres_name": value["nama"].split(" - ")[1].strip(),
                "votes": votes_data["chart"][key],
                "votes_formatted": "{:,}".format(votes_data["chart"][key]),  # Formatting votes with thousands separator
                "percentage": votes_data["chart"][key] / total_votes * 100,
                "percentage_formatted": "{:.2f}%".format(votes_data["chart"][key] / total_votes * 100),
            }
            

        last_update_timestamp = datetime.strptime(votes_data["ts"], "%Y-%m-%d %H:%M:%S")
        last_update_formatted = last_update_timestamp.strftime("%d %B %Y %H:%M:%S WIB")

        level_2 = {}
        for key, value in votes_data["table"].items():
            area_code = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            level_2[key] = {
                "area_code": area_code,
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
        
        response_data = {
            "last_update": last_update_formatted,
            "highest_votes": highest_votes,
            "highest_votes_formatted": "{:,}".format(highest_votes),
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes),
            "progress_data": progress_data,
            "level_1": level_1,
            # **level_2
            "level_2": level_2
        }

        return Response(response_data)
