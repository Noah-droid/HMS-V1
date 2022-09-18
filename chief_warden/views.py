from django.db.models import F
from django.shortcuts import render, redirect
from hostelapp.models import *
from .forms import *
from django.conf import settings
from accounts.decorators import *
from django.contrib import messages

User = settings.AUTH_USER_MODEL


@allowed_users(allowed_roles=['chief warden'])
def index(request):
    block_list = blocks.objects.all()
    block_count = blocks.objects.all().count()
    room_count = room.objects.all().count()
    booked = student_room.objects.count()
    student_list = student_room.objects.all().order_by('-created_on')
    spaces_left = 2596
    # capacity = room_count.Capacity
    # occupied = room_booked.Number_already_occupied
    if request.method == 'POST':
        Ref_No = request.POST.get('Ref_No')
        print(Ref_No)
        return redirect('update_student_room_name', pk=Ref_No)
    context = {'block_list': block_list, 'block_count':block_count, 'room_count':room_count, 'booked':booked,
    'student_list':student_list, 'spaces_left':spaces_left
    }
    return render(request, 'chief_warden/index.html', context)


@allowed_users(allowed_roles=['chief warden'])
def student(request):
    block_list = blocks.objects.all()
    block_count = blocks.objects.all().count()
    room_count = room.objects.all().count()
    booked = student_room.objects.count()
    student_list = student_room.objects.all().order_by('-created_on')
    spaces_left = 2592
    # capacity = room_count.Capacity
    # occupied = room_booked.Number_already_occupied
    if request.method == 'POST':
        Ref_No = request.POST.get('Ref_No')
        print(Ref_No)
        return redirect('update_student_room_name', pk=Ref_No)
    context = {'block_list': block_list, 'block_count':block_count, 'room_count':room_count, 'booked':booked,
    'student_list':student_list, 'spaces_left':spaces_left
    }
    return render(request, 'chief_warden/student.html', context)

def hostel(request):
    block_list = blocks.objects.all()
    block_count = blocks.objects.all().count()
    room_count = room.objects.all().count()
    booked = student_room.objects.count()
    student_list = student_room.objects.all()
    spaces_left = 2592
    
    # capacity = room_count.Capacity
    # occupied = room_booked.Number_already_occupied
    if request.method == 'POST':
        Ref_No = request.POST.get('Ref_No')
        print(Ref_No)
        return redirect('update_student_room_name', pk=Ref_No)
    context = {'block_list': block_list, 'block_count':block_count, 'room_count':room_count, 'booked':booked,
    'student_list':student_list, 'spaces_left':spaces_left
    }
    return render (request, 'chief_warden/hostel.html', context)


@allowed_users(allowed_roles=['chief warden'])
def manager_list(request):
    w_list = warden.objects.all()
    context = {'w_list': w_list}
    return render(request, 'chief_warden/list_HM.html', context)





@allowed_users(allowed_roles=['chief warden'])
def update_managers(request, pk):
    try:
        warden_info = warden.objects.get(id=pk)
        form_w = update_warden_form(instance=warden_info)
        if request.method == 'POST':
            form_w = update_warden_form(request.POST, instance=warden_info)
            if form_w.is_valid():
                form_w.save()
                message = "Successfully warden room update"
                messages.success(request, message)
                return redirect('chief_warden_home')
            else:
                message = "warden don't updated room!!"
                messages.error(request, message)
                redirect('chief_warden_home')

        context = {'form_w': form_w, 'warden_info': warden_info}
        return render(request, 'chief_warden/update_warden.html', context)
    except Exception:
        message = "Warden does not exist !"
        messages.error(request, message)
        return redirect('chief_warden_home')









# Create your views here.
@allowed_users(allowed_roles=['chief warden'])
def chief_warden(request):
    block_list = blocks.objects.all()
    block_count = blocks.objects.all().count()
    room_count = room.objects.all().count()
    booked = student_room.objects.count()
    student_list = student_room.objects.all()
    # capacity = room_count.Capacity
    # occupied = room_booked.Number_already_occupied
    if request.method == 'POST':
        Ref_No = request.POST.get('Ref_No')
        print(Ref_No)
        return redirect('update_student_room_name', pk=Ref_No)
    context = {'block_list': block_list, 'block_count':block_count, 'room_count':room_count, 'booked':booked,
    'student_list':student_list
    }
    return render(request, 'chief_warden/starting_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_block(request):
    create_block_form = Block_form()
    if request.method == 'POST':
        create_block_form = Block_form(request.POST)
        if create_block_form.is_valid():
            create_block_form.save()
            message = "Created Block is successfully done"
            messages.success(request, message)
            return redirect('chief_warden_home')
        else:
            message = "Created Block is Failed"
            messages.error(request, message)
            return redirect('chief_warden_home')

    context = {'form_table': create_block_form}
    return render(request, 'chief_warden/create_block_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_floor(request):
    create_floor_form = floor_form()
    if request.method == 'POST':
        create_floor_form = floor_form(request.POST)
        if create_floor_form.is_valid():
            create_floor_form.save()
            message = "Created floor is successfully done"
            messages.success(request, message)
            return redirect('chief_warden_home')
        else:
            message = "Created floor is Failed"
            messages.error(request, message)
            return redirect('chief_warden_home')

    context = {'form_table': create_floor_form}
    return render(request, 'chief_warden/create_floor_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_room(request):
    create_room_form = room_form()
    if request.method == 'POST':
        create_room_form = room_form(request.POST)
        if create_room_form.is_valid():
            create_room_form.save()
            message = "Created room is successfully done"
            messages.success(request, message)
            # return redirect('chief_warden_home')
        else:
            message = "Created room is Failed"
            messages.error(request, message)
            # return redirect('chief_warden_home')
    context = {'form_table': create_room_form}
    return render(request, 'chief_warden/create_room_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def create_warden(request):
    create_warden_form = warden_form()
    if request.method == 'POST':
        create_warden_form = warden_form(request.POST)
        if create_warden_form.is_valid():
            form = create_warden_form.save()
            # form.custom_warden_form()
            print("the form id is", form.id)
            floor_id = create_warden_form.data['Hostel_Number']
            # print("The floor id is",floor_id)
            floor_temp = floors.objects.get(id=floor_id)
            room_list = floor_temp.room_set.all()
            print("The room list is", room_list)
            # room_list = floor_temp.room_set.all().order_by('Warden_id').update(Warden_id_id = F(int(form.id)))
            for i in room_list:
                print("The warden id before is", i.Warden_id_id)
                print("the warden id from the form", form.id)
                i.Warden_id_id = int(form.id)
                # warden_name= User.objects.get(id=int(create_warden_form.data['Warden_ID']))
                # i.Warden_id = warden_name
                print("The warden id after is", i.Warden_id_id)
                print("The room is", i)
                # print("The warden name is",warden_name)
                i.save()
            message = "Successfully warden is created"
            messages.success(request, message)
            return redirect('/chief_warden/list_of_managers/')
        else:
            message = "Failed to created  warden! "
            messages.error(request, message)
            return redirect('chief_warden_home')
    context = {'form_table': create_warden_form}
    return render(request, 'chief_warden/create_warden_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def update_student_room(request, pk):
    try:
        student_info_room = student_room.objects.get(id=pk)
        print(student_info_room.user, student_info_room.user_room)
        old_room_data = student_info_room.user_room_id
        student_room_form = update_booking_form(instance=student_info_room)

        if request.method == 'POST':
            new_student_room_form = update_booking_form(request.POST, instance=student_info_room)
            if new_student_room_form.is_valid():
                # student_info_room

                old_room_id = old_room_data
                old_room = room.objects.get(id=old_room_id)
                print(f'old room {old_room}')
                print(f'old room redo {old_room.Number_already_occupied}')
                old_room.Number_already_occupied -= 1
                print(f'old room updated {old_room.Number_already_occupied}')

                new_room_data = new_student_room_form.data['user_room']

                new_room = room.objects.get(id=new_room_data)
                capacity = new_room.Capacity
                occupied = new_room.Number_already_occupied
                print(f'new room {new_room}')
                print(f'ner room redo {new_room.Number_already_occupied}')
                if capacity > occupied:
                    new_room.Number_already_occupied += 1
                    print(f'new room redo {new_room.Number_already_occupied}')
                    new_room.save()
                    new_student_room_form.save()
                    old_room.save()
                    student_room_form = new_student_room_form
                    message = "Successfully Student room update"
                    messages.success(request, message)
                    return redirect('chief_warden_home')
                else:
                    message = "Room is already occupied"
                    messages.error(request, message)
            else:

                message = "Failed to update Student room"
                messages.error(request, message)
                # print(f'new room {new_room_data} old room {old_room}')

                # student_info_room.room.save()
                # student_save_form = student_room_form.save()
        context = {'student_room_form': student_room_form, 'student_info_room': student_info_room, 'capacity':capacity}
        # print(student_room_form, '---')
        return render(request, 'chief_warden/student_room_update_page.html', context)
    except Exception:
        message = "Student didn't create room!!"
        messages.error(request, message)
        return redirect('chief_warden_home')


@allowed_users(allowed_roles=['chief warden'])
def chief_floors(request, pk):
    chief_block = blocks.objects.get(id=pk)
    chief_floors_list = chief_block.floors_set.all()
    context = {'chief_floors_list': chief_floors_list}
    return render(request, 'chief_warden/floors.html', context)


@allowed_users(allowed_roles=['chief warden'])
def chief_rooms(request, pk):
    floor_temp = floors.objects.get(id=pk)
    chief_rooms_list = floor_temp.room_set.all()
    new_room = room.objects.get(id=pk)
    capacity = new_room.Capacity
    occupied = new_room.Number_already_occupied
    floor_tem = floors.objects.get(id=pk)
    room_list = floor_tem.room_set.all()
    room_count = floor_tem.room_set.count()

    context = {'chief_rooms_list': chief_rooms_list, 'capacity':capacity, 'occupied':occupied, 'room_count':room_count}
    return render(request, 'chief_warden/rooms.html', context)


@allowed_users(allowed_roles=['chief warden'])
def student_view(request, pk):
    student_list = student_room.objects.filter(user_room_id=pk).order_by('created_on')
    context = {'student_list': student_list}
    print(student_list)
    return render(request, 'chief_warden/student_info_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def warden_list(request):
    w_list = warden.objects.all()
    context = {'w_list': w_list}
    return render(request, 'chief_warden/warden_list_page.html', context)


@allowed_users(allowed_roles=['chief warden'])
def update_warden(request, pk):
    try:
        warden_info = warden.objects.get(id=pk)
        form_w = update_warden_form(instance=warden_info)
        if request.method == 'POST':
            form_w = update_warden_form(request.POST, instance=warden_info)
            if form_w.is_valid():
                form_w.save()
                message = "Successfully warden room update"
                messages.success(request, message)
                return redirect('chief_warden_home')
            else:
                message = "warden don't updated room!!"
                messages.error(request, message)
                redirect('chief_warden_home')

        context = {'form_w': form_w, 'warden_info': warden_info}
        return render(request, 'chief_warden/update_warden_page.html', context)
    except Exception:
        message = "Warden does not exist !"
        messages.error(request, message)
        return redirect('chief_warden_home')



def search(request):
    query = request.POST['query']
    if len(query) >= 150 or len(query) < 1:
        allposts = student_room.objects.none()
    elif len(query.strip()) == 0:
        allposts = student_room.objects.none()
    else:
        allpostsTitle = student_room.objects.filter(title__icontains=query)
        allpostsAuthor = student_room.objects.filter(author__username = query)
        # allposts = allpostsAuthor.union(allpostsTitle)
    
    params = {'allposts': allposts}
    return render(request, 'chief_warden/search_results.html', params)