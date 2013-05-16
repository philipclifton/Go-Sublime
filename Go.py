import sublime
import sublime_plugin
import pprint
import subprocess
import os
import re

from os.path import join



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
			message = 'Creating virtual host at ' + self.folder + ' from  ' + self.giturl
			print (subprocess.Popen("go create " + self.folder + ' ' + self.giturl , shell=True))
		elif self.folder != '':
			message = 'Creating virtual host ' + self.folder
			print (subprocess.Popen("go create " + self.folder, shell=True))
		else:
			message = 'No project directory supplied'

		self.output_view = self.get_window().get_output_panel("log")
		self.output_view.set_read_only(False)
		self._output_to_view(self.output_view, message, clear=True)
		self.output_view.set_read_only(True)
		self.get_window().run_command("show_panel", {"panel": "output.log"})

	def _output_to_view(self, output_file, output, clear=False,
	        syntax="Packages/Diff/Diff.tmLanguage", **kwargs):
	    output_file.set_syntax_file(syntax)
	    args = {
	        'output': output,
	        'clear': clear
	    }
	    output_file.run_command('git_scratch_output', args)

	
	def get_window(self):
	    return self.view.window()

	def project_change(self, string):
		return ''

	def project_cancel(self, string):
		return ''

class remove_vhost(sublime_plugin.TextCommand):

	def run(self, edit):
		self.view.window().show_input_panel('Project Folder: ', '', self.project_done, self.project_change, self.project_cancel)
		return ''

	def project_done(self, string):
		if string != '':
			message = 'Deleting VHOST at ' + string
			print (subprocess.Popen("go remove " + string, shell=True))

			self.output_view = self.get_window().get_output_panel("log")
			self.output_view.set_read_only(False)
			self._output_to_view(self.output_view, message, clear=True)
			self.output_view.set_read_only(True)
			self.get_window().run_command("show_panel", {"panel": "output.log"})

	def _output_to_view(self, output_file, output, clear=False,
	        syntax="Packages/Diff/Diff.tmLanguage", **kwargs):
	    output_file.set_syntax_file(syntax)
	    args = {
	        'output': output,
	        'clear': clear
	    }
	    output_file.run_command('git_scratch_output', args)

	
	def get_window(self):
	    return self.view.window()

	def project_change(self, string):
		return ''

	def project_cancel(self, string):
		return ''


class work_vhost(sublime_plugin.TextCommand):

	def run(self, edit):
		self.view.window().show_input_panel('Project: ', '', self.project_done, self.project_change, self.project_cancel)
		return ''

	def project_done(self, string):
		if string != '':
			
			if subprocess.Popen("go work " + string, shell=True):
				message = 'Switching Project to ' + string
			else:
				message = 'Switch to Project failed'

			self.output_view = self.get_window().get_output_panel("log")
			self.output_view.set_read_only(False)
			self._output_to_view(self.output_view, message, clear=True)
			self.output_view.set_read_only(True)
			self.get_window().run_command("show_panel", {"panel": "output.log"})

	def _output_to_view(self, output_file, output, clear=False,
	        syntax="Packages/Diff/Diff.tmLanguage", **kwargs):
	    output_file.set_syntax_file(syntax)
	    args = {
	        'output': output,
	        'clear': clear
	    }
	    output_file.run_command('git_scratch_output', args)

	
	def get_window(self):
	    return self.view.window()

	def project_change(self, string):
		return ''

	def project_cancel(self, string):
		return ''


class get_image_size(sublime_plugin.WindowCommand):
	
	def run(self, paths = []):
		dimensionArgs = ['/usr/bin/sips', '-g', 'pixelHeight', '-g', 'pixelWidth', paths[0]]
		sips = subprocess.Popen(dimensionArgs, stdout=subprocess.PIPE)
		dimensions = sips.stdout.read()
		dimensions = dimensions.decode("utf-8")
		dimensions = re.findall('pixel(Height|Width): ([0-9]+)', dimensions ,re.DOTALL)

		css_attr = 'width: ' + dimensions[1][1] + 'px;' + "\n" + 'height: ' + dimensions[0][1] + 'px;'

		sublime.set_clipboard(css_attr)


