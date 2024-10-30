# Copyright(C) 2010-2013 Bezleputh
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

from .base import BaseObject, Capability, StringField
from .date import DateField

__all__ = ['BaseJobAdvert', 'CapJob']


class BaseJobAdvert(BaseObject):
    """
    Represents a job announce.
    """
    publication_date = DateField('Date when the announce has been published')
    society_name =     StringField('Name of the society taht published the announce')
    place =            StringField('Place where the job take place')
    job_name =         StringField('Name of the job')
    title =            StringField('Title of the announce')
    contract_type =    StringField('Type of the contrat : CDI, CDD')
    pay =              StringField('Amount of the salary')
    description =      StringField('Description of the job')
    formation =        StringField('Required formation')
    experience =       StringField('Required experience')

    def __str__(self):
        message = '\r\n-- Advert --\r\n'
        message += 'id : %s\r\n' % self.id
        message += 'url : %s\r\n' % self.url
        message += 'publication_date : %s\r\n' % self.publication_date
        message += 'society_name : %s\r\n' % self.society_name
        message += 'place : %s\r\n' % self.place
        message += 'job_name : %s\r\n' % self.job_name
        message += 'title : %s\r\n' % self.title
        message += 'contract_type : %s\r\n' % self.contract_type
        message += 'pay : %s\r\n' % self.pay
        message += 'description : %s\r\n' % self.description
        message += 'formation : %s\r\n' % self.formation
        message += 'experience : %s\r\n' % self.experience
        return message

    @classmethod
    def id2url(cls, _id):
        """Overloaded in child classes provided by backends."""
        raise NotImplementedError()

    @property
    def page_url(self):
        """
        Get page URL of the announce.
        """
        return self.id2url(self.id)


class CapJob(Capability):
    """
    Capability of job annouce websites.
    """

    def search_job(self, pattern=None):
        """
        Iter results of a search on a pattern.

        :param pattern: pattern to search on
        :type pattern: str
        :rtype: iter[:class:`BaseJobAdvert`]
        """
        raise NotImplementedError()

    def advanced_search_job(self):
        """
         Iter results of an advanced search

        :rtype: iter[:class:`BaseJobAdvert`]
        """

    def get_job_advert(self, _id, advert=None):
        """
        Get an announce from an ID.

        :param _id: id of the advert
        :type _id: str
        :param advert: the advert
        :type advert: BaseJobAdvert
        :rtype: :class:`BaseJobAdvert` or None if not found.
        """
        raise NotImplementedError()
