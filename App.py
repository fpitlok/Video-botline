from flask import Flask, request, abort
...
...
...
...

app = Flask(__name__)
... 
...
...
...
@app.route("/callback", methods=['POST'])
def callback():
    ...
    ...

def update_xvideo(url):
    res = requests.get(url)
    imgs = re.findall(r'http://img-.*jpg',res.text)
    t = re.findall(r'html5player.setVideoUrlHigh(.*)',res.text)
    img = 'https{}'.format(imgs[0][4:])
    url = t[0][2:-3]
    return url,img
def yvideo(url):
    url = 'https://qdownloader.net/download?video={}'.format(url)
    res = requests.get(url)
    soup = bf(res.text,'html.parser')
    t = soup.select('.col-md-8 td a' )
    url = t[0]['href']
    t = soup.select('.info.col-md-4 img' )
    img = t[0]['src']
    url = re.search(r'.*&title',url).group()[:-6]
    return url,img
def youtube_page(keyword):
    url = []
    title = []
    pic = []
    target_url = 'https://www.youtube.com/results?search_query={}&sp=EgIQAQ%253D%253D'.format(quote(keyword))
    rs = requests.session()
    res = rs.get(target_url)
    soup = bf(res.text, 'html.parser')
    for data in soup.select('.yt-lockup-title'):
        if len(data.find('a')['href']) > 20:
            continue
        url.append('https://www.youtube.com{}'.format(data.find('a')['href']))
        title.append(data.find('a')['title'])
        pic.append('https://i.ytimg.com/vi/{}/0.jpg'.format(data.find('a')['href'][9:]))
    return url,title,pic

def xvideo_page(text,page=0):
    tex =  quote(text)
    url = []
    img = []
    title = []
    target_url = 'https://www.xvideos.com/?k={}&p={}'.format(tex,page)
    rs =  requests.session()
    rs.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    res = rs.get(target_url)
    soup = bf(res.text,'html.parser')
    title = [i.select('a')[0].get('title') for i in soup.select('.thumb-under')]
    url = ['https://www.xvideos.com'+i.select('a')[0].get('href') for i in soup.select('.thumb')]
    img = [i.select('img')[0].get('data-src') for i in soup.select('.thumb')]
    return img,url,title

def buttons_template_yout(page, keyword, jud):
    confirm_template = TemplateSendMessage(
        alt_text='video template',
        template=ConfirmTemplate(
            text='請選擇一下',
            actions=[
                MessageTemplateAction(
                    label='推薦',
                    text='台北暗殺星奪冠之路yout'
                ),
                PostbackTemplateAction(
                    label='再來10部',
                    data='carousel/{}/{}/{}'.format(page, keyword, jud)
                )
            ]
        )
    )
    return confirm_template


def carousel_template(keyword='japanese', jud='xvideo', page=0):
    pass_url = []
    if jud == 'yout':
        judge = 'yout'
        video_url, title, img_url = youtube_page(keyword)
    else:
        img_url, video_url, title = xvideo_page(keyword)
        judge = 'xvideo'
    if page != 0:
        if jud == 'xvideo':
            img_url, video_url, title = xvideo_page(keyword, page / 2)
        if page % 2 == 0:
            pass
        else:
            temp = 10
            video_url = [i for i in video_url[temp:]]
            title = [i for i in title[temp:]]
            img_url = [i for i in img_url[temp:]]
    if jud == 'yout':
        pass_url = [i[32:] for i in video_url]
    else:
        pass_url = [i[24:] for i in video_url]
    if len(title) < 10:
        buttons_template = porn_video_template(keyword, jud)
        return buttons_template

    Image_Carousel = TemplateSendMessage(
        alt_text='Carousel_template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url=img_url[0],
                    action=PostbackTemplateAction(
                        label=title[0][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[0])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[1],
                    action=PostbackTemplateAction(
                        label=title[1][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[1])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[2],
                    action=PostbackTemplateAction(
                        label=title[2][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[2])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[3],
                    action=PostbackTemplateAction(
                        label=title[3][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[3])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[4],
                    action=PostbackTemplateAction(
                        label=title[4][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[4])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[5],
                    action=PostbackTemplateAction(
                        label=title[5][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[5])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[6],
                    action=PostbackTemplateAction(
                        label=title[6][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[6])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[7],
                    action=PostbackTemplateAction(
                        label=title[7][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[7])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[8],
                    action=PostbackTemplateAction(
                        label=title[8][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[8])
                    )
                ),
                ImageCarouselColumn(
                    image_url=img_url[9],
                    action=PostbackTemplateAction(
                        label=title[9][:12],
                        text='請等待一下...',
                        data='video/{}/{}/{}'.format(judge, keyword, pass_url[9])
                    )
                )
            ]
        )
    )
    return [Image_Carousel, buttons_template_yout(page, keyword, jud)]

def get_total_flex(body_content,footer_content=[ButtonComponent(style='link',action=URIAction(label='My github', uri='https://github.com/kevin1061517?tab=repositories'))]):
    bubble = BubbleContainer(
            body=BoxComponent(
                layout='vertical',
                contents=body_content
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents= footer_content
            )
        )
    return bubble

def look_up(tex):
    content = ''
    target_url = 'https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXG86cTRcUGoAESt9rolQ?p={}&fr2=sb-top'.format(tex)
    res =  requests.get(target_url)
    soup = bf(res.text,'html.parser')
    try:
        content += '{}\n'.format(soup.select('.lh-22.mh-22.mt-12.mb-12.mr-25.last')[0].text)
        for i in soup.select('.layoutCenter .lh-22.mh-22.ml-50.mt-12.mb-12'):
            if i.select('p  span') != []:   
                content += '{}\n{}\n'.format(i.select('.fz-14')[0].text,i.select('p  span')[0].text)
            else:
                content += '{}\n'.format(i.select('.fz-14')[0].text)
        if content == '':
            for i in soup.select('.layoutCenter .ml-50.mt-5.last'):
                content += i.text
    except IndexError:
        content = '查無此字'
    return content


def integer_word(word):
    content = look_up(word)
    if content != '查無此字':
        content = [TextComponent(text='🔍英文單字查詢',weight='bold', align='center',size='md',wrap=True,color='#000000'),SeparatorComponent(margin='lg'),TextComponent(text=content, size='sm',wrap=True,color='#000000')]
        audio_button = [
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=PostbackAction(label='📢 美式發音', data='audio/{}'.format(word))
                    )
                    ]
        ..................
        ......省略@@......
        ..................
    else:
        message = TextSendMessage(text=content)
    return message
def template_img(path):
            print('temp---------'+str(path))
            buttons_template = TemplateSendMessage(
            alt_text='news template',
            template=ButtonsTemplate(
                title='你傳來的是圖片',
                text='請選擇怎樣處理',
                thumbnail_image_url='https://i.imgur.com/GoAYFqv.jpg',
                actions=[
                    PostbackTemplateAction(
                        label='影像文字翻譯辨識',
                        text='請稍等....',
                        data = 'trans/{}'.format(path)
                    ),
                    PostbackTemplateAction(
                        label='影像儲存至相簿',
                        text='請稍等....',
                        data = 'image/{}'.format(path)
                    )
                ]
            )
            )
            return buttons_template
        

import pytesseract
from PIL import Image
@handler.add(PostbackEvent)
def handle_postback(event):
    temp = event.postback.data
    s = ''
    if temp[:5] == 'image':
     print('------postback'+str(temp))
     t = temp.split('/')
     path = '/{}/{}'.format(t[2],t[3])
     print('postback---------'+str(path))
     img_id = 1
     t = fb.get('/pic',None)
     if t!=None:
         count = 1
         for key,value in t.items():
            if count == len(t):#取得最後一個dict項目
                img_id = int(value['id'])+1
            count+=1
     try:

        client = ImgurClient(client_id, client_secret, access_token, refresh_token)
        config = {
            'album': album_id,
            'name' : img_id,
            'title': img_id,
            'description': 'Cute kitten being cute on'
        }
        client.upload_from_path(path, config=config, anon=False)
        os.remove(path)
        line_bot_api.reply_message(event.reply_token,[TextSendMessage(text='上傳成功'),image_reply])
     except  Exception as e:
        t = '上傳失敗'+str(e.args)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=t))
    elif temp[:5] == 'trans':
        t = temp.split('/')
        path = '/{}/{}'.format(t[2],t[3])
        print('postback----'+str(path)) 
        pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
        image = Image.open(path)
        t = pytesseract.image_to_string(image)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=t))
    elif temp[:5] == 'audio':
        print('-----------')
        t = temp.split('/')
        word = t[1]
        url = 'https://s.yimg.com/bg/dict/dreye/live/f/{}.mp3'.format(word)
        line_bot_api.reply_message(
                event.reply_token,
                AudioSendMessage(original_content_url=url,duration=3000)
            )
    elif temp[:8] == 'carousel':
        t = temp.split('/')
        pa = int(t[1])
        print('--------be else-------{}---{}'.format(pa, str(type(pa))))
        pa += 1
        print('--------af else-------{}'.format(pa))
        keyword = t[2]
        jud = t[3]
        t = carousel_template(keyword, jud, page=pa)
        line_bot_api.reply_message(
            event.reply_token,
            t)
    elif temp[0:5] == 'video':
        t = temp.split('/')
        print('----t-----' + str(t))
        judge = t[1]
        keyword = t[2]
        video_url = t[3]
        if judge == 'yout':
            video_url = 'https://www.youtube.com/watch?v={}'.format(video_url)
            video_url, img = yvideo(video_url)
        else:
            url = 'https://www.xvideos.com/{}/{}'.format(video_url, t[4])
            video_url, img = update_xvideo(url)
        line_bot_api.reply_message(
            event.reply_token,
            VideoSendMessage(
                original_content_url=video_url,
                preview_image_url=img))
# 處理圖片
@handler.add(MessageEvent,message=ImageMessage)
def handle_msg_img(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(prefix='jpg-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name
    path = tempfile_path
    buttons_template = template_img(path)
    line_bot_api.reply_message(event.reply_token,buttons_template)


# 處理訊息:
@handler.add(MessageEvent, message=TextMessage)
def handle_msg_text(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    user_name = profile.display_name
    picture_url = profile.picture_url
    if re.search(r'eng$',event.message.text.lower())!=None:
        keyword = event.message.text.lower()[:-3]
        keyword = keyword.replace(' ','')
        print('-----------'+keyword)
        message = integer_word(keyword)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif re.search(r'porn$', event.message.text.lower()) != None:
        keyword = event.message.text.lower()[:-4]
        carousel = carousel_template(keyword)
        line_bot_api.reply_message(event.reply_token, carousel)

    elif re.search(r'yout$',event.message.text.lower())!=None:
        keyword = event.message.text.lower()[:-4]
        carousel = carousel_template(keyword,jud='yout')
        line_bot_api.reply_message(event.reply_token, carousel)
