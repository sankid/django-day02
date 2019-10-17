from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    # # 通过loader加载模板
    # html = loader.get_template('test.html')
    # # 将html对象转换成html字符串
    # html = html.render()
    # # 将html return到浏览器
    # return HttpResponse(html)

    # render 方案
    dict = {'username': 'guoxiaonao', 'age': 18}
    return render(request, 'test.html', dict)  # 比上一次方法简单


def test_p(request):
    # 测试页面传参
    dic = {}
    dic['lst'] = ['小红', '小明', '小兰']
    dic['dict'] = {'username': 'guoxiaonao', 'age': 18}
    dic['class_obj'] = Dog()
    dic['say_hi'] = say_hi
    return render(request, 'test_p.html', dic)


class Dog:
    def say(self):
        return 'hahahaha'


def say_hi():
    return 'hi~'


def test_if(request):
    # /test_if?x=3
    x = int(request.GET.get('x', 0))
    dic = {'x': x}
    return render(request, 'test_if.html', dic)


def mycal(request):
    # GET & POST
    if request.method == 'GET':
        # 拿页面显示给用户
        return render(request, "cal.html")
    elif request.method == 'POST':
        # /mycal?x=x_val&op=op_val&y=y_val  浏览器从页面上收集到的数据会返回到按照name值返回后台
        # x = int(request.POST.get('x'))  #text框 空提交时 浏览器会带上具体text框的name及空值一并提交到浏览器
        x = request.POST.get('x')
        if not x:
            error = 'Please give me x!!'
            dic = {'error': error}
            return render(request, 'cal.html', dic)
        try:
            x = int(x)
        except Exception as e:
            print("----x is error----")
            print(e)
            try:
                x = int(float(x))
            except Exception as e:
                error = 'The x must be error'
                dic = {'error': error}
                return render(request, 'cal.html', dic)

        # TODO 检查y值;方法同上
        op = request.POST.get('op')
        y = int(request.POST.get('y'))
        result = 9999999
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request, 'cal.html', locals())
        return HttpResponse("----TEST IS OK----")


def test_for(request):
    lst = {"小红", "小兰", "小绿"}
    return render(request, 'test_for.html', locals())


def base_c(x):
    if x < 3082:
        return 0
    elif x > 23118:
        return 23118
    else:
        return x


def insur(request):
    if request.method == 'GET':
        # 拿页面显示给用户
        return render(request, "insurance.html")
    elif request.method == 'POST':
        base = request.POST.get('base')
        if not base:
            error = '请输入工资基数!'
            dic = {'error': error}
            return render(request, 'insurance.html', dic)
        try:
            base = int(base)
        except Exception as e:
            print("----x is error----")
            print(e)
            try:
                base = int(float(base))
            except Exception as e:
                print(e)
                error = 'The x must be error'
                dic = {'error': error}
                return render(request, 'cal.html', dic)
        op = request.POST.get('is_city')
        b = base_c(base)
        try:
            # 养老保险
            x1 = 0.08 * b
            y1 = 0.19 * b
            # 生育保险
            x3 = 0
            y3 = 0.008 * b
            # 医疗保险
            x4 = 0.02 * b + 3
            y4 = 0.1 * b
            # 工伤保险
            x5 = 0
            y5 = 0.005 * b
            # 公积金
            x6 = 0.12 * b
            y6 = 0.12 * b
            if op == '1':
                # 失业保险
                x2 = 0.002 * b
                y2 = 0.008 * b
            else:
                # 失业保险
                x2 = 0
                y2 = 0.008 * b

            total_per = x1 + x2 + x3 + x4 + x5 + x6
            total_com = y1 + y2 + y3 + y4 + y5 + y6
            total = total_com + total_per
            return render(request, 'result_i.html', locals())
        except Exception as e:
            print(e)
            return render(request, 'insurance.html')
