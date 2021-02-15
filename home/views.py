from django.shortcuts import render, redirect
from .model.signup import Signup
from .model.blog import Blog
from .model.category import Category
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def index(request):
    if request.session.get("islogin"):
        return render(request, "afterlogin.html")
    return render(request, "index.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Signup.get_customer(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['email'] = email
                request.session['islogin'] = True
                return redirect("afterlogin")
            else:
                error_message = "email and password invaild"

        else:
            error_message = "email and password invaild"

            return render(request, 'login.html', {'error': error_message})


def afterlogin(request):
    if request.method == "GET":
        categories = Category.get_all_categories()
        data = {}
        data['categories'] = categories
        return render(request, "afterlogin.html", data)
    else:
        postdata = request.POST
        title = postdata.get('title')
        post = postdata.get('post')
        category = postdata.get('category')
        bloguser = Blog(
            email=request.session.get("email"),
            title=title,
            post=post,
            category=category,
        )
        bloguser.reg()

        return render(request, "myblog.html")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        email = postdata.get('email')
        password = postdata.get('password')
        confirm_password = postdata.get('confimpassword')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
        # validation------>
        error_message = None
        if(not first_name):
            error_message = "first name required"
        elif (not last_name):
            error_message = "last name required"
        elif len(password) < 6:
            error_message = "password must be 6 char long"
    # saving---->
        if not error_message:
            customer = Signup(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                confirm_password=confirm_password
            )
            customer.password = make_password(customer.password)
            customer.confirm_password = make_password(
                customer.confirm_password)
            customer.register()
            return redirect('loginpage')
        else:
            data = {
                'error': error_message,
                'value': value
            }
            return render(request, 'register.html', data)


def logout(request):
    if request.session.get("islogin"):
        del request.session['email']
        del request.session['islogin']
        return render(request, "login.html")
    else:
        return redirect("afterlogin")


def myblog(request):
    if request.method == "GET":
        blogs = Blog.objects.filter(email=request.session.get("email"))
        return render(request, "myblog.html", {"data": blogs})

    else:
        pass


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


def blog(request):
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        print(categoryId)
        data = {}
        data['categories'] = categories
        for obj in Category.objects.filter(id=categoryId):
            name=obj.name
            print(name)
            if name:
                    blogs = Blog.get_all_blog_by_name(name)
                    data['blogs'] = blogs
                    return render(request, 'blog.html', data)
            else:
                pass
        else:
                blog = Blog.get_all_blogs()
                data = {}
                data['blogs'] = blog
                data['categories'] = categories
                return render(request, 'blog.html',data)
        return render(request, 'blog.html', data)


def about(request):
    return render(request, "about.html")
