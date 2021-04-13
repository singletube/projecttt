import sqlite3

connection = sqlite3.connect('inform.db')
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS OVEN
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute("""INSERT INTO OVEN
   VALUES('Овен открывает новый зодиакальный цикл,
    относится к стихии Огня, обладает особенной
     харизмой (качеством) первооткрывателя,
      инициативой и целеустремленностью. 
      Даже обладающие спокойным темпераментом,
       Овны никогда не забывают про свои цели и,
        как правило, рано или поздно достигают желаемого.
         Инициатива и активность представителей этого знака
          позволяет находить новые задачи,
           которые Овен ставит перед своими последователями.',
           
            '',
            
             'Целеустремленность Овна также обеспечивает его энергией ненадолго.
              Быстрая потеря интереса к начатому,
               потребность в новых впечатлениях часто толкает
                Овна к рискованным занятиям и профессиям.
                 В общении прямолинейны, иногда даже слишком,
                  но искренни как дети. Эта искренность часто граничит 
                  с бестактностью, может обернуться грубостью.
                   Но сами Овны долго не могут держать обиду,
                    резко рвут отношения, не сожалея о прошлом.',
                    
                      'В вопросе здоровья Овнам важно не перегружать нервную
                       систему, хорошо спать, следить за состоянием сосудов
                        и работой почек, а также избегать травм головы.
                         Непоседливый Овен тратит много энергии и нуждается
                          в калорийной пище, содержащей достаточно фосфора
                           — основного звена в энергетическом балансе организма.
                            Овен обычно не обращает внимания на еду — ест когда
                             угодно и что попало. Самое полезное, но трудновыполнимое
                              — это питаться регулярно примерно в одно и то же время.',
                      
                      'Овен – прирожденный исследователь.
                       Он обладает множеством скрытых талантов,
                        что позволяет ему в дальнейшем стать хорошим руководителем.
                         Овен достаточно легко переживает сложные времена,
                          включая позитивный настрой и мотивируя окружающих на успех.',
                          
                          'Овен сильно подвержен пагубному влиянию:
                           он может и ругаться, как сапожник, и злоупотреблять
                            алкоголем. В таком состоянии он рискует
                             растерять заложенный в него потенциал и использовать
                              свои сильные стороны во вред самому себе.',
                              
                              'Стрелец Близнецы Водолей',
                              
                              'Рак Весы Козерог',
                              
                              'администратор в гостиничном и туристическом секторе,
                      инженер, адвокат, прокурор, правозащитник, хирург.',
                      
                      '3',
                    
                    'Все будет хорошо, может не с нами и не в этой жизни')""")


cursor.execute('''CREATE TABLE IF NOT EXISTS TELEZ
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute("""INSERT INTO TELEZ
   VALUES('Телец - основательный, музыкальный, практичный
Фиксированный знак стихии земли, созидатель и гурман,
 Телец воплощает собой принцип любви к жизни и ее благам,
  а также имеет качества упорства и практичности.
   Телец умеет и любит работать, терпеливо создает себе комфортные
    условия для жизни. Способен долго и терпеливо ждать созревания
     подходящих условий. Терпение Тельца удивительно,
      ему трудно учиться чему-то новому и приспосабливаться
       к незнакомым условиям.
Очень восприимчив ко всему прекрасному,
 обладает сильной интуицией, склонен анализировать ситуацию,
  прежде, чем совершать поступки. Дар Тельца — воплощать
   красивые мечты в реальность.',
   
   '',
   
   'Телец несколько пассивный знак,
    который скорее ждет подходящего случая,
     чем активно охотится за возможностями.
      Способен долго и тяжело работать,
       самый трудолюбивый знак зодиака,
        если найдет подходящий способ самовыражения.
         Любит красивые вещи, все оценивает по высоким критериям,
          даже поступки может счесть некрасивыми.
           Ярко выраженная практичность и житейская мудрость,
            неторопливость делает Тельца основательным домохозяином.',
            
            'Уязвимое место — горло, шея.
             Часто простужаются, подвержены нервным срывам 
             из-за перегрузки. Склонен к полноте из-за переедания,
              подвержен заболеваниям щитовидной железы, нарушению
               гормонального баланса, когда находится в агрессивной среде.
                Необходимо медленно пережевывать пищу.',
            
   
   'Тельцы обладают невероятным потенциалом и силой,
    хотя производят впечатление скромных и закрытых личностей.
     Такие люди легко находят друзей в различных сферах
      деятельности – во многом благодаря хорошему чувству юмора.',
      
      'Обратная сторона медали – отказ от ответственности,
       нежелание признавать собственные ошибки.
        Тельцы склонны игнорировать проблемы и искать
         максимально легкие пути ее решения.',
         
         'Рыба Рак Скорпион',
         
         'Водолей Близнецы Стрелец',
         
         'финансист, геолог,
          ювелир, флорист, менеджер по продажам дорогих товаров',
          
          '6',
         
         'Все будет хорошо, может не с нами и не в этой жизни')""")

cursor.execute('''CREATE TABLE IF NOT EXISTS BLIZNEZI
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute("""INSERT INTO BLIZNEZI
   VALUES('Знак подвижного креста стихии воздуха.
    Близнецы обладают сильным характером, энергичны,
     независимы и общительны. Коммуникабельны,
      с веселым характером и темпераментным любопытством.
       Близнецы легко устанавливают связи со множеством
        разноплановых людей. Интересные эрудированные собеседники,
         темпераментные и неутомимые, Близнецы живут активной
          и насыщенной жизнью, легко приспосабливаются к любой
           обстановке. Обеспечивают связи и потоки
            информации между людьми.',
            
            '',
            
            'Близнецы — интеллектуально одаренный знак.
             Часто они легко осваивают иностранные языки,
              талантливы в литературе и актерской профессии.
               Переменчивы во мнении, могут менять свое отношение
                несколько раз в день. Модники, следуют самым 
                новейшим направлениям в обществе. Общительные
                 и бесцеремонные выдумщики. С ними никогда
                  не бывает скучно. Для Близнецов жизненно
                   необходимо постоянно заниматься каким-то делом,
                    они любят быть в центре внимания',
                    
                    'Близнецы выносливы и крепки,
                     подвержены эмоциональным перепадам. 
                     Как рутина, так и переутомление от
                      впечатлений приводят к болезням.
                       Им жизненно необходимо совмещать
                        процесс обдумывания и сортировки
                         информации с физической нагрузкой,
                          например долгие пешие прогулки на 
                          свежем воздухе, велосипедная езда, йога.
                           Близнецы часто простужаются, подвержены
                            аллергиям. Кофе и вредные привычки
                             усиливают возбуждение и беспокойство.
                              Для здоровья важно высыпаться',
                                   
                                   'Близнецы легко приспосабливаются.
                                    Они могут найти свое место в любой сфере
                                     – будь то шоу-бизнес или агропромышленность.
                                      Они достаточно умны и находчивы,
                                       с легкостью берутся за новое дело,
                                        даже когда не уверены в успехе.
                                         Близнецы всегда придут на помощь,
                                          даже если перед этим часами жаловались
                                           на жизнь и возмущались.',
                                           
                                           'Когда Близнецы теряют интерес,
                                            они крайне рассеяны. Кроме того,
                                             они редко прикладывают усилия,
                                              чтобы изменить себя.
                                               Чаще всего они ищут корень проблемы в других людях.
                                                Их общительность зачастую не знает
                                                 границ и переходит в болтливость,
                                                  так что доверять им сокровенные
                                                   секреты – не самая лучшая затея.',
                                                   
                                                   'Овен Лев Стрелец',
                                                   
                                                   'Телец Дева Козерог Рыбы Скорпион Рак',
                                                   
                                                   'актер, писатель, оратор, лектор,
                               психолог, продавец-консультант,
                                проповедник, теолог, журналист
                                 (корреспондент), специалист по связям
                                  с общественностью (PR), пресс-секретарь,
                                   политик, ресторанный или театральный критик.',
                                   
                                   '4',
                                   
                                   'Все будет хорошо, может не с нами и не в этой жизни')""")

cursor.execute('''CREATE TABLE IF NOT EXISTS RAK
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute("""INSERT INTO RAK
   VALUES('Знак водной стихии находится
    под покровительством ночного светила.
     Управление Луны влияет на характер
      представителей этого знака, делая 
      их ранимыми и чувствительными людьми.
       Луна и водная стихия знака дают 
       Раку способность к эмпатии, возможность 
       мгновенно угадывать мысли и чаяния других 
       людей. Это решительные и благородные люди,
        часто патриоты. Но если жизнь Рака
         была полна лишений и несправедливости
          с детства, то обладают коварством
           и харизмой гангстера.
Влияют на других людей, могут
 подчинить себе ради достижения 
общей цели или выживания. Жесткие
 и проницательные руководители.',
 
 '',
 
 'Рак — самый эмоциональный знак среди всего зодиака.
  Но сам не любит делиться личными эмоциями.
   Чувства и настроение окружающих Рак
    понимает мгновенно, но редко откровенен.
     Проблема с выражением своих чувств связана
      с защитными психическими механизмами.
       С ранних лет Рак выстраивает личную систему
        защиты от нечаянного проникновения в душу,
         обрастает стереотипами и предрассудками.
          Очень привязан к семье, особенно к матери.',
 
 'Сдерживание эмоций и подавление агрессии
  часто приводит к нервным расстройствам,
   истощению, болезням желудочно-кишечного тракта.
    Переедание, любовь к сладкому, малоподвижный
     образ жизни — главный враги здоровья Рака 
     наряду с нервным перенапряжением.
      Часто трудоголики, Раки забывают об отдыхе,
       и недостаток сна приводит их к хронической
        усталости. Им необходим режим питания и сна,
         позитивный заряд общения с избранным кругом людей,
          медитация для успокоения ума.',
          
          'Раки всегда стараются преуспеть во
           всем том, что им приходится делать.
            Они остроумны и прикладывают все усилия,
             чтобы защитить всех нуждающихся.
              Иногда такие люди выглядят достаточно
               холодными, но на самом деле они
                очень восприимчивы и часто переживают
                 из-за неудач.',
          
          'Раки – прекрасные ораторы, им легко убеждать
           других людей, но сами они не хотят следовать
            собственным записям. Они очень руководить
             окружающими людьми и поэтому часто лезут
              в чужие дела, даже если в этом нет
               никакой необходимости. ',
               
               'Телец Дева Козерог',
               
               'Овен Лев Стрелец Близнецы Весы Водолей',
               
               'актер, писатель, оратор, лектор, 
               психолог, продавец-консультант, 
               проповедник, теолог, журналист (корреспондент), 
               специалист по связям с общественностью (PR),
                пресс-секретарь, политик, 
                ресторанный или театральный критик.',
               
               '2',
               
               'Все будет хорошо, может не с нами и не в этой жизни')""")


cursor.execute('''CREATE TABLE IF NOT EXISTS LEB
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute("""INSERT INTO LEB
   VALUES('Фиксированный знак стихии огня, 
   Лев обладает даром созидания и настойчивостью в 
   достижении своих целей. Это деятельный человек,
    стремящийся к успеху и популярности. 
    Сильная, чувствительная и любящая натура,
     часто попадает под влияние эмоций и чувств.
      Лев великодушен, решителен и храбр.
      Самообладание и амбициозность являются сильными чертами
       этого знака. Не равнодушен к вниманию, лести и роскоши',
       
       '',
       
       'Не переносит критику, горделив и эгоистичен.
        Часто переоценивает свои возможности, не пунктуален,
         обидчив и ревнив. Долго помнит оскорбления.
          Из-за тщеславия может ошибаться в людях,
           попадает в авантюры, азартен.
            Может жить за чужой счет.
             Часто окружен фальшивыми друзьями,
              которые пользуются энергией Льва в корыстных целях.
               Не выносит рутину и расписания,
                часто ко времени проявляет независимость,
                 бывает груб и резок.',
                 
                 'В теле человека Лев символически представляет сердце
                  и позвоночник. Чрезмерность в еде и удовольствиях,
                   малоподвижный образ жизни губительны для
                    сердечной деятельности.
                     Активный образ жизни, диета,
                      богатая магнием и калием,
                       профилактическое очищение сосудов
                        и правильный режим дня помогут надолго
                         сохранить долголетие. Необходимо
                          беречь нервную систему, достаточно
                           спать, чередовать физические нагрузки
                            с отдыхом.',
                            
                            ' Львы – сильные личности, но кричать
                             на каждом углу о своих достоинствах
                              они не будут. Они всегда заботятся
                               о других людях, очень дружелюбны и любят действовать в команде.',
                               
                               'Львы очень легко заводятся,
                                да так сильно, что порой не слышат
                                 своих собеседников. А еще если они в чем-то уверены,
                                  переубедить их невозможно! Проще
                                    договориться с фонарным столбом,
                                     чтобы он подвинулся :) Шутка.',
                                     
                                     'Близнецы Весы Водолеи',
                                     
                                     'Телец Дева Козерог Рыбы Рак Скорпион', 
                                     
                                     'финансист, визажист, парикмахер,
                                      телеведущий, журналист развлекательного жанра,
                                       литературный деятель (малые формы).',
                                       
                                       '1',
                                       
                                         'Все будет хорошо, может не с нами и не в этой жизни')""")

cursor.execute('''CREATE TABLE IF NOT EXISTS DEVA
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS VECI
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS SKORPION
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS CTRELEZ
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS KOZA
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS VODOLEI
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS RIBA
              (zz TEXT, asz TEXT, otl TEXT, pred TEXT,
              plus TEXT, minus TEXT, sov TEXT, nesov TEXT,
              delo TEXT, chislo TEXT, prognos TEXT)''')
connection.commit()
connection.close()
