# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "serializers"
"""
  * @File    :   serializers.py
  * @Time    :   2024/10/31 09:03:44
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :
"""

from rest_framework import serializers


# Serializers define the API representation.
class Serializer(serializers.ModelSerializer):

    default_value = None
    default_value_map = {}
    filtered_fields = ["id"]

    @classmethod
    def initial(
        cls,
        instance=None,
        default_value=None,
        default_value_map=None,
        filtered_fields=None,
        *args,
        **kwargs,
    ):
        admin_model_serializer = cls(instance)
        admin_model_serializer.default_value = default_value
        if default_value_map != None and type(default_value_map) == type({}):
            admin_model_serializer.default_value_map = default_value_map
        if filtered_fields != None and type(filtered_fields) == type([]):
            admin_model_serializer.filtered_fields = filtered_fields
        return admin_model_serializer

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            try:
                if not value:
                    if key in self.default_value_map.keys():
                        data[key] = self.default_value_map.get(key)
                    else:
                        data[key] = self.default_value
            except KeyError:
                continue
            except:
                continue
        dataCache = data.copy()
        for key in dataCache.keys():
            if self.filtered_fields and key in self.filtered_fields:
                del data[key]
        return data
