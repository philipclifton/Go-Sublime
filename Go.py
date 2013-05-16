import sublime, sublime_plugin, pprint, subprocess

class create_vhost(sublime_plugin.TextCommand):
	folder = ''
	giturl = ''
	def run(self, edit):
		# pprint.pprint(sublime.get_clipboard())
		self.view.window().show_input_panel('Project Folder: ', '', self.project_done, self.project_change, self.project_cancel)
		return ''

	def project_done(self, string):
		self.folder = string
		self.view.window().show_input_panel('Git Remote: ', '', self.git_done, self.project_change, self.project_cancel)
	
	def git_done(self, string):
		self.giturl = string

		if self.giturl != '' and self.folder != '':
			print ('Creating VHOST at ' + self.folder + ' from  ' + self.giturl)
			print (subprocess.call("go create " + self.folder + ' ' + self.giturl , shell=True))
		elif self.folder != '':
			print ('Creating VHOST at ' + self.folder)
			print (subprocess.call("go create " + self.folder, shell=True))

	def project_change(self, string):
		return ''

	def project_cancel(self, string):
		return ''

class remove_vhost(sublime_plugin.TextCommand):

	def run(self, edit):
		# pprint.pprint(sublime.get_clipboard())
		self.view.window().show_input_panel('Project Folder: ', '', self.project_done, self.project_change, self.project_cancel)
		return ''

	def project_done(self, string):
		if string != '':
			print ('Deleting VHOST at ' + string)
			print (subprocess.call("go remove " + string, shell=True))

	def project_change(self, string):
		return ''

	def project_cancel(self, string):
		return ''


class work_vhost(sublime_plugin.TextCommand):

	def run(self, edit):
		# pprint.pprint(sublime.get_clipboard())
		self.view.window().show_input_panel('Project: ', '', self.project_done, self.project_change, self.project_cancel)
		return ''

	def project_done(self, string):
		if string != '':
			print ('Switching Project to ' + string)
			print (subprocess.call("go work " + string, shell=True))

	def project_change(self, string):
		return ''

	def project_cancel(self, string):
		return ''
