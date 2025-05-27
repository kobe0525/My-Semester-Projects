import random
from PIL import Image
import requests
from io import BytesIO

Majors = ["Petroleum Engineering","Mining And Mineral Engineering","Metallurgical Engineering","Naval Architecture And Marine Engineering","Chemical Engineering","Nuclear Engineering","Actuarial Science","Astronomy And Astrophysics","Mechanical Engineering","Electrical Engineering","Computer Engineering","Aerospace Engineering","Biomedical Engineering","Materials Science","Engineering Mechanics Physics And Science","Biological Engineering","Industrial And Manufacturing Engineering","General Engineering","Architectural Engineering","Court Reporting","Computer Science","Electrical Engineering Technology","Materials Engineering And Materials Science","Management Information Systems And Statistics","Civil Engineering","Construction Services","Operations Logistics And E-Commerce","Miscellaneous Engineering","Public Policy","Environmental Engineering","Engineering Technologies","Miscellaneous Fine Arts","Geological And Geophysical Engineering","Nursing","Finance","Economics","Business Economics","Industrial Production Technologies","Nuclear  Industrial Radiology  And Biological Technologies","Accounting","Mathematics","Computer And Information Systems","Physics","Medical Technologies Technicians","Information Sciences","Statistics And Decision Science","Applied Mathematics","Pharmacology","Oceanography","Engineering And Industrial Management","Medical Assisting Services","Mathematics And Computer Science","Computer Programming And Data Processing","Cognitive Science And Biopsychology","School Student Counseling","International Relations","General Business","Architecture","International Business","Pharmacy Pharmaceutical Sciences And Administration","Molecular Biology","Miscellaneous Business & Medical Administration","Agriculture Production And Management","General Agriculture","Miscellaneous Engineering Technologies","Mechanical Engineering Related Technologies","Genetics","Miscellaneous Social Sciences","United States History","Industrial And Organizational Psychology","Agricultural Economics","Physical Sciences","Military Technologies","Chemistry","Electrical  Mechanical  And Precision Technologies And Production","Business Management And Administration","Marketing And Marketing Research","Political Science And Government","Geography","Microbiology","Computer Administration Management And Security","Biochemical Sciences","Botany","Computer Networking And Telecommunications","Geology And Earth Science","Human Resources And Personnel Management","Pre-Law And Legal Studies","Miscellaneous Health Medical Professions","Public Administration","Geosciences","Social Psychology","Environmental Science","Communications","Criminal Justice And Fire Protection","Commercial Art And Graphic Design","Journalism","Multi-Disciplinary Or General Science","Advertising And Public Relations","Area Ethnic And Civilization Studies","Special Needs Education","Physiology","Criminology","Nutrition Sciences","Health And Medical Administrative Services","Communication Technologies","Transportation Sciences And Technologies","Natural Resources Management","Neuroscience","Multi/Interdisciplinary Studies","Atmospheric Sciences And Meteorology","Forestry","Soil Science","General Education","History","French German Latin And Other Common Foreign Language Studies","Intercultural And International Studies","Social Science Or History Teacher Education","Community And Public Health","Mathematics Teacher Education","Educational Administration And Supervision","Health And Medical Preparatory Programs","Miscellaneous Biology","Biology","Sociology","Mass Media","Treatment Therapy Professions","Hospitality Management","Language And Drama Education","Linguistics And Comparative Language And Literature","Miscellaneous Education","Interdisciplinary Social Sciences","Ecology","Secondary Teacher Education","General Medical And Health Services","Philosophy And Religious Studies","Art And Music Education","English Language And Literature","Elementary Education","Physical Fitness Parks Recreation And Leisure","Liberal Arts","Film Video And Photographic Arts","General Social Sciences","Plant Science And Agronomy","Science And Computer Teacher Education","Psychology","Music","Physical And Health Education Teaching","Art History And Criticism","Fine Arts","Family And Consumer Sciences","Social Work","Animal Sciences","Visual And Performing Arts","Teacher Education: Multiple Levels","Miscellaneous Psychology","Human Services And Community Organization","Humanities","Theology And Religious Vocations","Studio Arts","Cosmetology Services And Culinary Arts","Miscellaneous Agriculture","Anthropology And Archeology","Communication Disorders Sciences And Services","Early Childhood Education","Other Foreign Languages","Drama And Theater Arts","Composition And Rhetoric","Zoology","Educational Psychology","Clinical Psychology","Counseling Psychology","Library Science"]
Category =["Engineering","Engineering","Engineering","Engineering","Engineering","Engineering","Business","Physical Sciences","Engineering","Engineering","Engineering","Engineering","Engineering","Engineering","Engineering","Engineering","Engineering","Engineering","Engineering","Law & Public Policy","Computers & Mathematics","Engineering","Engineering","Business","Engineering","Industrial Arts & Consumer Services","Business","Engineering","Law & Public Policy","Engineering","Engineering","Arts","Engineering","Health","Business","Social Science","Business","Engineering","Physical Sciences","Business","Computers & Mathematics","Computers & Mathematics","Physical Sciences","Health","Computers & Mathematics","Computers & Mathematics","Computers & Mathematics","Biology & Life Science","Physical Sciences","Engineering","Health","Computers & Mathematics","Computers & Mathematics","Biology & Life Science","Education","Social Science","Business","Engineering","Business","Health","Biology & Life Science","Business","Agriculture & Natural Resources","Agriculture & Natural Resources","Engineering","Engineering","Biology & Life Science","Social Science","Humanities & Liberal Arts","Psychology & Social Work","Agriculture & Natural Resources","Physical Sciences","Industrial Arts & Consumer Services","Physical Sciences","Industrial Arts & Consumer Services","Business","Business","Social Science","Social Science","Biology & Life Science","Computers & Mathematics","Biology & Life Science","Biology & Life Science","Computers & Mathematics","Physical Sciences","Business","Law & Public Policy","Health","Law & Public Policy","Physical Sciences","Psychology & Social Work","Biology & Life Science","Communications & Journalism","Law & Public Policy","Arts","Communications & Journalism","Physical Sciences","Communications & Journalism","Humanities & Liberal Arts","Education","Biology & Life Science","Social Science","Health","Health","Computers & Mathematics","Industrial Arts & Consumer Services","Agriculture & Natural Resources","Biology & Life Science","Interdisciplinary","Physical Sciences","Agriculture & Natural Resources","Agriculture & Natural Resources","Education","Humanities & Liberal Arts","Humanities & Liberal Arts","Humanities & Liberal Arts","Education","Health","Education","Education","Health","Biology & Life Science","Biology & Life Science","Social Science","Communications & Journalism","Health","Business","Education","Humanities & Liberal Arts","Education","Social Science","Biology & Life Science","Education","Health","Humanities & Liberal Arts","Education","Humanities & Liberal Arts","Education","Industrial Arts & Consumer Services","Humanities & Liberal Arts","Arts","Social Science","Agriculture & Natural Resources","Education","Psychology & Social Work","Arts","Education","Humanities & Liberal Arts","Arts","Industrial Arts & Consumer Services","Psychology & Social Work","Agriculture & Natural Resources","Arts","Education","Psychology & Social Work","Psychology & Social Work","Humanities & Liberal Arts","Humanities & Liberal Arts","Arts","Industrial Arts & Consumer Services","Agriculture & Natural Resources","Humanities & Liberal Arts","Health","Education","Humanities & Liberal Arts","Arts","Humanities & Liberal Arts","Biology & Life Science","Psychology & Social Work","Psychology & Social Work","Psychology & Social Work","Education" ]
Median_Salaries = [110000,75000,73000,70000,65000,65000,62000,62000,60000,60000,60000,60000,60000,60000,58000,57100,57000,56000,54000,54000,53000,52000,52000,51000,50000,50000,50000,50000,50000,50000,50000,50000,50000,48000,47000,47000,46000,46000,46000,45000,45000,45000,45000,45000,45000,45000,45000,45000,44700,44000,42000,42000,41300,41000,41000,40100,40000,40000,40000,40000,40000,40000,40000,40000,40000,40000,40000,40000,40000,40000,40000,40000,40000,39000,38400,38000,38000,38000,38000,38000,37500,37400,37000,36400,36200,36000,36000,36000,36000,36000,36000,35600,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,35000,34000,34000,34000,34000,34000,34000,34000,34000,33500,33500,33400,33000,33000,33000,33000,33000,33000,33000,33000,33000,32500,32400,32200,32100,32000,32000,32000,32000,32000,32000,32000,32000,31500,31000,31000,31000,30500,30000,30000,30000,30000,30000,30000,30000,30000,29000,29000,29000,29000,28000,28000,28000,27500,27000,27000,26000,25000,25000,23400,22000]
Unemployment_rate =[0.018380527,0.117241379,0.024096386,0.050125313,0.061097712,0.177226407,0.095652174,0.021167415,0.057342278,0.059173845,0.065409275,0.065162085,0.09208386,0.023042836,0.006334343,0.087143069,0.042875544,0.059824231,0.061930783,0.011689692,0.063172771,0.087557114,0.027788805,0.058239614,0.070609574,0.060023041,0.047858703,0.074392523,0.128426299,0.093588575,0.055030385,0.089375,0.075038285,0.044862724,0.060686356,0.099092317,0.096448381,0.028308097,0.07154047,0.069749014,0.047277138,0.093460326,0.048224496,0.03698279,0.060741445,0.086273666,0.090823307,0.085531575,0.056994819,0.03365166,0.042506527,0,0.11398259,0.075236167,0.107579462,0.096798943,0.072861468,0.113331949,0.096175064,0.055520827,0.084361164,0.071982974,0.050030836,0.019642463,0.05253852,0.056357078,0.034117647,0.073079538,0.047179487,0.108786611,0.077249576,0.035353535,0,0.0539724,0.029479503,0.072218341,0.061215064,0.101174601,0.113458628,0.066775872,0.099723375,0.080531385,0,0.151849807,0.075448568,0.059569649,0.071965016,0.08141125,0.1594906,0.024373731,0.029649596,0.078584681,0.075176976,0.082452199,0.096797577,0.069176442,0.055806815,0.067960766,0.063429289,0.041507819,0.0691628,0.097243919,0.068700676,0.089626262,0.119511469,0.072724524,0.066619195,0.048481675,0.070860927,0.022228555,0.096725743,0,0.057359929,0.095666912,0.075566386,0.083633531,0.054082941,0.112144387,0.016202835,0,0.069779712,0.058545455,0.070724732,0.084951001,0.089836827,0.059821207,0.061169193,0.050306435,0.10443571,0.059211951,0.092305816,0.054475193,0.05222898,0.082101621,0.096051684,0.038637747,0.08772359,0.046585715,0.051467273,0.078267592,0.10577224,0.103454715,0.045454545,0.047263682,0.083810867,0.075959674,0.074667496,0.060298284,0.084186296,0.067128194,0.06882792,0.050862499,0.102197419,0.03654583,0.05190783,0.037819026,0.068584071,0.062628297,0.089552239,0.055676856,0.059766764,0.102791571,0.047584,0.040104981,0.107115726,0.07754113,0.081742207,0.04632028,0.065112187,0.149048198,0.053620646,0.104945718]
filtered_list = []
empty_list = []


def about(major):
  x = Majors.index(major)
  print(Category[x])
  print("Median salarie is $" + str(Median_Salaries[x]) )
  print("The unemployment rate is " + str(Unemployment_rate[x]) + "%")

def salary(Salaries):
  for i in range(len(Median_Salaries)):
          if Median_Salaries[i] >= int(Salaries):
            filtered_list.append(Majors[i])
  if len(filtered_list)== 0:
      print("Sorry no jobs fits this salary criteria")
  else :
      random_item=random.choice(filtered_list)
      print("I recomend you major in " + random_item )

def unemployment(rate):
  for i in range(len(Unemployment_rate)):
          if Unemployment_rate[i] <= float(rate):
            empty_list.append(Majors[i])
  if len(empty_list)==0:
      print("Sorry no jobs fits this unemployment rate criteria")
  else :
      random_item=random.choice(empty_list)
      print("I recomend you major in " + random_item )

def find_catogory(catogory):
  for i in range(len(Category)):
          if Category[i] == catogory:
            empty_list.append(Majors[i])
  random_item=random.choice(empty_list)
  print("I recomend you major in " + random_item )\

def find_major():
    print("Welcome to Find The College Major For You! ")
    while 1==1:

          option = int(input(print("Please select an option by entering the corresponding number 1.)find major based on salary. 2.)Find major based on unemployment rates. 3.)Find major based on its category 4.)About major 5.)Off ")))
          if option == 1 :
                filtered_list.clear()
                empty_list.clear()
                salary(input(print("What is the salry you would like? Please enter number without comma or dollar sign. (Ranges from $110,000 through $22,000)")))
          if option == 2 :
                filtered_list.clear()
                empty_list.clear()
                unemployment(input(print("Please enter a decimal number between 0 and 0.1594906, where 0 represents 0 percent unemployment and 0.1594906 represents 15.95 percent unemployment.")))
          if option == 3 :
                filtered_list.clear()
                empty_list.clear()
                find_catogory(input(print("""What category would you like your major in?
		1.	Engineering
		2.	Business
		3.	Physical Sciences
		4.	Computers & Mathematics
		5.	Health
		6.	Law & Public Policy
		7.	Social Science
		8.	Arts
		9.	Biology & Life Science
		10.	Humanities & Liberal Arts
		11.	Agriculture & Natural Resources
		12.	Industrial Arts & Consumer Services
		13.	Psychology & Social Work""")))
          if option == 4 :
              filtered_list.clear()
              empty_list.clear()
              about(input(print("What major would you like to know more about?")))
          if option == 5 :
               print("Hope I helped finding the college major for you!")
               break


find_major()



#The data about all college majors.  source:jonthegeek. 2018. Accessed via https://github.com/rfordatascience/tidytuesday/tree/main/data/2018/2018-10-16

