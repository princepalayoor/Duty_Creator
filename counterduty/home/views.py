
from django.shortcuts import render
from .models import stafflevel, stafftype, staff

# Create your views here.
def index(request):
    return render(request, 'home.html')

#staff views
def staffadd(request):
    message = '0'
    if request.method == "POST":
        sname = request.POST['sname']
        stype = stafftype.objects.get(stafftype_name = request.POST['stype'])
        slevel = stafflevel.objects.get(stafflevel_name = request.POST['slevel'])
        sstatus = request.POST.get('sstatus', 0)
        if sstatus:
            sstatus = 1
        else:
            sstatus = 0
        staffdata = staff(staff_name=sname, staff_type=stype, staff_level=slevel, staff_active=sstatus)
        staffdata.save()
        message = "Staff " + sname + " Created Successfully"
    
    dict_type = {
        'typename':stafftype.objects.all()
    }
    dict_level = {
        'levelname':stafflevel.objects.all()
    }
    dict = {'type':dict_type, 'level':dict_level, 'messagedata':message}
    return render(request, 'addstaff.html', dict)

def stafflist(request):
    dict_staff_counter = {
        'staffname':staff.objects.filter(staff_type='1'),
        'countercount':staff.objects.filter(staff_type='1').count()
    }
    dict_staff_department = {
        'staffname':staff.objects.filter(staff_type='2'),
        'departmentcount':staff.objects.filter(staff_type='2').count()
    }
    dict_staff_office = {
        'staffname':staff.objects.filter(staff_type='3'),
        'officecount':staff.objects.filter(staff_type='3').count()
    }
    dict_staff = {'counter':dict_staff_counter, 'department':dict_staff_department, 'office':dict_staff_office}
    return render(request, 'stafflist.html', dict_staff)

def staffdetails(request, id):
    message = '0'
    if request.method == "POST":
        sname = request.POST['sname']
        stype = stafftype.objects.get(stafftype_name = request.POST['stype'])
        slevel = stafflevel.objects.get(stafflevel_name = request.POST['slevel'])
        sstatus = request.POST.get('sstatus', 0)
        if sstatus:
            sstatus = 1
        else:
            sstatus = 0
        selectstaffdetails = staff.objects.get(id=id)
        if selectstaffdetails.staff_name != sname:
            selectstaffdetails.staff_name = sname
            if message != '0':
                message = message + " And Name"
            else:
                message = "Name"
        if selectstaffdetails.staff_type != stype:
            selectstaffdetails.staff_type = stype
            if message != '0':
                message = message + " And Type"
            else:
                message = "Type"
        if selectstaffdetails.staff_level != slevel:
            selectstaffdetails.staff_level = slevel
            if message != '0':
                message = message + " And Level"
            else:
                message = "Level"
        if selectstaffdetails.staff_active != sstatus:
            selectstaffdetails.staff_active = sstatus
            if message != '0':
                message = message + " And Status"
            else:
                message = "Status"
        if message != '0':
            selectstaffdetails.save()
            message = message + " Changed Successfully"
        else:
            message = "No Changes Found"
        

    dict_staff_details = {
        'staffname':staff.objects.get(id=id)
    }
    dict_type = {
        'typename':stafftype.objects.all()
    }
    dict_level = {
        'levelname':stafflevel.objects.all()
    }
    dict_add_staff = {
        'staffdetails':dict_staff_details, 'type':dict_type, 'level':dict_level, 'messagedata':message
    }
    return render(request, 'staffdetails.html', dict_add_staff)