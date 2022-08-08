from django.http import HttpResponse,JsonResponse

def getlunbo(request):
    resObj = [
        {
        'id': 1,
        'url': 'http://www.itcast.cn/subject/phoneweb/index.html',
        'img': 'http://destiny001.gitee.io/image/ban1.jpg'
    }, {
           'id': 2,
           'url': 'http://www.itcast.cn/subject/phoneweb/index.html',
           'img': 'http://destiny001.gitee.io/image/ban2.jpg'
    }, {
           'id': 3,
           'url': 'http://www.itcast.cn/subject/phoneweb/index.html',
           'img': 'http://destiny001.gitee.io/image/ban3.jpg'
    },
    {
        'id': 4,
        'url': 'http://www.itcast.cn/subject/phoneweb/index.html',
        'img': 'http://destiny001.gitee.io/image/ban4.jpg'
    }
    ]
    return JsonResponse({'code':200,'msg':'获取成功','data':resObj})
def getnewslist(request):
    resObj = [{'add_time': "2015-04-16T03:50:28.000Z",
    'click': 1,
    'id': 13,
    'img_url': "http://demo.dtcms.net/upload/201504/16/201504161149414479.jpg",
    'title': "1季度多家房企利润跌幅超50% 去库存促销战打响",
    'zhaiyao': "房企一季度销售业绩已经陆续公布，克而瑞研究中心统计"
               },
              {
    'add_time': "2015-04-16T04:05:34.000Z",
    'click': 2,
    'id': 14,
    'img_url': "http://demo.dtcms.net/upload/201504/16/201504161205596364.jpg",
    'title': "买房还是炒股，2015年买房无法拒绝的5大理由",
    'zhaiyao': "转眼间2015年已经过去了4个月，在这短短的四个月"
              },
              {
                  'add_time': "2016-12-07T08:49:04.000Z",
                  'click': 1,
                  'id': 15,
                  'img_url': "http://demo.dtcms.net/upload/201504/16/201504161218505373.jpg",
                  'title': "抢先实拍猎豹CS10 霸气时尚2.0T涡轮增压",
                  'zhaiyao': "在SUV当道的天下，许多自主品牌相继推出了旗下多款"
              },
              {
                  'add_time': "2016-12-07T08:49:04.000Z",
                  'click': 1,
                  'id': 15,
                  'img_url': "http://demo.dtcms.net/upload/201504/16/201504161218505373.jpg",
                  'title': "抢先实拍猎豹CS10 霸气时尚2.0T涡轮增压",
                  'zhaiyao': "在SUV当道的天下，许多自主品牌相继推出了旗下多款"
              },
              {
                  'add_time': "2016-12-07T08:49:04.000Z",
                  'click': 1,
                  'id': 15,
                  'img_url': "http://demo.dtcms.net/upload/201504/16/201504161218505373.jpg",
                  'title': "抢先实拍猎豹CS10 霸气时尚2.0T涡轮增压",
                  'zhaiyao': "在SUV当道的天下，许多自主品牌相继推出了旗下多款"
              },
              {
                  'add_time': "2016-12-07T08:49:04.000Z",
                  'click': 1,
                  'id': 15,
                  'img_url': "http://demo.dtcms.net/upload/201504/16/201504161218505373.jpg",
                  'title': "抢先实拍猎豹CS10 霸气时尚2.0T涡轮增压",
                  'zhaiyao': "在SUV当道的天下，许多自主品牌相继推出了旗下多款"
              },
              {
                  'add_time': "2016-12-07T08:49:04.000Z",
                  'click': 1,
                  'id': 15,
                  'img_url': "http://demo.dtcms.net/upload/201504/16/201504161218505373.jpg",
                  'title': "抢先实拍猎豹CS10 霸气时尚2.0T涡轮增压",
                  'zhaiyao': "在SUV当道的天下，许多自主品牌相继推出了旗下多款"
              },
              {
                  'add_time': "2016-12-07T08:49:04.000Z",
                  'click': 1,
                  'id': 15,
                  'img_url': "http://demo.dtcms.net/upload/201504/16/201504161218505373.jpg",
                  'title': "抢先实拍猎豹CS10 霸气时尚2.0T涡轮增压",
                  'zhaiyao': "在SUV当道的天下，许多自主品牌相继推出了旗下多款"
              },
              ]
    return JsonResponse({'code': 200, 'msg': '获取成功', 'data': resObj})