import requests
from bs4 import BeautifulSoup
import random

MAIN_URL = "https://www.coupondunia.in/category/travel?noOfPages=10"

ALL_IPS = ['122.144.8.30:43935', '134.119.214.200:1080', '136.228.128.14:61158', '103.56.232.130:31816', '31.214.138.207:8080', '77.37.142.203:53281', '185.6.167.99:51123', '118.97.235.234:8080', '103.44.139.87:30191', '151.106.10.56:1080', '103.205.26.57:8080', '177.55.189.156:8080', '178.18.197.82:80', '5.143.65.246:8081', '118.174.233.18:61605', '163.53.198.54:42787', '185.238.139.203:3128', '5.202.94.49:80', '122.144.8.28:43935', '178.239.145.13:80', '182.19.41.145:80', '176.124.128.97:56595', '89.250.220.40:40423', '191.238.218.78:80', '5.202.157.192:80', '37.152.174.58:80', '219.92.37.172:80', '5.202.77.119:80', '5.202.151.74:80', '192.162.214.11:41258', '185.135.74.151:80', '1.10.189.100:50169', '185.215.235.165:80', '103.250.157.46:37013', '80.211.233.19:80', '194.32.78.57:80', '212.101.74.73:443', '212.101.74.74:443', '138.197.67.160:3128', '164.132.98.72:8080', '31.14.133.86:8080', '47.254.83.176:8080', '167.99.165.114:3128', '103.87.16.2:80', '208.131.186.162:31866', '37.235.30.123:80', '201.184.93.218:30310', '3.19.17.101:8080', '54.183.35.194:3128', '37.152.170.67:80', '5.202.46.65:80', '185.126.13.245:80', '35.236.97.7:3128', '35.236.90.146:3128', '213.230.68.183:3128', '142.93.202.126:8080', '187.12.121.138:65301', '36.67.57.165:8888', '185.205.249.24:49335', '182.163.111.85:34778', '91.137.104.188:80', '92.255.205.227:30359', '190.145.76.19:33230', '116.74.95.18:21776', '123.201.19.116:50543', '36.89.228.57:35400', '95.67.114.222:60748', '185.126.13.225:80', '185.126.13.181:80', '185.126.7.237:80', '35.236.56.105:3128', '118.99.119.171:8080', '68.183.42.79:3128', '35.245.39.255:3128', '197.234.42.241:8083', '185.126.13.86:80', '185.126.13.173:80', '185.126.13.187:80', '128.199.102.188:3128', '181.115.180.178:42791', '157.230.210.133:8080', '91.222.196.177:80', '91.237.254.21:80', '91.237.254.30:80', '37.19.89.214:80', '5.202.46.166:80', '128.199.106.195:80', '5.202.101.226:80', '5.202.67.186:80', '159.203.7.65:3128', '95.179.135.66:3128', '191.252.191.23:80', '13.58.1.38:8080', '172.104.43.148:8080', '157.230.187.183:80', '159.203.27.154:3128', '5.202.94.134:80', '104.248.67.19:8080', '185.126.7.15:80', '185.224.177.54:80', '138.68.174.231:8080', '35.183.224.95:8080', '54.90.184.114:8080', '157.230.227.116:8080', '46.218.155.194:3128', '37.114.201.2:80', '164.58.168.2:8080', '138.201.193.196:8080', '37.32.28.38:80', '35.236.207.97:8080', '128.199.169.60:80', '212.33.197.155:80', '37.32.11.183:80', '180.183.136.150:8080', '118.175.93.91:52142', '118.106.145.95:80', '212.67.0.150:33171', '217.112.173.215:55934', '36.67.31.95:41766', '212.112.113.27:37393', '78.36.203.200:30967', '95.158.47.79:52761', '13.232.165.154:80', '193.151.119.233:30068', '212.232.6.15:53281', '62.182.110.19:41258', '85.30.215.48:32946', '103.255.235.38:39847', '117.4.243.172:40870', '110.164.197.99:8080', '46.243.172.29:8080', '131.196.141.44:33729', '12.190.124.122:8888', '36.69.95.226:8080', '195.16.48.142:36083', '37.143.160.5:59027', '79.171.13.182:39282', '94.127.217.66:40115', '103.58.251.181:41936', '209.97.170.0:31330', '117.242.147.73:43592', '103.53.110.55:44164', '109.237.147.213:37581', '103.106.58.42:54117', '116.212.150.7:34295', '200.53.220.253:59947', '27.116.20.209:36630', '46.48.88.238:32379', '103.216.172.1:50031', '194.213.212.60:51022', '177.36.7.61:53281', '134.119.214.196:1080', '177.72.72.217:40311', '115.85.65.146:39736', '190.90.63.140:48736', '18.231.95.69:80', '93.76.239.44:43823', '118.172.70.209:8080', '82.147.120.41:60682', '180.183.98.217:8213', '103.111.53.82:44495', '117.74.113.45:50091', '180.248.248.155:8080', '79.101.98.2:53281', '109.167.113.9:42004', '103.94.66.85:46103', '159.224.37.181:32288', '185.46.219.124:80', '198.199.122.218:8080', '99.79.100.105:8080', '99.79.53.109:8080', '202.129.251.39:23500', '94.154.31.136:53281', '207.182.135.148:443', '185.126.12.62:80', '185.126.12.26:80', '185.126.12.72:80', '185.126.15.210:80', '103.239.145.109:32807', '85.112.77.210:41258', '103.248.30.34:8080', '217.64.109.234:45282', '180.183.100.144:8213', '171.100.204.146:38878', '188.95.77.33:46509', '95.215.228.130:36988', '139.5.29.55:48087', '103.117.213.74:57403', '185.13.229.138:80', '91.144.154.253:8080', '103.9.188.135:39619', '202.131.229.98:45134', '180.183.127.48:8213', '86.57.177.8:50348', '36.66.83.153:35056', '180.250.159.34:56979', '182.52.51.31:30298', '103.87.171.251:32582', '159.65.8.166:3128', '182.73.56.134:56124', '35.236.195.107:3128', '109.195.103.121:56376', '54.233.117.98:3128', '185.126.1.118:80', '185.126.12.159:80', '153.232.170.16:8080', '212.33.199.22:80', '5.202.154.33:80', '37.152.168.15:80', '201.217.247.99:80', '91.210.252.118:8080', '37.152.173.176:80', '103.74.220.47:43678', '117.255.223.5:8080', '175.141.131.216:8080', '182.52.112.205:8080', '190.63.134.220:31499', '35.236.105.107:3128', '191.241.226.230:53281', '2.180.36.99:32996', '103.9.188.151:37974', '77.104.250.236:53281', '195.88.42.19:51147', '115.178.99.247:23500', '36.67.8.245:58626', '37.17.9.28:35387', '178.128.243.15:80', '195.9.44.50:55197', '85.30.48.222:30228', '36.37.70.90:60383', '138.219.248.2:31586', '179.124.11.128:58092', '124.41.211.86:61199', '35.243.129.210:80', '151.80.197.192:80', '62.196.125.168:39036', '190.196.72.130:32637', '185.129.217.130:8080', '91.240.74.69:33149', '118.173.232.98:39598', '80.48.35.181:8082', '138.94.28.234:50823', '123.201.20.246:32570', '93.187.183.144:8080', '212.231.80.64:52883', '83.221.195.249:8081', '86.57.219.184:23500', '103.126.114.42:8080', '203.142.76.171:8080', '112.78.38.165:63141', '31.220.183.217:53281', '180.183.21.145:8088', '187.191.20.5:61994', '85.111.25.113:32796', '5.202.46.28:80', '45.5.224.145:58796', '41.180.65.27:52881', '104.236.55.48:8080', '81.163.3.78:80', '5.202.151.100:80', '5.202.78.123:80', '37.235.31.170:80', '5.202.74.53:80', '109.125.136.98:80', '118.172.201.169:40782', '46.143.207.81:80', '37.114.202.109:80', '5.202.232.13:80', '5.202.67.177:80', '31.209.110.159:31959', '5.202.101.136:80', '5.202.158.69:80', '5.202.158.238:80', '5.202.148.116:80', '5.202.94.27:80', '5.202.212.131:80', '5.202.75.158:80', '5.202.47.31:80', '5.202.158.24:80', '5.202.77.106:80', '5.202.62.184:80', '5.202.157.166:80', '5.202.158.225:80', '5.202.158.234:80', '5.202.243.214:80', '5.202.158.132:80', '5.202.41.238:80', '37.235.31.215:80', '37.152.171.219:80', '5.202.38.118:80', '5.202.158.125:80', '5.202.68.221:80', '5.202.240.137:80', '5.202.45.73:80', '77.237.175.26:80', '5.202.101.194:80', '5.202.33.162:80', '93.110.92.42:80', '5.202.158.202:80', '5.202.101.163:80']

def crawl_offers():
    # proxy = random.choice(ALL_IPS)
    source_code  = requests.get(MAIN_URL)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    offer_section = soup.find("section", {"class": "offer-cards"})
    all_offers = offer_section.findAll("div", {"class":"ofr-card-wrap"})

    offer_list = list()

    for offer in all_offers:
        try:
            offer_id = offer['id']
            offer_type = offer.find("div", {"class": "offer-card-wrapper"})["data-offer-value"]

            spans = offer.findAll("span")[:2]
            amount, offer_value = spans[0].get_text(), spans[1].get_text()

            verified_on = offer.find("span", {"class":"coupon-verification"}).get_text()
            
            a_links = offer.find("div", {"class":"horizontal_online_content"}).findAll("a")
            product, description = a_links[0].get_text(), a_links[1].get_text()
            
            if str(offer_type) != "deal":
                offer_code = offer.find("div", {"class": "get-offer-code"})["data-offer-value"]
            else:
                offer_code = ""

            offer_list.append({"offer_id":offer_id, "amount":amount, "offer_value":offer_value, "verified_on": verified_on, "product":product, "description":description, "offer_code":offer_code})
        except Exception as e:
            print(e)

    return offer_list

# print((crawl_offers())[0])