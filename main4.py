from flask import *
from sql_manager1 import SQLManager

app = Flask(__name__)


database = [
    (0, "Гавайська піца", "Смачна піца з хрусткою скоринкою та соковитою начинкою, приготована зі свіжих інгредієнтів. Томатний соус, моцарела, ароматні спеції та свіжі овочі створюють ідеальний баланс смаків.", 150, "піца", "gavpizza.jpg"),
    (1, "Піца Три Сири", "Піца Три Сири - це витончена комбінація моцарели, чеддера і горгонзоли, що дарує багатий і насичений смак. Кожен шматочок цієї піци - справжня насолода для гурманів.", 170, "піца", "pizzachease.jpg"),
    (2, "Ананасовий фреш", "Свіжий ананасовий сік, виготовлений з найкращих тропічних ананасів. Має натуральний смак та приємну солодкість, ідеально підходить для втамування спраги у спекотні дні.", 40, "сік", "ananas.jpg"),
    (3, "Лимонад освіжаючий", "Освіжаючий лимонний сік з приємною кислинкою, виготовлений зі стиглих лимонів. Прекрасний вибір для тих, хто любить освіжитися та отримати заряд вітамінів.", 50, "сік", "lemon.jpg"),
    (4, "Апельсиновий мікс", "Натуральний апельсиновий сік з насиченим смаком свіжих апельсинів. Має яскравий аромат та солодкий смак, ідеально підходить для сніданку або будь-якого часу дня.", 30, "сік", "orange.jpg"),
    (5, "Вишуканий десерт", "Солодкий десерт, який тане в роті, приготований з ніжних вершків, шоколаду та свіжих фруктів. Кожен шматочок дарує справжню насолоду і робить ваш день кращим.", 65, "десерт", "desert1.jpg"),
    (6, "Шоколадний донат", "Пухкий пончик з ніжною начинкою, обсипаний цукровою пудрою. Ідеальний десерт для любителів солодкого, що приносить задоволення з першого укусу.", 40, "десерт", "donat.jfif"),
    (7, "Фанта Апельсинова", "Освіжаючий напій Fanta з апельсиновим смаком, який заряджає енергією і бадьорістю. Легко п'ється та чудово втамовує спрагу.", 25, "напої", "fanta.jpg"),
    (8, "Класична Кока-Кола", "Класичний напій Coca-Cola для справжніх поціновувачів. Має унікальний смак, який не сплутати ні з чим, і освіжає навіть у найспекотніший день.", 25, "напої", "kola.png"),
    (9, "Прохолодний Спрайт", "Легкий і освіжаючий напій Sprite, який дарує відчуття свіжості та прохолоди. Ідеальний для будь-якої нагоди, коли потрібен заряд бадьорості.", 25, "напої", "sprite1.jpg"),
    (10, "Чиста вода", "Чиста питна вода для здорового життя. Добре підходить для щоденного вживання, адже підтримує водний баланс і добре втамовує спрагу.", 25, "напої", "water1.webp"),
    (11, "Класичний бургер", "Соковитий бургер з хрусткою булочкою, ніжною котлетою, свіжими овочами та смачними соусами. Ідеальний вибір для швидкого і смачного перекусу в будь-який час дня.", 60, "фас-фут", "burger.jfif"),
    (12, "Кокосове Лате", "Ніжний та ароматний кокосовий латте. Поєднання еспресо та кокосового молока створює ідеальний баланс між насиченим кавовим смаком та солодкими нотками кокосу. Вишуканий напій, що дарує відчуття екзотики та блаженства з кожним ковтком.", 27, "Напої", "coclate.jpg"),
    (13, "Шаурма","Соковита шаурма з ніжним м'ясом, свіжими овочами та ароматними спеціями, загорнута у хрусткий лаваш. Ідеальний вибір для швидкого та смачного перекусу. Насолоджуйтесь справжнім смаком східної кухні з кожним шматочком.", 140, "закуски", "shaverma.jpg"),
    (14, "Картопля фрі", "Золотисті картопляні фрі з хрусткою скоринкою, посипані дрібкою солі. Ідеальний гарнір або самостійний перекус, який люблять усі.", 70, "фас-фут", "potato.png"),
    (15, "Курячі крильця", "Соковиті курячі крильця зі спеціями, приготовані до золотистої скоринки. Має насичений смак і аромат, що робить їх ідеальним вибором для м'ясних закусок.", 120, "фас-фут", "wings.jpg")
]

@app.route('/')
def index():
    return render_template('index1.html',items=database)
@app.route('/aboutus')
def about():
    return render_template('about us.html')
@app.route("/product/<item_id>")
def product_page(item_id):

    return render_template("product_page.html", item=database[int(item_id)])

app.run()