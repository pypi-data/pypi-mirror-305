# Copyright(C) 2010-2021 Nicolas Duhamel
#
# This file is part of woob.
#
# woob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# woob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with woob. If not, see <http://www.gnu.org/licenses/>.

from copy import copy
from posixpath import sep, join


class WorkingPath:
    def __init__(self):
        self.split_path = []
        self.previous = copy(self.split_path)

    def cd1(self, user_input):
        """
        Append *one* level to the current path.
        This means that separators (/) will get escaped.
        """
        split_path = self.get()
        split_path.append(user_input)
        self.location(split_path)

    def location(self, split_path):
        """
        Go to a new path, and store the previous path.
        """
        self.previous = self.get()
        self.split_path = split_path

    def restore(self):
        """
        Go to the previous path
        """
        self.split_path, self.previous = self.previous, self.split_path

    def home(self):
        """
        Go to the root
        """
        self.location([])

    def up(self):
        """
        Go up one directory
        """
        self.location(self.split_path[:-1])

    def get(self):
        """
        Get the current working path
        """
        return copy(self.split_path)

    def __str__(self):
        return join(sep, *[s.replace('/', r'\/') for s in self.split_path])
