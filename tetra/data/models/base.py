"""
Copyright 2016 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from tetra.data.db_handler import get_handler


class BaseModel(object):

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return dict(self.__dict__)

    @classmethod
    def create(cls, resource, handler=None):
        handler = handler or get_handler()
        return handler.create(resource)

    @classmethod
    def get(cls, resource_id, handler=None):
        handler = handler or get_handler()
        return handler.get(resource_id=resource_id, resource_class=cls)

    @classmethod
    def get_all(cls, handler=None):
        handler = handler or get_handler()
        return handler.get_all(resource_class=cls)

    @classmethod
    def delete(cls, resource_id, handler=None):
        handler = handler or get_handler()
        return handler.delete(resource_id=resource_id, resource_class=cls)