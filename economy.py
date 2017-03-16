dodatoc_b = {'A': ['Обладнання для виробництва продукції А', 515000],
			 'Б': ['Обладнання для виробництва продукції Б', 525000],
			 'В': ['Обладнання для виробництва продукції В', 535000],
			 'Г': ['Обладнання для виробництва продукції Г', 545000],
			 'Д': ['Обладнання для виробництва продукції Д', 555000],
			 'Е': ['Обладнання для виробництва продукції Е', 565000],
			 'Є': ['Обладнання для виробництва продукції Є', 575000],
			 'Ж': ['Обладнання для виробництва продукції Ж', 585000],
			 'З': ['Обладнання для виробництва продукції З', 595000],
			 'И': ['Обладнання для виробництва продукції И', 605000],
			 'І': ['Обладнання для виробництва продукції І', 615000],
			 'Ї': ['Обладнання для виробництва продукції Ї', 625000],
			 'К': ['Обладнання для виробництва продукції К', 635000],
			 'Л': ['Обладнання для виробництва продукції Л', 645000],
			 'М': ['Обладнання для виробництва продукції М', 655000],
			 'Н': ['Обладнання для виробництва продукції Н', 675000],
			 'О': ['Обладнання для виробництва продукції О', 685000],
			 'П': ['Обладнання для виробництва продукції П', 695000],
			 'Р': ['Обладнання для виробництва продукції Р', 705000],
			 'С': ['Обладнання для виробництва продукції С', 715000],
			 'Т': ['Обладнання для виробництва продукції Т', 725000],
			 'У': ['Обладнання для виробництва продукції У', 735000],
			 'Ф': ['Обладнання для виробництва продукції Ф', 745000],
			 'Х': ['Обладнання для виробництва продукції Х', 755000],
			 'Ц': ['Обладнання для виробництва продукції Ц', 765000],
			 'Ч': ['Обладнання для виробництва продукції Ч', 775000],
			 'Ш': ['Обладнання для виробництва продукції Ш', 785000],
			 'Щ': ['Обладнання для виробництва продукції Щ', 795000],
			 'Ю': ['Обладнання для виробництва продукції Ю', 805000],
			 'Я': ['Обладнання для виробництва продукції Я', 815000]}

dodatoc_v = { 0 : [115000, 550000],
			    1 : [125000, 600000],
			    2 : [135000, 650000],
			    3 : [145000, 700000],
			    4 : [155000, 750000],
			    5 : [165000, 800000],
			    6 : [175000, 850000],
			    7 : [185000, 900000],
			    8 : [195000, 950000],
			    9 : [205000, 1000000]}

dodatoc_g = [3000, 2400, 2300, 1500]

dodatoc_d = { 0 : [3, 2, 2, 40, 47],
			    1 : [3, 3, 2, 39, 47],
			    2 : [3, 2, 3, 38, 46],
			    3 : [3, 1, 2, 37, 43],
			    4 : [3, 2, 3, 36, 44],
			    5 : [3, 3, 2, 35, 43],
			    6 : [3, 2, 3, 34, 42],
			    7 : [3, 3, 2, 33, 41],
			    8 : [3, 2, 3, 32, 40],
			    9 : [3, 3, 2, 31, 39]}

dodatoc_e = { 0 : [0.20],
			    1 : [0.22],
			    2 : [0.25],
			    3 : [0.27],
			    4 : [0.30],
			    5 : [0.31],
			    6 : [0.33],
			    7 : [0.35],
			    8 : [0.37],
			    9 : [0.40]}

per_dodatoc_b = input()
per_dodatoc_v = int(input())
per_dodatoc_d = int(input())
per_dodatoc_e = int(input())
print("""<p>Пропонується придбання обладнання вартістю {} грн. Для визначення
доцільності такого придбання розраховуються показники, що характеризують
ефективність діяльності підприємства в першому році роботи обладнання:
валовий, чистий прибуток та чиста рентабельність.</p>""".format(dodatoc_b.get(per_dodatoc_b)[1]))

print("<h1>1 Обсяг виробництва та обладнання</h1>")
print("<p>Назва обладнання, його вартість та річний обсяг виробництва</p>")
print("""<table style="border-collapse: collapse;">
			<tr>
				<td style=" border: 1px solid #000; padding: 5px">Назва обладнання</td>
				<td style=" border: 1px solid #000; padding: 5px">Варт. грн</td>
				<td style=" border: 1px solid #000;">Р. обсяг виробництва</td>
			</tr>
			<tr>
				<td style=" border: 1px solid #000; padding: 5px">{}</td>
				<td style=" border: 1px solid #000; padding: 5px">{}</td>
				<td style=" border: 1px solid #000; padding: 5px">{}</td>
			</tr>
		</table>""".format(dodatoc_b.get(per_dodatoc_b)[0],
							dodatoc_b.get(per_dodatoc_b)[1],
							dodatoc_v.get(per_dodatoc_v)[0]))

print("<h1>2 Персонал і посадові оклади</h1>")
print("<p>Склад виробничого персоналу підприємства та посадові оклади</p>")
print("""<table style="border-collapse: collapse;">
			<tr>
				<td style=" border: 1px solid #000; padding: 5px">Посада</td>
				<td style=" border: 1px solid #000; padding: 5px">Кількість, чол.</td>
				<td style=" border: 1px solid #000;">Посадовий оклад, грн.</td>
			</tr>
			<tr>
				<td style=" border: 1px solid #000; padding: 5px">Керівники</td>
				<td style=" border: 1px solid #000; padding: 5px">{}</td>
				<td style=" border: 1px solid #000; padding: 5px">3000</td>
			</tr>
			<tr>
				<td style=" border: 1px solid #000; padding: 5px">Спеціалісти</td>
				<td style=" border: 1px solid #000; padding: 5px">{}</td>
				<td style=" border: 1px solid #000;">2400</td>
			</tr>
			<tr>
				<td style=" border: 1px solid #000; padding: 5px">Службовці</td>
				<td style=" border: 1px solid #000; padding: 5px">{}</td>
				<td style=" border: 1px solid #000; padding: 5px">2300</td>
			</tr>
			<tr>
				<td style=" border: 1px solid #000; padding: 5px">Робітники</td>
				<td style=" border: 1px solid #000; padding: 5px">{}</td>
				<td style=" border: 1px solid #000;">1500</td>
			</tr>
			<tr>
				<td style=" border: 1px solid #000; padding: 5px">Всього</td>
				<td style=" border: 1px solid #000; padding: 5px">{}</td>
				<td style=" border: 1px solid #000;">-</td>
			</tr>
		</table>""".format(dodatoc_d.get(per_dodatoc_d)[0],
							dodatoc_d.get(per_dodatoc_d)[1],
							dodatoc_d.get(per_dodatoc_d)[2],
							dodatoc_d.get(per_dodatoc_d)[3],
							dodatoc_d.get(per_dodatoc_d)[4]))

print("<h1>3 Визначення витрат</h1>")
print("<p>Собівартість – це економічний показник, що включає витрати на спожиті засоби виробництва і на оплату праці. </p>")
print("<p>Склад собівартості за економічними елементами витрат (кошторис витрат на виробництво) представлений нижче: </p>")
print(""" <ol>
				<li>Матеріальні витрати.</li>
				<li>Витрати на оплату праці.</li>
				<li>Відрахування з фонду оплати праці.</li>
				<li>Амортизаційні відрахування.</li>
				<li>Інші витрати.</li>
			</ol>""")

print("<p>Витрати на оплату праці: </p>")
v_OP = 12 * (dodatoc_d.get(per_dodatoc_d)[0]*dodatoc_g[0]+dodatoc_d.get(per_dodatoc_d)[1]*dodatoc_g[1]+dodatoc_d.get(per_dodatoc_d)[2]*dodatoc_g[2]+dodatoc_d.get(per_dodatoc_d)[3]*dodatoc_g[3])
print("В_ОП = 12 * ({}*{}+{}*{}+{}*{}+{}*{}) = {} (грн)".format(dodatoc_d.get(per_dodatoc_d)[0], dodatoc_g[0],
																	dodatoc_d.get(per_dodatoc_d)[1],dodatoc_g[1],
																	dodatoc_d.get(per_dodatoc_d)[2],dodatoc_g[2],
																	dodatoc_d.get(per_dodatoc_d)[3],dodatoc_g[3], v_OP))

print("<p>Нарахування на фонд оплати праці: </p>")
v_n_FOP = (22 * v_OP)/100
print("В_ФОП = (22 * {})/100 = {} (грн)".format(v_OP, v_n_FOP))

print("<p>У контрольній роботі амортизація обладнання нараховується із застосуванням прямолінійного методу: </p>")
v_A = (dodatoc_b.get(per_dodatoc_b)[1]) / 10
print("В_A = {} / 10 = {} (грн)".format(dodatoc_b.get(per_dodatoc_b)[1], v_A))

print("<p>Інші витрати: </p>")
v_IN = 0.1 * (v_OP+v_n_FOP)
print("В_IN = 0.1 * ({} + {}) = {} (грн)".format(v_OP, v_n_FOP, v_IN))


C = dodatoc_v.get(per_dodatoc_v)[1] + v_OP + v_n_FOP + v_A + v_IN
print("<p>С = {}+{}+{}+{}+{} = {} (грн)</p>".format(dodatoc_v.get(per_dodatoc_v)[1],
													 v_OP, v_n_FOP, v_A, v_IN, C))