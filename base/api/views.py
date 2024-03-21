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
        'GET /api/level1-api/'
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
        

'''
level 1 is national
level 2 is province
level 3 is city
'''

class Level1API(APIView):
    def get(self, request, format=None):
        names_url = "http://127.0.0.1:8000/api/names/"
        votes_lv1_url = "http://127.0.0.1:8000/api/votes/"
        wilayah_lv1_url = "http://127.0.0.1:8000/api/wilayah/0/"

        names_response = requests.get(names_url)
        names_data = names_response.json()

        votes_response = requests.get(votes_lv1_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_lv1_url)
        wilayah_data = wilayah_response.json()

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        
        # level 1: data nasional
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

        # level 2: data provinsi
        level_2 = {}
        for key, value in votes_data["table"].items():
            area_code_lv2 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            level_2[key] = {
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
            "level_1": level_1,
            # **level_2
            "level_2": level_2
        }

        return Response(response_data)
    
    
class Level2API(APIView):
    def get(self, request, area_code_lv2, format=None):
        names_url = "http://127.0.0.1:8000/api/names/"
        votes_lv1_url = "http://127.0.0.1:8000/api/votes/"
        wilayah_lv1_url = "http://127.0.0.1:8000/api/wilayah/0/"
        votes_lv2_url = f"http://127.0.0.1:8000/api/votes/{area_code_lv2}/"
        wilayah_lv2_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/"


        names_response = requests.get(names_url)
        names_data = names_response.json()

        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv1_data = wilayah_lv1_response.json()

        votes_response = requests.get(votes_lv2_url)
        votes_data = votes_response.json()
        
        wilayah_response = requests.get(wilayah_lv2_url)
        wilayah_data = wilayah_response.json()

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        
        # level 2: data provinsi
        level_2 = {}
        for key, value in names_data.items():
            level_2[key] = {
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

        # level 3: data kabupaten/kota
        level_3 = {}
        for key, value in votes_data["table"].items():
            area_code_lv3 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            level_3[key] = {
                "code_lv2": area_code_lv2,
                "area_code_lv3": area_code_lv3,
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
            "level_2": level_2,
            # **level_3
            "level_3": level_3
        }

        return Response(response_data)
    
    
class Level3API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, format=None):
        names_url = "http://127.0.0.1:8000/api/names/"
        votes_lv1_url = "http://127.0.0.1:8000/api/votes/"
        wilayah_lv1_url = "http://127.0.0.1:8000/api/wilayah/0/"
        votes_lv2_url = f"http://127.0.0.1:8000/api/votes/{area_code_lv2}/"
        wilayah_lv2_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/"
        votes_lv3_url = f"http://127.0.0.1:8000/api/votes/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv3_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        
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
        
        level_3 = {}
        for key, value in names_data.items():
            level_3[key] = {
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

        level_4 = {}
        for key, value in votes_data["table"].items():
            area_code_lv4 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            level_4[key] = {
                "code_lv2": area_code_lv2,
                "area_code_lv3": area_code_lv3,
                "area_code_lv4": area_code_lv4,
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
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break
        # print(wilayah_lv3_data)
        area_name_lv3 = None
        for item in wilayah_lv2_data:
            if item["kode"] == area_code_lv3:
                area_name_lv3 = item["nama"]
                break
        # print(item)

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
            "level_3": level_3,
            # **level_4
            "level_4": level_4
        }

        return Response(response_data)
    
    
class Level4API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, area_code_lv4, format=None):
        names_url = "http://127.0.0.1:8000/api/names/"
        wilayah_lv1_url = "http://127.0.0.1:8000/api/wilayah/0/"
        wilayah_lv2_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/"
        wilayah_lv3_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv4_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        votes_lv4_url = f"http://127.0.0.1:8000/api/votes/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        
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

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        
        level_4 = {}
        for key, value in names_data.items():
            level_4[key] = {
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

        level_5 = {}
        for key, value in votes_data["table"].items():
            area_code_lv5 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)
            level_5[key] = {
                "code_lv2": area_code_lv2,
                "area_code_lv3": area_code_lv3,
                "area_code_lv4": area_code_lv4,
                "area_code_lv5": area_code_lv5,
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
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break
        # print(wilayah_lv3_data)
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
            # print(item)

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
            "level_4": level_4,
            # **level_5
            "level_5": level_5
        }

        return Response(response_data)
    
    
class Level5API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, area_code_lv4, area_code_lv5, format=None):
        names_url = "http://127.0.0.1:8000/api/names/"
        wilayah_lv1_url = "http://127.0.0.1:8000/api/wilayah/0/"
        wilayah_lv2_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/"
        wilayah_lv3_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv4_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        wilayah_lv5_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/"
        votes_lv5_url = f"http://127.0.0.1:8000/api/votes/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/"
        
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
        # print(votes_data)
        
        wilayah_response = requests.get(wilayah_lv5_url)
        wilayah_data = wilayah_response.json()

        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        
        level_5 = {}
        for key, value in names_data.items():
            level_5[key] = {
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

        level_6 = {}
        for key, value in votes_data["table"].items():
            area_code_lv6 = next((item["kode"] for item in wilayah_data if item["kode"] == key), None)
            area_id = next((item["id"] for item in wilayah_data if item["kode"] == key), None)
            area_name = next((item["nama"] for item in wilayah_data if item["kode"] == key), None)
            level = next((item["tingkat"] for item in wilayah_data if item["kode"] == key), None)

            # Check if keys exist before accessing them
            votes_100025 = value.get("100025", 0)
            votes_100026 = value.get("100026", 0)
            votes_100027 = value.get("100027", 0)

            level_6[key] = {
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
        # print(wilayah_lv3_data)
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
            # print(item)
        
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
            "level_5": level_5,
            # **level_6
            "level_6": level_6
        }

        return Response(response_data)
    
    
class Level6API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, area_code_lv4, area_code_lv5, area_code_lv6, format=None):
        names_url = "http://127.0.0.1:8000/api/names/"
        wilayah_lv1_url = "http://127.0.0.1:8000/api/wilayah/0/"
        wilayah_lv2_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/"
        wilayah_lv3_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv4_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        wilayah_lv5_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/"
        votes_lv6_url = f"http://127.0.0.1:8000/api/votes/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/{area_code_lv6}"
        
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
        # print(votes_data)
        
        wilayah_response = requests.get(wilayah_lv5_url)
        wilayah_data = wilayah_response.json()

        # total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen")
        # Calculate total votes, filtering out the 'null' value
        total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen" and values is not None)

        
        level_6 = {}
        for key, value in names_data.items():
            level_6[key] = {
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
        
        # highest_votes = max(values for key, values in votes_data["chart"].items() if key != "persen")
        
        # Filter out None values before finding the maximum
        filtered_values = [value for key, value in votes_data["chart"].items() if value is not None]

        # Check if there are any non-None values before finding the maximum
        if filtered_values:
            highest_votes = max(filtered_values)
        else:
            # Handle the case when all values are None
            highest_votes = None

        
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
        
        # percentage_tps = (progress_tps / total_progress_tps) * 100
        
        votes_data_100025 = votes_data["chart"]["100025"]
        votes_data_100026 = votes_data["chart"]["100026"]
        votes_data_100027 = votes_data["chart"]["100027"]
        
        total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027

        percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
        percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
        percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100

        # html_progres_tps = f"<div class='progress-bar bg-success' role='progressbar' style='width: { percentage_tps }%' aria-valuenow='{ percentage_tps }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100025 = f"<div class='progress-bar bg-secondary' role='progressbar' style='width: { percentage_votes_data_100025 }%' aria-valuenow='{ percentage_votes_data_100025 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progres_100026 = f"<div class='progress-bar bg-primary' role='progressbar' style='width: { percentage_votes_data_100026 }%' aria-valuenow='{ percentage_votes_data_100026 }' aria-valuemin='0' aria-valuemax='100'></div>"
        html_progress_100027 = f"<div class='progress-bar bg-danger' role='progressbar' style='width: { percentage_votes_data_100027 }%' aria-valuenow='{ percentage_votes_data_100027 }' aria-valuemin='0' aria-valuemax='100'></div>"

        html_progres = {
            # "html_progres_tps": html_progres_tps,
            "html_progress_100025": html_progres_100025,
            "html_progress_100026": html_progres_100026,
            "html_progress_100027": html_progress_100027
        }
        
        area_name_lv2 = None
        for item in wilayah_lv1_data:
            if item["kode"] == area_code_lv2:
                area_name_lv2 = item["nama"]
                break
        # print(wilayah_lv3_data)
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
            # print(item)
        
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

        suara_sah = administrasi["suara_sah"]
        suara_tidak_sah = administrasi["suara_tidak_sah"]
        suara_total = administrasi["suara_total"]
        
        if suara_sah + suara_tidak_sah == suara_total:
            status_suara = "Votes (suara) - correct count"
        else:
            status_suara = "Votes (suara) - wrong count"

        pemilih_dpt_jumlah = administrasi["pemilih_dpt_j"]
        pemilih_dpt_laki = administrasi["pemilih_dpt_l"]
        pemilih_dpt_perempuan = administrasi["pemilih_dpt_p"]
        
        if pemilih_dpt_jumlah == pemilih_dpt_laki + pemilih_dpt_perempuan:
            status_pemilih_dpt = "Pemilih DPT - correct count"
        else:
            status_pemilih_dpt = "Pemilih DPT - wrong count"

        pengguna_dpt_jumlah = administrasi["pengguna_dpt_j"]
        pengguna_dpt_laki = administrasi["pengguna_dpt_l"]
        pengguna_dpt_perempuan = administrasi["pengguna_dpt_p"]
        
        if pengguna_dpt_jumlah == pengguna_dpt_laki + pengguna_dpt_perempuan:
            status_pengguna_dpt = "Pengguna DPT - correct count"
        else:
            status_pengguna_dpt = "Pengguna DPT - wrong count"
            
        pengguna_dptb_jumlah = administrasi["pengguna_dptb_j"]
        pengguna_dptb_laki = administrasi["pengguna_dptb_l"]
        pengguna_dptb_perempuan = administrasi["pengguna_dptb_p"]
        
        if pengguna_dptb_jumlah == pengguna_dptb_laki + pengguna_dptb_perempuan:
            status_pengguna_dptb = "Pengguna DPTB - correct count"
        else:
            status_pengguna_dptb = "Pengguna DPTB - wrong count"
            
        pengguna_total_jumlah = administrasi["pengguna_total_j"]
        pengguna_total_laki = administrasi["pengguna_total_l"]
        pengguna_total_perempuan = administrasi["pengguna_total_p"]

        if pengguna_total_jumlah == pengguna_total_laki + pengguna_total_perempuan:
            status_pengguna_total = "Pengguna Total - correct count"
        else:
            status_pengguna_total = "Pengguna Total - wrong count"

        pengguna_non_dpt_jumlah = administrasi["pengguna_non_dpt_j"]
        pengguna_non_dpt_laki = administrasi["pengguna_non_dpt_l"]
        pengguna_non_dpt_perempuan = administrasi["pengguna_non_dpt_p"]

        if pengguna_non_dpt_jumlah == pengguna_non_dpt_laki + pengguna_non_dpt_perempuan:
            status_pengguna_non_dpt = "Pengguna Non DPT - correct count"
        else:
            status_pengguna_non_dpt = "Pengguna Non DPT - wrong count"

        if pengguna_total_jumlah == suara_sah + suara_tidak_sah:
            valid = "valid"
        else:
            valid = "invalid"

        modified_administrasi = {
            # "suara_sah": administrasi["suara_sah"],
            "valid": valid,
            "status_suara": status_suara,
            "status_pemilih_dpt": status_pemilih_dpt,
            "status_pengguna_dpt": status_pengguna_dpt,
            "status_pengguna_dptb": status_pengguna_dptb,
            "status_pengguna_total": status_pengguna_total,
            "status_pengguna_non_dpt": status_pengguna_non_dpt,

            "suara_sah_formated": f"{administrasi['suara_sah']:,}",
            # "suara_tidak_sah": administrasi["suara_tidak_sah"],
            "suara_tidak_sah_formated": f"{administrasi['suara_tidak_sah']:,}",
            # "suara_total": administrasi["suara_total"],
            "suara_total_formated": f"{administrasi['suara_total']:,}",
            # "pemilih_dpt_jumlah": administrasi["pemilih_dpt_j"],
            "pemilih_dpt_jumlah_formated": f"{administrasi['pemilih_dpt_j']:,}",
            # "pemilih_dpt_laki": administrasi["pemilih_dpt_l"],
            "pemilih_dpt_laki_formated": f"{administrasi['pemilih_dpt_l']:,}",
            # "pemilih_dpt_perempuan": administrasi["pemilih_dpt_p"],
            "pemilih_dpt_perempuan_formated": f"{administrasi['pemilih_dpt_p']:,}",
            # "pengguna_dpt_jumlah": administrasi["pengguna_dpt_j"],
            "pengguna_dpt_jumlah_formated": f"{administrasi['pengguna_dpt_j']:,}",
            # "pengguna_dpt_laki": administrasi["pengguna_dpt_l"],
            "pengguna_dpt_laki_formated": f"{administrasi['pengguna_dpt_l']:,}",
            # "pengguna_dpt_perempuan": administrasi["pengguna_dpt_p"],
            "pengguna_dpt_perempuan_formated": f"{administrasi['pengguna_dpt_p']:,}",
            # "pengguna_dptb_jumlah": administrasi["pengguna_dptb_j"],
            "pengguna_dptb_jumlah_formated": f"{administrasi['pengguna_dptb_j']:,}",
            # "pengguna_dptb_laki": administrasi["pengguna_dptb_l"],
            "pengguna_dptb_laki_formated": f"{administrasi['pengguna_dptb_l']:,}",
            # "pengguna_dptb_perempuan": administrasi["pengguna_dptb_p"],
            "pengguna_dptb_perempuan_formated": f"{administrasi['pengguna_dptb_p']:,}",
            # "pengguna_total_jumlah": administrasi["pengguna_total_j"],
            "pengguna_total_jumlah_formated": f"{administrasi['pengguna_total_j']:,}",
            # "pengguna_total_laki": administrasi["pengguna_total_l"],
            "pengguna_total_laki_formated": f"{administrasi['pengguna_total_l']:,}",
            # "pengguna_total_perempuan": administrasi["pengguna_total_p"],
            "pengguna_total_perempuan_formated": f"{administrasi['pengguna_total_p']:,}",
            # "pengguna_non_dpt_jumlah": administrasi["pengguna_non_dpt_j"],
            "pengguna_non_dpt_jumlah_formated": f"{administrasi['pengguna_non_dpt_j']:,}",
            # "pengguna_non_dpt_laki": administrasi["pengguna_non_dpt_l"],
            "pengguna_non_dpt_laki_formated": f"{administrasi['pengguna_non_dpt_l']:,}",
            # "pengguna_non_dpt_perempuan": administrasi["pengguna_non_dpt_p"],
            "pengguna_non_dpt_perempuan_formated": f"{administrasi['pengguna_non_dpt_p']:,}",
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
            # "progress_data": progress_data,
            "level_6": level_6,
            "images": images,  # Include the "images" field, defaulting to an empty list if not present
            "administrasi": modified_administrasi, 
        }

        return Response(response_data)
    
    
class Level61API(APIView):
    def get(self, request, area_code_lv2, area_code_lv3, area_code_lv4, area_code_lv5, area_code_lv6, format=None):
        # Define URLs
        names_url = "http://127.0.0.1:8000/api/names/"
        wilayah_lv1_url = "http://127.0.0.1:8000/api/wilayah/0/"
        wilayah_lv2_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/"
        wilayah_lv3_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/"
        wilayah_lv4_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/"
        wilayah_lv5_url = f"http://127.0.0.1:8000/api/wilayah/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/"
        votes_lv6_url = f"http://127.0.0.1:8000/api/votes/{area_code_lv2}/{area_code_lv3}/{area_code_lv4}/{area_code_lv5}/{area_code_lv6}"
        
        # Make API requests
        names_response = requests.get(names_url)
        wilayah_lv1_response = requests.get(wilayah_lv1_url)
        wilayah_lv2_response = requests.get(wilayah_lv2_url)
        wilayah_lv3_response = requests.get(wilayah_lv3_url)
        wilayah_lv4_response = requests.get(wilayah_lv4_url)
        wilayah_lv5_response = requests.get(wilayah_lv5_url)
        votes_response = requests.get(votes_lv6_url)

        # Initialize default values
        default_data = {
            "area_name": None,
            "highest_votes": None,
            "highest_votes_formatted": None,
            "whose_highest_votes": None,
            "total_votes": None,
            "total_votes_formatted": None,
            "html_progres": None,
            "level_6": {},
            "images": [],
            "administrasi": {}
        }

        # Parse JSON data or use default values if API request fails
        names_data = names_response.json() if names_response.status_code == 200 else {}
        wilayah_lv1_data = wilayah_lv1_response.json() if wilayah_lv1_response.status_code == 200 else []
        wilayah_lv2_data = wilayah_lv2_response.json() if wilayah_lv2_response.status_code == 200 else []
        wilayah_lv3_data = wilayah_lv3_response.json() if wilayah_lv3_response.status_code == 200 else []
        wilayah_lv4_data = wilayah_lv4_response.json() if wilayah_lv4_response.status_code == 200 else []
        wilayah_lv5_data = wilayah_lv5_response.json() if wilayah_lv5_response.status_code == 200 else []
        votes_data = votes_response.json() if votes_response.status_code == 200 else {}

        # Handle missing data by filling with default values
        area_name_lv2 = wilayah_lv1_data[0]["nama"] if wilayah_lv1_data else None
        area_name_lv3 = wilayah_lv2_data[0]["nama"] if wilayah_lv2_data else None
        area_name_lv4 = wilayah_lv3_data[0]["nama"] if wilayah_lv3_data else None
        area_name_lv5 = wilayah_lv4_data[0]["nama"] if wilayah_lv4_data else None
        area_name_lv6 = wilayah_lv5_data[0]["nama"] if wilayah_lv5_data else None

        highest_votes = None
        whose_highest = None
        total_votes = None
        html_progres = None

        if votes_data["chart"] is not None:
            total_votes = sum(values for key, values in votes_data["chart"].items() if key != "persen" and values is not None)

            filtered_values = [value for key, value in votes_data["chart"].items() if value is not None]
            if filtered_values:
                highest_votes = max(filtered_values)

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

            votes_data_100025 = votes_data["chart"].get("100025", 0)
            votes_data_100026 = votes_data["chart"].get("100026", 0)
            votes_data_100027 = votes_data["chart"].get("100027", 0)

            total_votes_data = votes_data_100025 + votes_data_100026 + votes_data_100027

            if total_votes_data != 0:
                percentage_votes_data_100025 = (votes_data_100025 / total_votes_data) * 100
                percentage_votes_data_100026 = (votes_data_100026 / total_votes_data) * 100
                percentage_votes_data_100027 = (votes_data_100027 / total_votes_data) * 100

                html_progres = {
                    "html_progress_100025": f"<div class='progress-bar bg-secondary' role='progressbar' style='width: {percentage_votes_data_100025}%' aria-valuenow='{percentage_votes_data_100025}' aria-valuemin='0' aria-valuemax='100'></div>",
                    "html_progress_100026": f"<div class='progress-bar bg-primary' role='progressbar' style='width: {percentage_votes_data_100026}%' aria-valuenow='{percentage_votes_data_100026}' aria-valuemin='0' aria-valuemax='100'></div>",
                    "html_progress_100027": f"<div class='progress-bar bg-danger' role='progressbar' style='width: {percentage_votes_data_100027}%' aria-valuenow='{percentage_votes_data_100027}' aria-valuemin='0' aria-valuemax='100'></div>"
                }

        modified_administrasi = {}

        if votes_data["administrasi"] is not None:
            administrasi = votes_data["administrasi"]

            suara_sah = administrasi.get("suara_sah", 0)
            suara_tidak_sah = administrasi.get("suara_tidak_sah", 0)
            suara_total = administrasi.get("suara_total", 0)

            if suara_sah + suara_tidak_sah == suara_total:
                status_suara = "CORRECT!!!!"
            else:
                status_suara = "WRONG!!!!"

            modified_administrasi = {
                # "suara_sah": suara_sah,
                "suara_sah_formated": f"{suara_sah:,}",
                # "suara_tidak_sah": suara_tidak_sah,
                "suara_tidak_sah_formated": f"{suara_tidak_sah:,}",
                # "suara_total": suara_total,
                "suara_total_formated": f"{suara_total:,}",
                "status_suara": status_suara,
                # "pemilih_dpt_jumlah": administrasi.get("pemilih_dpt_j", 0),
                "pemilih_dpt_jumlah_formated": f"{administrasi.get('pemilih_dpt_j', 0):,}",
                # "pemilih_dpt_laki": administrasi.get("pemilih_dpt_l", 0),
                "pemilih_dpt_laki_formated": f"{administrasi.get('pemilih_dpt_l', 0):,}",
                # "pemilih_dpt_perempuan": administrasi.get("pemilih_dpt_p", 0),
                "pemilih_dpt_perempuan_formated": f"{administrasi.get('pemilih_dpt_p', 0):,}",
                # "pengguna_dpt_jumlah": administrasi.get("pengguna_dpt_j", 0),
                "pengguna_dpt_jumlah_formated": f"{administrasi.get('pengguna_dpt_j', 0):,}",
                # "pengguna_dpt_laki": administrasi.get("pengguna_dpt_l", 0),
                "pengguna_dpt_laki_formated": f"{administrasi.get('pengguna_dpt_l', 0):,}",
                # "pengguna_dpt_perempuan": administrasi.get("pengguna_dpt_p", 0),
                "pengguna_dpt_perempuan_formated": f"{administrasi.get('pengguna_dpt_p', 0):,}",
                # "pengguna_dptb_jumlah": administrasi.get("pengguna_dptb_j", 0),
                "pengguna_dptb_jumlah_formated": f"{administrasi.get('pengguna_dptb_j', 0):,}",
                # "pengguna_dptb_laki": administrasi.get("pengguna_dptb_l", 0),
                "pengguna_dptb_laki_formated": f"{administrasi.get('pengguna_dptb_l', 0):,}",
                # "pengguna_dptb_perempuan": administrasi.get("pengguna_dptb_p", 0),
                "pengguna_dptb_perempuan_formated": f"{administrasi.get('pengguna_dptb_p', 0):,}",
                # "pengguna_total_jumlah": administrasi.get("pengguna_total_j", 0),
                "pengguna_total_jumlah_formated": f"{administrasi.get('pengguna_total_j', 0):,}",
                # "pengguna_total_laki": administrasi.get("pengguna_total_l", 0),
                "pengguna_total_laki_formated": f"{administrasi.get('pengguna_total_l', 0):,}",
                # "pengguna_total_perempuan": administrasi.get("pengguna_total_p", 0),
                "pengguna_total_perempuan_formated": f"{administrasi.get('pengguna_total_p', 0):,}",
                # "pengguna_non_dpt_jumlah": administrasi.get("pengguna_non_dpt_j", 0),
                "pengguna_non_dpt_jumlah_formated": f"{administrasi.get('pengguna_non_dpt_j', 0):,}",
                # "pengguna_non_dpt_laki": administrasi.get("pengguna_non_dpt_l", 0),
                "pengguna_non_dpt_laki_formated": f"{administrasi.get('pengguna_non_dpt_l', 0):,}",
                # "pengguna_non_dpt_perempuan": administrasi.get("pengguna_non_dpt_p", 0),
                "pengguna_non_dpt_perempuan_formated": f"{administrasi.get('pengguna_non_dpt_p', 0):,}",
            }

        # Construct response data
        response_data = {
            "last_update": datetime.now().strftime("%d %B %Y %H:%M:%S WIB"),
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
            "highest_votes_formatted": "{:,}".format(highest_votes) if highest_votes is not None else None,
            "whose_highest_votes": whose_highest,
            "total_votes": total_votes,
            "total_votes_formatted": "{:,}".format(total_votes) if total_votes is not None else None,
            "html_progres": html_progres,
            "level_6": {},
            "images": votes_data.get("images", []),
            "administrasi": modified_administrasi,
        }

        return Response(response_data)
