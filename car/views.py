# Create your views here.
from car.models import Car_MB
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from bs4 import BeautifulSoup 
import urllib
import re







def home (request):
	

	return render_to_response('index.html', {}, context_instance=RequestContext(request))

def car_data (request):

	my_brand = []
	
	

	url = urllib.urlopen("http://www.car-part.com/")
	soup = BeautifulSoup(url)

	brand = soup.find("select", {"id" : "model"})

	
	# for child in brand.contents:
	for i in range (2, len(brand)):

		# my_brand brand.contents[i].text.split(' ', 1)
		temp  = brand.contents[i].text.split(' ', 1)
		my_brand.append (temp)

	for mys in my_brand:
		try:
			brand_model = Car_MB (car_brand = mys[0], car_model = mys[1])
			
			
		except IndexError, e:
			brand_model = Car_MB (car_brand = mys[0], car_model = " ")
			print e
			
		brand_model.save()
		





	return render_to_response('car_data.html', {'brand':my_brand}, context_instance=RequestContext(request))

	# <select data-placeholder="Select a Make" style="width: 210px; display: none;" class="cf_dropdown2 form-select chzn-done" id="clone-make" name="clone-make">
	# <option value=""></option>
	# <option value="">Any Make</option>
	# 		<option value="ACURA">ACURA</option><option value="ALFA ROMEO">ALFA ROMEO</option><option value="AMERICAN MOTORS">AMERICAN MOTORS</option><option value="APRILIA">APRILIA</option><option value="ARCT">ARCT</option><option value="ARO">ARO</option><option value="ASTON MARTIN">ASTON MARTIN</option><option value="AUDI">AUDI</option><option value="AUSTIN">AUSTIN</option><option value="BED">BED</option><option value="BENTLEY">BENTLEY</option><option value="BMW">BMW</option><option value="BUICK">BUICK</option><option value="CADILLAC">CADILLAC</option><option value="CAN-AM">CAN-AM</option><option value="CAPI">CAPI</option><option value="CHEVROLET">CHEVROLET</option><option value="CHRYSLER">CHRYSLER</option><option value="CODA">CODA</option><option value="CORD">CORD</option><option value="DAEWOO">DAEWOO</option><option value="DAIHATSU">DAIHATSU</option><option value="DATSUN">DATSUN</option><option value="DCX SPRINTER">DCX SPRINTER</option><option value="DODGE">DODGE</option><option value="DUCATI">DUCATI</option><option value="EAGLE">EAGLE</option><option value="ELGI">ELGI</option><option value="FERRARI">FERRARI</option><option value="FIAT">FIAT</option><option value="FISKER">FISKER</option><option value="FORD">FORD</option><option value="FREIGHTLINER">FREIGHTLINER</option><option value="GEM">GEM</option><option value="GEO">GEO</option><option value="GMC">GMC</option><option value="GO-4">GO-4</option><option value="HARLEY-DAVIDSON">HARLEY-DAVIDSON</option><option value="HOME">HOME</option><option value="HONDA">HONDA</option><option value="HORT">HORT</option><option value="HUMMER">HUMMER</option><option value="HYUNDAI">HYUNDAI</option><option value="INFINITI">INFINITI</option><option value="INNOCENTI">INNOCENTI</option><option value="INTERNATIONAL">INTERNATIONAL</option><option value="ISUZU">ISUZU</option><option value="JAGUAR">JAGUAR</option><option value="JEEP">JEEP</option><option value="JENS">JENS</option><option value="JOHN">JOHN</option><option value="JOHN DEERE">JOHN DEERE</option><option value="KAND">KAND</option><option value="KAWASAKI">KAWASAKI</option><option value="KEYS">KEYS</option><option value="KIA">KIA</option><option value="KTM">KTM</option><option value="KYMCO">KYMCO</option><option value="LAMBORGHINI">LAMBORGHINI</option><option value="LAND ROVER">LAND ROVER</option><option value="LEXUS">LEXUS</option><option value="LINCOLN">LINCOLN</option><option value="LOTUS">LOTUS</option><option value="MACK">MACK</option><option value="MAGN">MAGN</option><option value="MASERATI">MASERATI</option><option value="MAXU">MAXU</option><option value="MAZDA">MAZDA</option><option value="MB">MB</option><option value="MERCEDES-BENZ">MERCEDES-BENZ</option><option value="MERCURY">MERCURY</option><option value="MG">MG</option><option value="MGB">MGB</option><option value="MILE">MILE</option><option value="MINI">MINI</option><option value="MITSUBISHI">MITSUBISHI</option><option value="MITSUBISHI FUSO">MITSUBISHI FUSO</option><option value="NISSAN">NISSAN</option><option value="NISSAN DIESEL">NISSAN DIESEL</option><option value="NOBL">NOBL</option><option value="OLDSMOBILE">OLDSMOBILE</option><option value="OPEL">OPEL</option><option value="OTHE">OTHE</option><option value="OTHR">OTHR</option><option value="PACE">PACE</option><option value="PIAGGIO">PIAGGIO</option><option value="PLYMOUTH">PLYMOUTH</option><option value="PONTIAC">PONTIAC</option><option value="PORSCHE">PORSCHE</option><option value="RAM">RAM</option><option value="ROLL">ROLL</option><option value="ROLLS-ROYCE">ROLLS-ROYCE</option><option value="ROLS">ROLS</option><option value="SAAB">SAAB</option><option value="SATURN">SATURN</option><option value="SCION">SCION</option><option value="SMART">SMART</option><option value="SPCN">SPCN</option><option value="STEI">STEI</option><option value="STEL">STEL</option><option value="STERLING">STERLING</option><option value="STUDEBAKER">STUDEBAKER</option><option value="SUBARU">SUBARU</option><option value="SUZUKI">SUZUKI</option><option value="TESLA">TESLA</option><option value="TOYO">TOYO</option><option value="TOYOTA">TOYOTA</option><option value="TRIUMPH">TRIUMPH</option><option value="UTIL">UTIL</option><option value="VOLKSWAGEN">VOLKSWAGEN</option><option value="VOLVO">VOLVO</option><option value="VPG">VPG</option><option value="WELL">WELL</option><option value="WHITEGMC">WHITEGMC</option><option value="YAMAHA">YAMAHA</option><option value="YUGO">YUGO</option><option value="ZAP">ZAP</option></select>