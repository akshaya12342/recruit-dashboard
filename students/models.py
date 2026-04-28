from django.db import models


class Student(models.Model):
	COURSE_CHOICES = [
		("web_development", "Web Development"),
		("data_science", "Data Science"),
		("ux_design", "UX Design"),
		("devops", "DevOps"),
		("product_management", "Product Management"),
	]

	STATUS_CHOICES = [
		("new", "New"),
		("contacted", "Contacted"),
		("interviewing", "Interviewing"),
		("accepted", "Accepted"),
		("rejected", "Rejected"),
	]

	name = models.CharField(max_length=120)
	email = models.EmailField(unique=True)
	course_interest = models.CharField(max_length=32, choices=COURSE_CHOICES)
	status = models.CharField(max_length=24, choices=STATUS_CHOICES, default="new")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
