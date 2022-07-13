#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pathlib
import pytube

class Files:
	
	@staticmethod
	def getRealPath(pathname):
		return str(pathlib.Path(pathname).resolve())

	@staticmethod
	def checkPath(onPath: str):
		downloadpath = Files.getRealPath(onPath)
		if not pathlib.Path(downloadpath).exists():
			pathlib.Path(downloadpath).mkdir(parents=True, exist_ok=True)
		return downloadpath
	
	@staticmethod
	def checkPathText(TextFile: str):
		path_parent = str(pathlib.Path(TextFile).parent.resolve())
		if not pathlib.Path(path_parent).exists():
			return False
		else:
			return True

	@staticmethod
	def filterName(onNames: str) -> str:
		outname = str(onNames).replace('|', '.').replace('%', '.').replace(':', '.').replace('"', '.').replace("'", ".").replace('<', '.').replace('>', '.')\
		.replace('[', '.').replace(']', '.').replace('{', '.').replace('}', '.').replace('#', '.').replace('$', '.').replace('?', '.')\
		.replace('`', '.').replace('~', '.').replace('@', '.').replace('!', '.').replace('&', '.').replace('^', '.').replace('*', '.')
		pattern = r'(.)\1+'
		repl = r'\1'
		return re.sub(pattern,repl,outname).strip()

class PyTDL(object):
	"""pytube control class"""
	
	# Лог ошибок
	fileLogs = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("logs.txt"))
	
	# Quality = 240p, 360p, 480p, 720p, 1024p ....
	Quality = ''
	# isVideoCount = "1/5 720p" к каждому видео
	isVideoCount = ''
	# onVideo - Информация о текущем видео в случае выведения в лог ошибок
	onVideo = []
	# video_url - Получение всех ссылок плейлиста, в т.ч. из файла. 
	video_url = []

	def __init__(self, link: str, loadDir: str = '', playListFile: str = '', 
				isPlayList: bool = False, isSaveInfo: bool = False, isSaveURL: bool = False, isSaveIndex: bool = False, isSaveName: bool = False,
				isSaveQuality: bool = True, isCli: bool = True):
		'''
			self.url - текущая ссылка пользователя
			self.isPlayList - Флаг плейлиста
			self.loadDir - Директория для скачивания. При наличии, автоматически проверяется на существование и при отсутствии - создаётся
			self.plFile - Файл плейлиста. При наличии, проверяется директория, в которой он располагается на существование. 
							При отсутствии директории родителя задаётся значение по умолчанию.
			self.isSaveInfo - Флаг сохранении всей информации о плейлисте или одном видео.
			self.isSaveURL - Флаг сохранения ссылок плейлиста или одного видео.
			self.isSaveIndex - Флаг сохранения индексации видео только при сохранении текстовой информации. 
							Индексация файлов плейлиста автоматическая и не изменяется во избежание конфликтов имён.
			self.isSaveName - Флаг сохранения наименований видео плейлиста или одного видео.
			self.isSaveQuality - Флаг сохранения разрешения видео при наименовании файлов плейлиста или одного видео.
			self.isCli - Флаг вывода сообщений консоли.
		'''
		self.url = link
		self.isPlayList = isPlayList
		if loadDir == '':
			self.loadDir = str(pathlib.Path(pathlib.Path.cwd()).resolve())
		else:
			self.loadDir = Files.checkPath(loadDir)
		if playListFile == '':
			self.plFile = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("playlist.txt"))
		else:
			if Files.checkPathText(playListFile):
				self.plFile = playListFile
			else:
				self.plFile = str(pathlib.Path(pathlib.Path.cwd()).resolve().joinpath("playlist.txt"))
		self.isSaveInfo = isSaveInfo
		self.isSaveURL = isSaveURL
		self.isSaveIndex = isSaveIndex
		self.isSaveName = isSaveName
		self.isSaveQuality = isSaveQuality
		self.isCli = isCli

	

if __name__ == '__main__':
	pass
