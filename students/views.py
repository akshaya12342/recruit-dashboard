from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Student


def student_list(request):
	query = request.GET.get("q", "").strip()
	course_interest = request.GET.get("course_interest", "").strip()
	students = Student.objects.all().order_by("-created_at")

	if query:
		students = students.filter(Q(name__icontains=query) | Q(email__icontains=query))

	if course_interest:
		students = students.filter(course_interest=course_interest)

	course_interest_label = dict(Student.COURSE_CHOICES).get(course_interest, "")

	context = {
		"students": students,
		"query": query,
		"course_interest": course_interest,
		"course_interest_label": course_interest_label,
		"course_choices": Student.COURSE_CHOICES,
		"total_count": students.count(),
	}
	return render(request, "students/student_list.html", context)


def student_create(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("students:list")
	else:
		form = StudentForm()

	return render(request, "students/student_form.html", {"form": form})
