import streamlit as st
import graphviz

st.set_page_config("Registrator offisi xizmati yo'riqnomlari",'®️','wide','collapsed')
st.write("### :green[Bo‘limning maqsadi:]  universitetning asosiy xizmatlarini talabalarga bir joydan turib tezkor, samarali va shaffof tarzda amalga oshirishdan iborat.")
with st.expander(":rainbow[“Registrator ofisi” haqida]"):
    st.write('''
             **O‘zbekiston Respublikasi Prezidentining** :blue[**2021-yil 24-dekabr**]dagi “Davlat oliy ta’lim muassasalarining akademik va tashkiliy-boshqaruv mustaqilligini ta’minlash bo‘yicha qo‘shimcha chora-tadbirlar to‘g‘risida”gi PQ-60-son va “Davlat oliy ta’lim muassasalariga moliyaviy mustaqillik berish chora-tadbirlari to‘g‘risida”gi _PQ-61-son_ qarorlari, O‘zbekiston Respublikasi Vazirlar Mahkamasining :blue[**2020-yil 31-dekabr**]dagi 824-son qarori bilan tasdiqlangan “Oliy ta’lim muassasalarida o‘quv jarayoniga kredit-modul tizimini joriy etish tartibi to‘g‘risida”gi Nizom, O‘zbekiston Respublikasi Prezidenti :rainbow[Sh.Mirziyoyev] rahbarligida :blue[**2024-yil 20-iyun**]da kengaytirilgan tarzda o‘tkazilgan videoselektor yig‘ilishining 32 - son bayoni va Ta’lim sohasidagi loyihalar markazi” loyiha ofisi va O‘zbekiston Respublikasi Oliy ta’lim, fan va innovatsiyalar vazirligining :blue[**2024-yil 9-iyul**]dagi “Oliy ta’lim tashkilotlarida :green[**“Registrator ofisi”**]ni tashkil etish to‘g‘risida”gi 24-son qo‘shma qaroriga asosan tashkil etilgan.
    ''')
    graph = graphviz.Digraph()
    graph.attr('node', shape='box', size='8,3', color='lightgreen', style='outline', fontcolor='blue')
    
    graph.edge("“Registrator ofisi” boshlig‘i", "Xizmat koʻrsatish (front office) boʻlimi boshligʻi")
    graph.edge("“Registrator ofisi” boshlig‘i", "Maʼlumotlar bazasi (back office) boʻlimi boshligʻi")
    
    graph.edge("Xizmat koʻrsatish (front office) boʻlimi boshligʻi", "Talabalarga xizmat koʻrsatish sektori")
    graph.edge("Talabalarga xizmat koʻrsatish sektori", "Ilmiy va innovatsion faoliyat boʻyicha xizmat koʻrsatish sektori")
    graph.edge("Ilmiy va innovatsion faoliyat boʻyicha xizmat koʻrsatish sektori", "Xalqaro aloqalar va akademik mobillik boʻyicha xizmat koʻrsatish sektori ")
    graph.edge("Xalqaro aloqalar va akademik mobillik boʻyicha xizmat koʻrsatish sektori ", "Marketing va buxgalteriya boʻyicha xizmat koʻrsatish sektori")
    
    graph.edge("Maʼlumotlar bazasi (back office) boʻlimi boshligʻi", "Statistik maʼlumotlarni yuritish sektori ")
    graph.edge("Statistik maʼlumotlarni yuritish sektori ", "Oʻquv jarayonini muvofiqlashtirish sektori")
    graph.edge("Oʻquv jarayonini muvofiqlashtirish sektori", "Talabalar hujjatlarini yuritish va saqlash sektori")

    st.graphviz_chart(graph)
tab1, tab2 = st.tabs(['Front office', 'Back office'])

with tab1:
    st.write("")
    with st.expander(":green[Talabalarga xizmat koʻrsatish sektori bo‘yicha]"):
        st.write('''
                - dars jadvallari haqida maʼlumot taqdim etish;
                - qayta oʻqish uchun fan guruhlariga ariza yuborishga yordam berish;
                - joriy, oraliq va yakuniy nazoratlar toʻgʻrisida talabalarga maʼlumot taqdim etish;
                - sirtqi va masofaviy taʼlim shaklida oʻqiyotgan talabalar uchun chaqiruv qogʻozini shakllantirish;
                - akademik maʼlumotnoma va transkript berish;
                - imtihonlar roʻyxatini taqdim etish;
                - oʻqishni koʻchirish va qayta tiklash uchun ariza yuborishga yordam berish;
                - oliy taʼlim tashkilotlariga ikkinchi taʼlimga kirish uchun onlayn ariza topshirishga yordam berish;
                - oliy taʼlim tashkilotlarining magistratura (klinik ordinatura) bosqichiga kirish uchun onlayn ariza topshirishga yordam berish;
                - talaba guvohnomasi hamda turar joyi guvohnomasini yaratish va taqdim etish;
                - talabaga oʻzining GPA koʻrsatkichi haqida maʼlumotnoma taqdim etish;
                - talabalarning “HEMIS” axborot tizimidagi parolini tiklash;
                - talabalarga tibbiy sugʻurta olish uchun yordam berish;
                - oʻqishga qabul va oʻqishni koʻchirish yuzasidan konsultatsiya berish;
                - ijara subsidiyasi uchun ariza yozishga koʻmaklashish;
                - oliy taʼlim tashkilotida mavjud turli xizmatlar va resurslar haqida maʼlumot berish; 
                - qatʼiy hisobdagi hujjatlar shakllarini (diplom, diplomga ilova, akademik sertifikatlar va boshqalar) taqdim etish;
                - qatʼiy hisobdagi blankalarini (diplom blankalari, akademik guvohnomalar, diplom ilovasi va boshqalar) qabul qilish, saqlash va berishni tashkil etish;
                - akademik qarzdor talabalarni aniqlash; 
                - talabalarning yotoqxonalarga joylashishi uchun ariza berishga koʻmaklashish;
                - talabalar turar joyiga koʻchib oʻtganlarni vaqtinchalik roʻyxatga qoʻyish uchun hujjatlarni tayyorlash;
                - ijara asosida yashayotgan talabalarga oylik ijara toʻlovining 50 foizi (bazaviy hisoblash miqdorining yarim baravaridan oshmagan holda) Davlat byudjeti mablagʻlari hisobidan toʻlab berilishi uchun hujjatlarni rasmiylashtirish va tavsiyalar berish.

                 ''')
    with st.expander(":blue[Ilmiy va innovatsion faoliyat boʻyicha xizmat koʻrsatish sektori bo‘yicha]"):
        st.write('''
                - grantlar va tanlovlar haqida maʼlumot berish;
                - ilmiy konferensiyalar haqida maʼlumot berish;
                - innovatsion gʻoya va startaplarni roʻyxatdan oʻtkazishga yordam berish;
                - talabalarga nomdor stipendiyalar haqida maʼlumot berish hamda ariza berishda koʻmaklashish;
                - ilmiy loyihalar toʻgʻrisida konsultatsiya berish;
                - “Ustoz-shogird maktabi”ga aʼzo boʻlishga yordam berish;
                - oliy taʼlim tashkiloti tomonidan tashkil etilayotgan ilmiy konferensiya, seminar va boshqa ilmiy-innovatsion tadbirlarni talabalar orasida ommalashtirish;
                - talabalarga ilmiy toʻgaraklar haqida maʼlumot berish hamda amaliy yordam koʻrsatish.

                 ''')
    with st.expander(":red[Xalqaro aloqalar va akademik mobillik boʻyicha xizmat koʻrsatish sektori bo‘yicha]"):
        st.write('''
                - oʻqish joyidan ingliz tilida maʼlumotnoma berish;
                - turli xalqaro grantlar va akademik mobillik dasturlari boʻyicha maʼlumotlarni taqdim etish;
                - oʻqishga qabul qilingan xorijlik talabalarni elektron tizimda roʻyxatga olish va fanlarga biriktirish;
                - xorijiy oliygohlarda tahsil olishda konsultatsiya berish;
                - xorijlik talabalar uchun viza xizmatlarini amalga oshirish;
                - xorijlik talabalarga toʻlov-shartnomalarini taqdim etish;
                - xorijlik talabalarni Oʻzbekiston Respublikasida vaqtinchalik roʻyxatga qoʻyish xizmatlarini amalga oshirish;
                - xorijlik talabalarni oʻqishga qabul qilish boʻyicha konsultatsiya berish, ariza va talab etiladigan hujjatlarni koʻrib chiqish uchun qabul qilish;
                - xorijlik talabalarga oliy taʼlim tashkilotidagi oʻquv jarayonlari haqida maʼlumot berish
                 ''')
    with st.expander("Marketing va buxgalteriya boʻyicha xizmat koʻrsatish sektori bo‘yicha"):
        st.write('''
                - ishga joylashgan bitiruvchilar haqida maʼlumotlarni kiritish va olish;
                - toʻlov-shartnoma summasini aniqlash, hisoblash va taqdim etish;
                - akademik qarzdor talabalar uchun qayta oʻzlashtirish bo‘yicha toʻlov miqdorlarini aniqlash va tasdiqlash;
                - talabalarga ishga joylashish borasida tavsiyalar berish;
                - bitiruvchilarni ishga taqsimlash va joylashishiga oid barcha zaruriy hujjatlar (ishga yuborilganlik toʻgʻrisida yoʻllanma, taqsimot komissiyasi qarori, shaxsiy taqsimot qaydnomasi) tayyorlash, rasmiylashtirish va bitiruvchilarga yetkazish;
                - potensial ish beruvchilar roʻyxatini shakllantirish va talabalarga yetkazish
                ''')

with tab2:
    st.write("")
    with st.expander(":green[Statistik maʼlumotlarni yuritish sektori bo‘ycha]"):
        st.write('''
                - talabalar, resurslar, shartnomalar, mashgʻulotlar va talabalarning oʻzlashtirishi haqidagi turli xil statistik maʼlumotlarni umumlashtirish va tahlil qilish;
                - talabalarning kursdan kursga qolishi, talabalar safidan chetlashtirilishi                 va akademik taʼtilga chiqishi boʻyicha statistik maʼlumotlarni umumlashtirish                va tahlil qilish;
                - oʻqishni koʻchirish va tiklashga tavsiya etilgan talabalarga oid statistik maʼlumotlarni umumlashtirish va tahlil qilish;
                - topshiriq va murojaatlarga asosan oliy taʼlim tashkiloti faoliyatiga doir statistik maʼlumotlarni taqdim etishga tayyorlash;
                - oliy taʼlim tashkilotlari tomonidan Statistika agentligiga taqdim etiladigan hisobot shakllarini yuritish;
                - bitiruvchilar toʻgʻrisida umumiy maʼlumotlar bankini shakllantirish;
                - bitiruvchilar bandligini ta’minlash bo‘yicha monitoring olib borish hamda ishga joylashganligi toʻgʻrisida maʼlumotlarni tayyorlash;
                - “HEMIS” axborot tizimiga kiritilayotgan statistik maʼlumotlarning toʻgʻriligini tahlil qilib borish
                ''')
    with st.expander(":blue[Oʻquv jarayonini muvofiqlashtirish sektori bo‘yicha]"):
        st.write('''
                - akademik guruhlarni shakllantirish;
                - talabalarga qayta oʻqishni tashkil qilish (fan guruhlarini yaratish, arizalarni koʻrib chiqish);
                - talabalarni tegishli fanlarga biriktirish;
                - talabalarni tizimga kiritish va tegishli guruhlarga biriktirish;
                - tyutorga tegishli guruhlarni biriktirish;
                - oʻquv rejada mavjud fanlarni semestrlarga biriktirish;
                - qabul qilingan talabalarni elektron tizimda roʻyxatga olish va fanlarga biriktirish;
                - talabalarni kursdan kursga oʻtkazish;
                - talabalarning o‘zlashtirish ko‘rsatkichini umumlashtirish va tahlil qilish; 
                - talabalarning maʼlumot bazalarini shakllantirish va yangilab borish;
                - oʻqishni bitirgan talabalarni tegishli tartibda rasmiylashtirish;
                - “HEMIS” tizimi orqali talabalar davomatini nazorat qilish, kunlik davomat hisobotini olish va fanlar boʻyicha davomatni monitoring qilish.
                '''
                )   
    with st.expander(":red[Talabalar hujjatlarini yuritish va saqlash sektori bo‘yicha]"):
        st.write('''
                - oliy taʼlim tashkilotini tugatgan talabalar hujjatlarini toʻplab yigʻma jildga tikish, roʻyxatga olish va arxivga qadar saqlash;
                - familiyasi oʻzgargan, akademik taʼtilga chiqqan, yoʻnalishni va fakultetni oʻzgartirgan, kursda qoldirilgan, talabalar safidan chiqarilgan talabalarning buyruqlaridan koʻchirmalarni talabalar bazasiga joylashtirish;
                - oʻqishni boshqa oliy taʼlim tashkilotiga koʻchirish munosabati bilan talabalar safidan chetlatilgan talabalarni hamma kerakli hujjatlarini talabaga yetkazish;
                - bitiruvchilarga berilgan diplomlarning haqiqiyligini tasdiqlash maqsadida doimiy ravishda https://OTT.mehnat.uz va http://d-arxiv.edu.uz platformalari orqali tashkilot va muassasalar bilan yozishmalarni amalga oshirish, yoʻqotilgan diplom va ilovalar oʻrniga dublikat berish toʻgʻrisidagi murojaatlarga javob qaytarish.
                ''')

