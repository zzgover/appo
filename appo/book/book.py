from decimal import	Decimal
from django.conf import	settings
from project.models import Project
class Book(object):
    def __init__(self, request):	 	 	 #	request 作为参数
        self.session = request.session
        book = self.session.get(settings.BOOK_SESSION_ID)
        if not book:
            book = self.session[settings.BOOK_SESSION_ID] =	{}
        self.book =	book
    def	add(self, project):
        project_id = str(project.id)
        if project_id not in self.book:
            self.book[project_id] =	{'quantity': 0, 'price': str(project.price)}
        self.save()
    def	save(self):
        self.session[settings.BOOK_SESSION_ID] = self.book
    #	session.modified 标记为 True 是为了告诉 Django，session 已经被改动，需要将它保存起来
        self.session.modified =	True
    def	remove(self, project):
        project_id = str(project.id)
        if project_id in self.book:
            del	self.book[project_id]
            self.save()
    def __iter__(self):
        project_ids	= self.book.keys()
        projects = Project.objects.filter(id__in=project_ids)
        for	project	in projects:
            self.book[str(project.id)]['project'] =	project
    def clear(self):
        del self.session[settings.BOOK_SESSION_ID]

        self.session.modified = True